# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) database to local database (mosivo)
"""

class UpdateFromRDB():
    """This class update all the tables necesary to the simulation
    """

    def __init__(self,ldb,rdb):
        """Class initialization function

        :param ldb: local database.
        :type ldb: DAL connection.
        :param rdb: remote database.
        :type rdb: DAL connection.
        """
        self.ldb = ldb
        self.rdb = rdb

    # def uDepartamento(self):
    #     """Get data DGF.Deptos
    #     """
    #     # print "uDepartamento"
    #     # print self.rdb.tables()
    #     # print self.rdb.Deptos.fields()

    #     rQ = self.rdb(
    #         self.rdb.Deptos
    #     ).select(
    #         self.rdb.Deptos.Codigo,
    #         self.rdb.Deptos.Nombre,
    #         self.rdb.Deptos.Numero,
    #         orderby = self.rdb.Deptos.Nombre
    #     )

    #     if len(rQ) > 0:
    #         # Set sequence in departamento
    #         self.ldb.executesql("ALTER SEQUENCE departamento_id_seq MINVALUE 0;")
    #         self.ldb.executesql("SELECT setval('departamento_id_seq', 0, true);")
    #         # Delete all data in table departamento
    #         self.ldb(self.ldb.departamento).delete()
    #         for row in rQ:
    #             self.ldb.departamento.insert(
    #                 codigo = row.Codigo,
    #                 nombre = row.Nombre,
    #                 numero = row.Numero
    #             )
    #         self.ldb.commit()

    def uGenero(self):
        """Get genero data from DGF.Plantas    
        """
        rQ = self.rdb(
            (self.rdb.Planes.CodG_Dec == self.rdb.Plantas.CodG)
        ).select(
            self.rdb.Planes.CodG_Dec,
            self.rdb.Plantas.Genero,           
            orderby=self.rdb.Planes.CodG_Dec,
            distinct=True
        )

        if len(rQ) > 0:
            # Set sequence in genero
            self.ldb.executesql("ALTER SEQUENCE genero_id_seq MINVALUE 0;")
            self.ldb.executesql("SELECT setval('genero_id_seq', 0, true);")
            # Delete all data in table genero
            self.ldb(self.ldb.genero).delete()
            for row in rQ:
                # print "%s | %s" % (row.Plantas.Genero,row.Planes.CodG_Dec)
                self.ldb.genero.insert(
                    nombre=row.Plantas.Genero,
                    codigo=row.Planes.CodG_Dec
                )
            self.ldb.commit()

    def uEspecie(self):
        """Get especie data from DGF.Plantas    
        """
        rQ = self.rdb(
            (self.rdb.Planes.CodG_Dec == self.rdb.Plantas.CodG) &
            (self.rdb.Planes.CodE_Dec == self.rdb.Plantas.CodE)
        ).select(
            self.rdb.Planes.CodG_Dec,
            self.rdb.Planes.CodE_Dec,
            self.rdb.Plantas.Especie,            
            orderby=self.rdb.Planes.CodG_Dec,
            distinct=True
        )

        if len(rQ) > 0:
            # Set sequence in genero
            self.ldb.executesql("ALTER SEQUENCE especie_id_seq MINVALUE 0;")
            self.ldb.executesql("SELECT setval('especie_id_seq', 0, true);")
            # Delete all data in table genero
            self.ldb(self.ldb.especie).delete()
            gcti = self.gCodToId()
            for row in rQ:
                print "%d,%s,%s" % (gcti[row.Planes.CodG_Dec],row.Plantas.Especie,row.Planes.CodE_Dec) 
                self.ldb.especie.insert(
                    genero = gcti[row.Planes.CodG_Dec],
                    nombre = row.Plantas.Especie,
                    codigo = row.Planes.CodE_Dec
                )
            self.ldb.commit()

    def dCodToId(self):
        """Util function that return a dictionary with ids of codes of departamento
        
        :returns:  dict -- keys = code, values = ids.
        """
        codtoid = {} 
        lQ = self.ldb(
            self.ldb.departamento
        ).select(
            self.ldb.departamento.id,
            self.ldb.departamento.codigo
        )
        for row in lQ:
            codtoid[row.codigo] = row.id
        return (codtoid)

    def gCodToId(self):
        """Util function that return a dictionary with ids of codes of genero
        :returns:  dict -- keys = code, values = ids.
        """
        codtoid = {} 
        lQ = self.ldb(
            self.ldb.genero
        ).select(
            self.ldb.genero.id,
            self.ldb.genero.codigo
        )
        for row in lQ:
            codtoid[row.codigo] = row.id
        return (codtoid)

    def cNumToId(self,cnum):
        """Util function that return id for a numero de carpeta in carpeta
        :returns:  int -- id of the number of .
        """
        lQ = self.ldb(
            self.ldb.carpeta
        ).select(
            self.ldb.carpeta.id,
            self.ldb.carpeta.numero_carpeta
        ).first()
        return (lQ.id)

    def uCarpeta(self):
        """Get carpeta data from DGF.Carpetas_P
        """
        # & AND, | OR    
        rQ = self.rdb(
            (self.rdb.Carpetas_P.Nro_Carpeta==self.rdb.Planes_Pro.Codigo_Cp) &
            (self.rdb.Planes_Pro.Codigo==self.rdb.Planes.Codigo_Plan_Pro) &
            (self.rdb.Planes.Ha_Dec>0) &
            (self.rdb.Planes.Ano_Dec>1900) & (self.rdb.Planes.Ano_Dec<2100)
        ).select(
            self.rdb.Carpetas_P.Nro_Carpeta,
            self.rdb.Carpetas_P.Cod_Depto,
            self.rdb.Carpetas_P.Cod_Sj,
            self.rdb.Carpetas_P.Longitud,
            self.rdb.Carpetas_P.Latitud,
            orderby = self.rdb.Carpetas_P.Nro_Carpeta,
            distinct = True
        )        
    
        if len(rQ) > 0:
            # Set sequence in departamento
            self.ldb.executesql("ALTER SEQUENCE carpeta_id_seq MINVALUE 0;")
            self.ldb.executesql("SELECT setval('carpeta_id_seq', 0, true);")
            # Delete all data in table carpeta
            self.ldb(self.ldb.carpeta).delete()
            # Get id for cod departamento
            dcodtoid = self.dCodToId()
            for row in rQ:
                # print "%i | %s" % (row.Nro_Carpeta,row.Cod_Depto)
                self.ldb.carpeta.insert(
                    numero_carpeta = row.Nro_Carpeta,
                    departamento = dcodtoid[row.Cod_Depto.upper()],    
                    sec_judicial = row.Cod_Sj,
                    lon = row.Longitud,
                    lat = row.Latitud
                )
            self.ldb.commit()

    def uPlan(self):
        """Get plan data from DGF.Planes
        """
        rQ = self.rdb(
            (self.rdb.Carpetas_P.Nro_Carpeta==self.rdb.Planes_Pro.Codigo_cp) &
            (self.rdb.Planes_Pro.Codigo==self.rdb.Planes.Codigo_Plan_Pro) &
            (self.rdb.Planes.Ha_Dec>0) &
            (self.rdb.Planes.Ano_Dec>1900) & (self.rdb.Planes.Ano_Dec<2100)
        ).select(
            self.rdb.Planes.Codigo,
            self.rdb.Carpetas_P.Nro_Carpeta,
            self.rdb.Planes.CodG_Dec,
            self.rdb.Planes.CodE_Dec,
            self.rdb.Planes.Ano_Dec,
            self.rdb.Planes.Ha_Dec
        )
    
        if len(rQ) > 0:
            # Set sequence in plan
            self.ldb.executesql("ALTER SEQUENCE plan_id_seq MINVALUE 0;")
            self.ldb.executesql("SELECT setval('plan_id_seq', 0, true);")
            # Delete all data in table plan
            self.ldb(self.ldb.plan).delete()
            for row in rQ:
                self.ldb.carpeta.insert(
                    carpeta = self.cNumToId(row.Nro_Carpeta),
                    especie = row[2],    
                    anio_plantado = row.Ano_Dec,
                    area_afectada = row.Ha_Dec
                )
            self.ldb.commit()

    def uAll(self):
        """Util function to update all the data from remote database to local database
        """
        # Order is important
        # self.uDepartamento()
        # self.uGenero()
        # self.uEspecie()
        # self.uCarpeta()
        # self.uPlan()
        pass
        