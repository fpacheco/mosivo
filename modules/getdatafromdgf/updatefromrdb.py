# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) to local database (mosivo)
"""
from gluon.dal import DAL

class UpdateFromRDB():
    """This class update all the tables necesary to the simulation
    """

    def __init__(self, mDatabase, inDGF=True):
        """Class initialization function

        :param mDatabase: local database (MoSiVo).
        :type mDatabase: DAL connection.
        :param inDGF: App is in DGF.
        :type inDGF: Bool.
        """
        self._db = mDatabase
        # DGF connection. Please use read only user
        user='mosivo'
        passw=''
        if inDGF:
            self.rdb = DAL("mssql://%s:%s@192.168.20.7/DGF" % (user, passw), migrate_enabled=False, migrate=False)
        else:
            self.rdb = DAL('sqlite://dgf_database.db', migrate_enabled=False, migrate=False)


    def __dsj2id(self, idDepto, idSj):
        if idDepto and idSj:
            r = self._db(
                ( self._db['seccionjudicial']['id']>0 ) &
                ( self._db['seccionjudicial']['nombre']==int(idSj) ) &
                ( self._db['seccionjudicial']['departamento']==int(idDepto) )
            ).select(
                self._db['seccionjudicial']['id']
            )
            if len(r)==1:
                return int( r[0]['id'] )
            else:
                return None
        else:
            return None


    def uPlan(self):
        """Inserta todas las carpetas no nulas y que no esten con bajas
        """
        sql = "SELECT DISTINCT cp.Nro_Carpeta, d.Numero, cp.Cod_Sj, cp.Longitud, cp.Latitud " \
            "FROM Carpetas_P cp, Deptos d " \
            "WHERE d.Codigo=cp.Cod_Depto AND cp.Baja=0 AND cp.Nro_Carpeta IS NOT NULL AND " \
            "cp.Cod_Depto IS NOT NULL AND cp.Cod_Sj IS NOT NULL AND cp.Cod_Sj>0 ORDER BY cp.Nro_Carpeta"
        rows = self.rdb.executesql(sql)

        if len(rows) > 0:            
            # Delete all data in table carpeta
            self._db.executesql("DELETE FROM plan")
            # Set sequence in departamento
            self._db.executesql("ALTER SEQUENCE plan_id_seq MINVALUE 0")
            self._db.executesql("SELECT setval('plan_id_seq', 0, true)")            
            self._db.commit()
            try:
                for r in rows:
                    self._db['plan'].insert(
                        ncarpeta=r[0],
                        sjudicial=self.__dsj2id(r[1],r[2]),
                        lon = r[3],
                        lat = r[4]
                    )
                self._db.commit()                
                return True
            except Exception as e:
                print "Error: %s" % e
                self._db.rollback()
                return False

    def __ge2idE(self, gen, esp):
        g=gen.strip()
        e=esp.strip()
        if len(g)>0 and len(e)>0:
            r = self._db(
                ( self._db['especie']['id']>0 ) &
                ( self._db['especie']['genero']==self._db['genero']['id'] ) &
                ( self._db['genero']['nombre']==g ) &
                ( self._db['especie']['nombre']==e)
            ).select(
                self._db['especie']['id']
            )
            if len(r)==1:
                return int( r[0]['id'] )
            else:
                return None
        else:
            return None


    def uRodalD(self):
        """Inserta rodales declarados para cada carpeta
        """
        lrows = self._db(
                ( self._db['plan']['id']>0 )
        ).select(
                self._db['plan']['id'],
                self._db['plan']['ncarpeta']
        )
        if len(lrows)>0:
            #self._db( self._db['rodald'] ).delete()
            self._db.executesql("DELETE FROM rodald")
            self._db.executesql("ALTER SEQUENCE rodald_id_seq MINVALUE 0")
            self._db.executesql("SELECT setval('rodald_id_seq', 0, true)")
            self._db.commit()
            try:
                for lr in lrows:
                    id=lr['id']
                    idCarpeta=lr['ncarpeta']
                    #RFPV - TODO: Desde al vista en DGF
                    sql = "SELECT DISTINCT pl.Genero,pl.Especie,p.Ano_Dec,p.Ha_Dec FROM Planes p, Planes_Pro pp, Carpetas_P cp, Plantas pl WHERE p.CodG_Dec IS NOT NULL AND p.CodE_Dec IS NOT NULL AND pp.Codigo_Cp=cp.Codigo AND pp.Codigo==p.Codigo_Plan_Pro AND p.Ano_Dec>0 AND p.Ha_Dec>0 AND cp.Nro_Carpeta=%d AND pl.CodG=p.CodG_Dec AND pl.CodE=p.CodE_Dec ORDER BY p.Ano_Dec" % idCarpeta
                    rows = self.rdb.executesql(sql)
                    if len(rows)>0:                    
                        try:
                            for r in rows:
                                self._db['rodald'].insert(
                                    plan=id,
                                    especie=self.__ge2idE(r[0],r[1]),
                                    anioplant=int(r[2]),
                                    areaafect=float(r[3])
                                )
                        except Exception as e:
                            print "Error: %s" % e
                            raise Exception("uRodalD!")
                self._db.commit()
                return True
            except Exception as e:
                print "Error: %s" % e
                self._db.rollback()
                return False
                

    def uGenero(self):
        """Get genero data from DGF.Plantas
        """
        sql = "SELECT DISTINCT CodG,Genero FROM Plantas WHERE Genero IS NOT NULL ORDER BY Genero"
        rows = self.rdb.executesql(sql)

        if len(rows) > 0:
            # Delete all data in table genero
            self._db.executesql("DELETE FROM genero")
            # Set sequence in genero
            self._db.executesql("ALTER SEQUENCE genero_id_seq MINVALUE 0;")
            self._db.executesql("SELECT setval('genero_id_seq', 0, true);")
            self._db.commit()
            try:
                for r in rows:
                    self._db.genero.insert(
                            nombre=str(r[1]).strip(),
                            codigo=str(r[0]).strip()
                    )
                self._db.commit()                                
                return True
            except Exception as e:
                print "Error: %s" % e
                self._db.rollback()
                return False


    def uEspecie(self):
        """Get especie data from DGF.Plantas
        """
       
        lrows = self._db(
            ( self._db['genero']['id']>0 )
        ).select (
            self._db['genero']['id'],
            self._db['genero']['nombre'],
            self._db['genero']['codigo']
        )

        if len(lrows)>0:
            # Delete all data in table especie
            self._db.executesql("DELETE FROM especie;")
            # Set sequence in especie
            self._db.executesql("ALTER SEQUENCE especie_id_seq MINVALUE 0;")
            self._db.executesql("SELECT setval('especie_id_seq', 0, true);")

            self._db.commit()
            try:           
                for lr in lrows:
                    id=int( lr['id'] )
                    genero=lr['nombre']
                    sql = 'SELECT CodE, Especie FROM Plantas WHERE Genero LIKE \'' + str(genero) + '%\''
                    print sql
                    rows=self.rdb.executesql(sql)                    
                    try:
                        for r in rows:
                            self._db.especie.insert(
                                genero = id,
                                nombre = str(r[1]).strip(),
                                codigo = str(r[0]).strip()
                            )                        
                    except Exception as e:
                        print "Error: %s" % e
                        raise Exception('Especie error')                        
                self._db.commit()
                return True              
            except Exception as e:
                print "Error: %s" % e
                self._db.rollback()
                return False
                

    def uAll(self):
        """Util function to update all the data from remote database to local database
        """
        # Order is important
        self.uGenero()
        self.uEspecie()
        self.uPlan()
        self.uRodalD()
