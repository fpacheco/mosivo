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


    def uPlanTmp(self):
        """Inserta todas las carpetas no nulas y que no esten con bajas en una tabla
        temporal de MoSiVo (plantmp)
        """
        sql = "SELECT DISTINCT cp.Nro_Carpeta, d.Numero, cp.Cod_Sj, cp.Longitud, cp.Latitud " \
            "FROM Carpetas_P cp, Deptos d " \
            "WHERE d.Codigo=cp.Cod_Depto AND cp.Baja=0 AND cp.Nro_Carpeta IS NOT NULL AND " \
            "cp.Cod_Depto IS NOT NULL AND cp.Cod_Sj IS NOT NULL AND cp.Cod_Sj>0 ORDER BY cp.Nro_Carpeta"
        rows = self.rdb.executesql(sql)

        if len(rows) > 0:
            # Delete all data in table carpeta
            self._db.executesql("DELETE FROM plantmp")
            # Set sequence in departamento
            self._db.executesql("ALTER SEQUENCE plantmp_id_seq MINVALUE 0")
            self._db.executesql("SELECT setval('plantmp_id_seq', 0, true)")

            self._db.commit()
            try:
                for r in rows:
                    self._db['plantmp'].insert(
                        ncarpeta=r[0],
                        depto=r[1],
                        sj=r[2],
                        lon = r[3],
                        lat = r[4]
                    )
                self._db.commit()
                return True
            except Exception as e:
                print "Error: %s" % e
                self._db.rollback()
                return False


    def uPT2P(self):
        """Pasa de plantmp a plan
        """
        # Delete all data in table plan
        self._db.executesql("DELETE FROM plan")
        # Set sequence in plan
        self._db.executesql("ALTER SEQUENCE plan_id_seq MINVALUE 0")
        self._db.executesql("SELECT setval('plan_id_seq', 0, true)")

        sql = "INSERT INTO plan(ncarpeta,sjudicial,lon,lat) "
        sql += "(SELECT pt.ncarpeta, sj.id, pt.lon, pt.lat "
        sql += "FROM plantmp pt, seccionjudicial sj "
        sql += "WHERE pt.depto=sj.departamento AND pt.sj=sj.nombre "
        sql += "ORDER BY pt.ncarpeta)"
        try:
            rows = self._db.executesql(sql)
            return True
        except Exception as e:
            print "Error: %s" % e
            return False


    def uPlan(self):
        """Actualiza en dos etapas plan desde DGF
        """
        if self.uPlanTmp():
            if self.uPT2P():
                return True
            else:
                return False
        else:
            return False


    def uRodalDTmp(self):
        """Inserta rodales declarados para cada carpeta
        """
        self._db.executesql("DELETE FROM rodaldtmp")
        self._db.executesql("ALTER SEQUENCE rodaldtmp_id_seq MINVALUE 0")
        self._db.executesql("SELECT setval('rodaldtmp_id_seq', 0, true)")

        '''
        sql = "SELECT cp.Nro_Carpeta, pl.Genero, pl.Especie, p.Ano_Dec, p.Ha_Dec "
        sql += "FROM Planes p, Planes_Pro pp, Carpetas_P cp, Plantas pl "
        sql += "WHERE p.CodG_Dec IS NOT NULL AND p.CodE_Dec IS NOT NULL AND " \
            "pp.Codigo_Cp=cp.Nro_Carpeta AND pp.Codigo=p.Codigo_Plan_Pro AND " \
            "p.Ano_Dec>0 AND p.Ha_Dec>0 AND " \
            "pl.CodG=p.CodG_Dec AND pl.CodE=p.CodE_Dec ORDER BY cp.Nro_Carpeta"
        '''
        #####################################################################
        # RFPV - Muy importante:
        # Planes_Pro.Codigo_Cp=Carpetas_P.Nro_Carpeta
        # Planes_Pro.Codigo=Planes.Codigo_Plan_Pro
        # RFPV - Muy importante
        ####################################################################
        sql = "SELECT cp.Nro_Carpeta, pl.Genero, pl.Especie, p.Anio_Dec, p.Ha_Dec "
        sql += "FROM Planes_View p, Planes_Pro pp, Carpetas_P cp, Plantas pl "
        sql += "WHERE p.CodG_Dec IS NOT NULL AND p.CodE_Dec IS NOT NULL AND " \
            "pp.Codigo_Cp=cp.Nro_Carpeta AND pp.Codigo=p.Codigo_Plan_Pro AND " \
            "p.Anio_Dec>0 AND p.Ha_Dec>0 AND " \
            "pl.CodG=p.CodG_Dec AND pl.CodE=p.CodE_Dec ORDER BY cp.Nro_Carpeta"
        rows = self.rdb.executesql(sql)

        self._db.commit()
        try:
            for r in rows:
                self._db['rodaldtmp'].insert(
                    ncarpeta=r[0],
                    ngen=r[1].strip(),
                    nesp=r[2].strip(),
                    anioplant=int(r[3]),
                    areaafect=float(r[4])
                )
            self._db.commit()
            return True
        except Exception as e:
            print "Error: %s" % e
            self._db.rollback()
            return False


    def uRDT2RD(self):
        """Pasa de rodaldtmp a rodald
        """
        # Delete all data in table plan
        self._db.executesql("DELETE FROM rodald")
        # Set sequence in plan
        self._db.executesql("ALTER SEQUENCE rodald_id_seq MINVALUE 0")
        self._db.executesql("SELECT setval('rodald_id_seq', 0, true)")

        sql = "INSERT INTO rodald(plan,especie,anioplant,areaafect) "
        sql += "(SELECT p.id, e.id, rdt.anioplant, rdt.areaafect "
        sql += "FROM plan p, especie e, genero g, rodaldtmp rdt "
        sql += "WHERE rdt.ncarpeta=p.ncarpeta AND e.nombre=rdt.nesp AND g.nombre=rdt.ngen AND " \
            "e.genero=g.id "
        sql += "ORDER BY rdt.ncarpeta)"
        try:
            rows = self._db.executesql(sql)
            return True
        except Exception as e:
            print "Error: %s" % e
            return False


    def uRodalD(self):
        """Actualiza en dos etapas rodald desde DGF
        """
        if self.uRodalDTmp():
            if self.uRDT2RD():
                return True
            else:
                return False
        else:
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
        return [
            self.uGenero(),
            self.uEspecie(),
            self.uPlan(),
            self.uRodalD()
        ]
