# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) database to local database (mosivo)
"""
import gluon
from gluon.dal import  Field
from gluon.dal import DAL 
from gluon import current

IN_DGF = False

class DGFModel():
    """This class update all the tables necessary to the simulation
    """

    def __init__(self):
        """Class initialization function
        """
        # DGF connection. Please use read only user
        try:
            if IN_DGF:
                self.rdb = DAL("mssql://fpacheco:fpacheco@192.168.20.7/DGF", migrate_enabled=False, migrate=False)
            else:
                self.rdb = DAL('sqlite://dgf_database.db', migrate_enabled=False, migrate=False)
            self.session = current.session
            self.request = current.request
            self.response = current.response
            self.cache = current.cache
            self.__define_tables()
            print self.rdb.tables()
        except:
            print "DGFModel: Can't load database!."


    def __define_tables(self):
        """Define all necessary tables in DGF
        """

        self.rdb.define_table('Deptos',
            Field('Codigo', type='string', length=1),
            Field('Nombre', type='string'),
            Field('Numero', type='integer'),
            primarykey=['Codigo'],
            migrate=False
        )

        self.rdb.define_table('Carpetas_P',
            Field('Codigo', type='integer'),
            # El numero de la carpeta
            Field('Nro_Carpeta', type='integer'),
            Field('Fecha_Pres', type='integer'),
            # Solo funciona así por el tema de que es un string
            Field('Cod_Depto', 'reference Deptos.Codigo'),
            Field('Cod_Sj', type='integer'),
            Field('Longitud', type='double'),
            Field('Latitud', type='double'),
            Field('Baja', type='boolean'),
            Field('Notas', type='string'),
            primarykey=['Codigo'],
            migrate=False
        )

        self.rdb.define_table('Plantas',
            Field('CodG', type='string'),
            Field('CodE', type='integer'),
            Field('Genero', type='string'),
            Field('Especie', type='string'),
            Field('Descripcion', type='string'),
            Field('Apel', type='string'),
            Field('Carac', type='text'),
            Field('Foto', type='upload'),
            Field('Taxo', type='upload'),
            primarykey=['CodG', 'CodE'],
            migrate=False
        )

        self.rdb.define_table('Carpetas_BN',
            Field('Codigo', type='integer'),
            # El numero de la carpeta
            Field('Nro_Carpeta', type='integer'),
            Field('Fecha_pres', type='integer'),
            Field('Cod_Depto','reference Deptos.Codigo'),
            Field('Cod_Sj', type='integer'),
            Field('Latitud', type='double'),
            Field('Longitud', type='double'),
            Field('Tipo_Bosque', type='string'),
            Field('Baja', type='boolean'),
            Field('Notas', type='string'),
            primarykey=['Codigo'],
            migrate=False
        )

        b = u'Año_Pro'
        a = b.encode('utf8')

        self.rdb.define_table('Planes_Pro',
            Field('Codigo', type='integer'),
            # El numero de la carpeta Carpetas_P(Nro_Carpeta)
            Field('Codigo_Cp', type='integer'),
            Field('Fecha_Act', type='datetime'),
            # RFPV - Esto da lio nombre de campo con caracter especial
            # Field('Año_Pro', type='integer'),
            # Field(a,type='integer'),
            Field('Ano_Pro', type='integer'),
            Field('CodG_Pro', type='string'),
            Field('CodE_Pro', type='integer'),
            Field('Epo_Pro', type='string'),
            Field('Ha_Pro', type='double'),
            Field('Den_Pro', type='integer'),
            Field('E1_Pro', type='integer'),
            Field('E2_Pro', type='integer'),
            Field('E3_Pro', type='integer'),
            Field('Cal_Pro', type='string'),
            Field('Met_Pro', type='string'),
            Field('Sem_Pro', type='string'),
            Field('Planta_Pro', type='string'),
            Field('Tipo_Planta_Pro', type='string'),
            Field('Raleo_Pro', type='string'),
            Field('Poda_Pro', type='string'),
            Field('Corta_Pro', type='string'),
            Field('Objetivo_pro', type='string'),
            Field('Proyecto_g_pro', type='string'),
            Field('Observaciones', type='string'),
            primarykey=['Codigo'],
            migrate=False
        )

        self.rdb.define_table('Planes',
            Field('Codigo', type='integer'),
            # El codigo de Planes_Pro
            Field('Codigo_Plan_Pro', type='integer'),
            Field('Fecha_Act', type='datetime'),
            # RFPV - Esto da lio nombre de campo con caracter especial
            # Field('Año_Dec', type='integer'),
            # Field('Ano_Dec', type='integer'),
            Field('CodG_Dec', type='string'),
            Field('CodE_Dec', type='integer'),
            Field('Epo_Dec', type='string'),
            Field('Ha_Dec', type='double'),
            Field('Den_Dec', type='integer'),
            Field('E1_Dec', type='integer'),
            Field('E2_Dec', type='integer'),
            Field('E3_Dec', type='integer'),
            Field('Cal_Dec', type='string'),
            Field('Met_Dec', type='string'),
            Field('Sem_Dec', type='string'),
            Field('Planta_Dec', type='string'),
            Field('Tipo_Planta_Dec', type='string'),
            Field('Raleo_Dec', type='string'),
            Field('Poda_Dec', type='string'),
            Field('Corta_Dec', type='string'),
            Field('Objetivo_dec', type='string'),
            Field('Proyecto_g_dec', type='string'),
            Field('Observaciones', type='string'),
            primarykey=['Codigo'],
            migrate=False
        )

        self.rdb.define_table('Propietarios',
            Field('Codigo', type='integer'),
            Field('Nombre', type='string'),
            Field('Direccion', type='string'),
            Field('Telefono', type='string'),
            Field('Representacion', type='string'),
            primarykey=['Codigo'],
            migrate=False
        )

        self.rdb.define_table('Registro',
            Field('Codigo', type='integer'),
            #Field('Codigo_Cp_Pr',self.rdb.Carpetas_P),
            #Field('Codigo_Cp_Bn',self.rdb.Carpetas_BN),
            Field('Codigo_Cp_Pr', type='integer'),
            Field('Codigo_Cp_Bn', type='integer'),
            # Solo funciona así por el tema de que es un string
            Field('Cod_Depto', 'reference Deptos.Codigo'),
            Field('Codigo_Pad', type='integer'),
            Field('Anexo', type='string'),
            Field('Tipo_Bos', type='string'),
            Field('Cant_Bosques', type='integer'),
            Field('Cant_Tipo_Bosque', type='integer'),
            Field('Cant_Tipo_Bosque_Depto', type='integer'),
            Field('Resoluciones', type='string'),
            Field('Codigo_Prop', self.rdb.Propietarios),
            Field('Rep_Prop', type='string'),
            Field('Area', type='double'),
            Field('Tipo_Prop', type='string'),
            primarykey=['Codigo'],
            migrate=False
        )


    def db(self):
        """
        Get the database connection

        :returns:  DAL connection for DGF database
        """
        return (self.rdb)
