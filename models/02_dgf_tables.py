# -*- coding: utf-8 -*-
"""
Tables in DGF database
"""
dgfdb.define_table('Deptos',
    Field('Codigo',type='string',length=1),
    Field('Nombre',type='string'),
    Field('Numero',type='integer'),
    primarykey=['Codigo'],
    migrate=False    
)

dgfdb.define_table('Carpetas_P',
    Field('Codigo',type='integer'),
    # El numero de la carpeta
    Field('Nro_Carpeta',type='integer'),
    Field('Fecha_Pres',type='integer'),
    # Solo funciona así por el tema de que es un string
    Field('Cod_Depto','reference Deptos.Codigo'),    
    Field('Cod_Sj',type='integer'),
    Field('Longitud',type='double'),
    Field('Latitud',type='double'),
    Field('Baja',type='boolean'),
    Field('Notas',type='string'),
    primarykey=['Codigo'],
    migrate=False
)

dgfdb.define_table('Plantas',
    Field('CodG',type='string'),
    Field('CodE',type='integer'),
    Field('Genero',type='string'),
    Field('Especie',type='string'),
    Field('Descripcion',type='string'),
    Field('Apel',type='string'),
    Field('Carac',type='text'),
    Field('Foto',type='upload'),
    Field('Taxo',type='upload'),
    primarykey=['CodG','CodE'],
    migrate=False 
)

dgfdb.define_table('Carpetas_BN',
    Field('Codigo',type='integer'),
    # El numero de la carpeta
    Field('Nro_Carpeta',type='integer'),
    Field('Fecha_pres',type='integer'),
    Field('Cod_Depto','reference Deptos.Codigo'),
    Field('Cod_Sj',type='integer'),
    Field('Latitud',type='double'),
    Field('Longitud',type='double'),
    Field('Tipo_Bosque',type='string'),
    Field('Baja',type='boolean'),
    Field('Notas',type='string'),
    primarykey=['Codigo'],
    migrate=False
)

b = u'Año_Pro'
a = b.encode('utf8')

dgfdb.define_table('Planes_Pro',
    Field('Codigo',type='integer'),
    # El numero de la carpeta Carpetas_P(Nro_Carpeta)
    Field('Codigo_Cp',type='integer'),
    Field('Fecha_Act',type='datetime'),
    # RFPV - Esto da lio nombre de campo con caracter especial
    # Field('Año_Pro',type='integer'),
    # Field(a,type='integer'),
    Field('CodG_Pro',type='string'),
    Field('CodE_Pro',type='integer'),
    Field('Epo_Pro',type='string'),
    Field('Ha_Pro',type='double'),
    Field('Den_Pro',type='integer'),
    Field('E1_Pro',type='integer'),
    Field('E2_Pro',type='integer'),
    Field('E3_Pro',type='integer'),
    Field('Cal_Pro',type='string'),
    Field('Met_Pro',type='string'),
    Field('Sem_Pro',type='string'),
    Field('Planta_Pro',type='string'),
    Field('Tipo_Planta_Pro',type='string'),
    Field('Raleo_Pro',type='string'),
    Field('Poda_Pro',type='string'),
    Field('Corta_Pro',type='string'),
    Field('Objetivo_pro',type='string'),
    Field('Proyecto_g_pro',type='string'),
    Field('Observaciones',type='string'),
    primarykey=['Codigo'],
    migrate=False
)

dgfdb.define_table('Planes',
    Field('Codigo',type='integer'),
    # El codigo de Planes_Pro
    Field('Codigo_Plan_Pro',type='integer'),
    Field('Fecha_Act',type='datetime'),
    # RFPV - Esto da lio nombre de campo con caracter especial
    # Field('Año_Dec',type='integer'),
    Field('CodG_Dec',type='string'),
    Field('CodE_Dec',type='integer'),
    Field('Epo_Dec',type='string'),
    Field('Ha_Dec',type='double'),
    Field('Den_Dec',type='integer'),
    Field('E1_Dec',type='integer'),
    Field('E2_Dec',type='integer'),
    Field('E3_Dec',type='integer'),
    Field('Cal_Dec',type='string'),
    Field('Met_Dec',type='string'),
    Field('Sem_Dec',type='string'),
    Field('Planta_Dec',type='string'),
    Field('Tipo_Planta_Dec',type='string'),
    Field('Raleo_Dec',type='string'),
    Field('Poda_Dec',type='string'),
    Field('Corta_Dec',type='string'),
    Field('Objetivo_dec',type='string'),
    Field('Proyecto_g_dec',type='string'),
    Field('Observaciones',type='string'),
    primarykey=['Codigo'],
    migrate=False
)

dgfdb.define_table('Propietarios',
    Field('Codigo',type='integer'),
    Field('Nombre',type='string'),
    Field('Direccion',type='string'),
    Field('Telefono',type='string'),
    Field('Representacion',type='string'),
    primarykey=['Codigo'],
    migrate=False
)

dgfdb.define_table('Registro',
    Field('Codigo',type='integer'),
    #Field('Codigo_Cp_Pr',dgfdb.Carpetas_P),
    #Field('Codigo_Cp_Bn',dgfdb.Carpetas_BN),
    Field('Codigo_Cp_Pr',type='integer'),
    Field('Codigo_Cp_Bn',type='integer'),    
    # Solo funciona así por el tema de que es un string
    Field('Cod_Depto','reference Deptos.Codigo'),
    Field('Codigo_Pad',type='integer'),
    Field('Anexo',type='string'),
    Field('Tipo_Bos',type='string'),
    Field('Cant_Bosques',type='integer'),
    Field('Cant_Tipo_Bosque',type='integer'),
    Field('Cant_Tipo_Bosque_Depto',type='integer'),
    Field('Resoluciones',type='string'),
    Field('Codigo_Prop',dgfdb.Propietarios),
    Field('Rep_Prop',type='string'),
    Field('Area',type='double'),
    Field('Tipo_Prop',type='string'),
    primarykey=['Codigo'],
    migrate=False
)

"""
db.define_table('Access',
    Field('IDpiani',type='integer'),
    Field('FECHAACT',type='datetime'),
    Field('PROY',type='integer'),
    Field('DPTO',type='string'),
    Field('SECJUD',type='integer'),
    Field('PRESENTADO',type='integer'),
    Field('SupEstab',type='integer'),
    Field('AÑOPRO',type='integer'),
    Field('CodG',type='string'),
    Field('CodE',type='integer'),
    Field('EPOPRO',type='string'),
    Field('HAPRO',type='double'),
    Field('DENPRO',type='integer'),
    Field('EP1',type='integer'),
    Field('EP2',type='integer'),
    Field('EP3',type='integer'),
    Field('CALPRO',type='string'),
    Field('MPfor',type='string'),
    Field('MPorsem',type='string'),
    Field('MPorplanta',type='string'),
    Field('MPtipoplanta',type='string'),
    Field('MPraleo',type='string'),
    Field('MPpoda',type='string'),
    Field('MPcorta',type='string'),
    Field('Gendec',type='string'),
    Field('Espdec',type='integer'),
    Field('AÑODEC',type='integer'),
    Field('HADEC',type='double'),
    Field('FUSTAL',type='integer'),
    Field('REBROTE',type='integer'),
    Field('ABAJA',type='integer'),
    Field('EPODEC',type='string'),
    Field('DENDEC',type='integer'),
    Field('ED1',type='integer'),
    Field('ED2',type='integer'),
    Field('ED3',type='integer'),
    Field('CALDEC',type='string'),
    Field('MDfor',type='string'),
    Field('MDorsem',type='string'),
    Field('MDorplanta',type='string'),
    Field('MDtipoplanta',type='string'),
    Field('MDraleo',type='string'),
    Field('MDpoda',type='string'),
    Field('MDcorta',type='string'),
    Field('OBSERVACIO',type='string'),
    Field('BAJA',type='string'),
    Field('FIRMA',type='string'),
    Field('FUSTALDIF',type='integer')
)


db.define_table('Deptos',
    Field('Codigo',type='string', unique=True, notnull=True),
    Field('Nombre',type='string'),
    Field('Numero',type='integer')
)

db.define_table('Rodales',
    Field('Codigo',type='integer', unique=True, notnull=True),
    Field('Fila',type='integer'),
    Field('Cod_Mon',type='integer'),
    Field('Area',type='double'),
    Field('Densidad',type='integer'),
    Field('Densidad_Act',type='integer'),
    Field('Codg',type='string'),
    Field('Code',type='integer'),
    Field('Origen',type='string'),
    Field('Procedencia',type='string'),
    Field('Propietario',type='integer'),
    Field('Responsable',type='string'),
    Field('Establecimiento',type='string'),
    Field('Observador',type='string'),
    Field('Localizacion',type='string'),
    Field('Datum',type='boolean'),
    Field('Longitud_G',type='string'),
    Field('Latitud_G',type='string'),
    Field('Longitud',type='double'),
    Field('Latitud',type='double'),
    Field('Cod_depto',db.Deptos),
    Field('Tipo',type='string'),
    Field('Turno',type='integer'),
    Field('Edad',type='double'),
    Field('Altura',type='double'),
    Field('Laboreo_Tipo',type='integer'),
    Field('Poda1',type='boolean'),
    Field('Epoca_Poda1',type='string'),
    Field('Año_Poda1',type='integer'),
    Field('Raleo1',type='boolean'),
    Field('Epoca_Raleo1',type='string'),
    Field('Año_Raleo1',type='integer'),
    Field('Poda2',type='boolean'),
    Field('Epoca_Poda2',type='string'),
    Field('Año_Poda2',type='integer'),
    Field('Raleo2',type='boolean'),
    Field('Epoca_Raleo2',type='string'),
    Field('Año_Raleo2',type='integer'),
    Field('Poda3',type='boolean'),
    Field('Epoca_poda3',type='string'),
    Field('Año_Poda3',type='integer'),
    Field('Raleo3',type='boolean'),
    Field('Epoca_Raleo3',type='string'),
    Field('Año_Raleo3',type='integer'),
    Field('Laboreo',type='boolean'),
    Field('Herbicida',type='boolean'),
    Field('Otros',type='boolean'),
    Field('Sin_manejo',type='boolean'),
    Field('Res_Cat1',type='double'),
    Field('Res_Cat2',type='double'),
    Field('Res_Cat3',type='double'),
    Field('Res_Cat4',type='double'),
    Field('Res_Cat5',type='double'),
    Field('Res_Fus1',type='double'),
    Field('Res_Fus2',type='double'),
    Field('Res_Fus3',type='double'),
    Field('Res_Fus4',type='double'),
    Field('Res_Fus5',type='double'),
    Field('Mapa',type='upload'),
    Field('Cant_Parcelas',type='integer')
)

db.define_table('Carpetas_BN',
    Field('Codigo',type='integer', unique=True, notnull=True),
    Field('Nro_Carpeta',type='integer'),
    Field('Fecha_pres',type='integer'),
    Field('Cod_Depto',db.Deptos),
    Field('Cod_Sj',type='integer'),
    Field('Latitud',type='double'),
    Field('Longitud',type='double'),
    Field('Tipo_Bosque',type='string'),
    Field('Baja',type='boolean'),
    Field('Notas',type='string')
)

db.define_table('Cambios_Areas',
    Field('Fecha',type='datetime'),
    Field('Nro_Carpeta',db.Carpetas_BN),
    Field('Cod_depto',db.Deptos),
    Field('Cod_Pad',type='integer'),
    Field('Area',type='double')
)

db.define_table('Carpetas_N',
    Field('Codigo',type='integer', unique=True, notnull=True),
    Field('Nro_Carpeta',type='integer'),
    Field('Fecha_Pres',type='integer'),
    Field('Cod_Depto',db.Deptos),
    Field('Cod_Sj',type='integer'),
    Field('Longitud',type='double'),
    Field('Latitud',type='double'),
    Field('Baja',type='boolean'),
    Field('Notas',type='string')
)

db.define_table('Carpetas_P',
    Field('Codigo',type='integer', unique=True, notnull=True),
    Field('Nro_Carpeta',type='integer'),
    Field('Fecha_Pres',type='integer'),
    Field('Cod_Depto',db.Deptos),
    Field('Cod_Sj',type='integer'),
    Field('Longitud',type='double'),
    Field('Latitud',type='double'),
    Field('Baja',type='boolean'),
    Field('Notas',type='string')
)

db.define_table('Coeficientes',
    Field('Creci_Pi_CN_5',type='integer'),
    Field('Creci_Pi_CN_10',type='integer'),
    Field('Creci_Pi_CN_15',type='integer'),
    Field('Creci_Pi_CN_20',type='integer'),
    Field('Creci_Pi_LI_5',type='integer'),
    Field('Creci_Pi_LI_10',type='integer'),
    Field('Creci_Pi_LI_15',type='integer'),
    Field('Creci_Pi_LI_20',type='integer'),
    Field('Creci_Pi_OT_6',type='integer'),
    Field('Creci_Pi_OT_12',type='integer'),
    Field('Creci_Pi_OT_18',type='integer'),
    Field('Creci_Pi_OT_25',type='integer'),
    Field('Creci_Pi_des',type='double'),
    Field('Creci_Eu_CN_Gr',type='integer'),
    Field('Creci_Eu_CN_Gl',type='integer'),
    Field('Creci_Eu_CN_Ot',type='integer'),
    Field('Creci_Eu_LI_Gr',type='integer'),
    Field('Creci_Eu_LI_Gl',type='integer'),
    Field('Creci_Eu_LI_Ot',type='integer'),
    Field('Creci_Eu_SE_Gr',type='integer'),
    Field('Creci_Eu_SE_Gl',type='integer'),
    Field('Creci_Eu_SE_Ot',type='integer'),
    Field('Creci_Pri_Gr',type='double'),
    Field('Creci_Pri_Gl',type='double'),
    Field('Creci_Pri_Ot',type='double'),
    Field('Creci_Seg_Gr',type='double'),
    Field('Creci_Seg_Gl',type='double'),
    Field('Creci_Seg_Ot',type='double'),
    Field('Creci_Eu_des',type='double'),
    Field('Des_Pi_Pu_Pri',type='integer'),
    Field('Des_Pi_Pu_Seg',type='integer'),
    Field('Des_Pi_Pu_Ter',type='integer'),
    Field('Des_Pi_Pu_Fin',type='integer'),
    Field('Des_Pi_As_Pri',type='integer'),
    Field('Des_Pi_As_Seg',type='integer'),
    Field('Des_Pi_As_Ter',type='integer'),
    Field('Des_Pi_As_Fin',type='integer'),
    Field('Des_Eu_Pu_CN_Pri',type='integer'),
    Field('Des_Eu_Pu_CN_Seg',type='integer'),
    Field('Des_Eu_Pu_CN_Ter',type='integer'),
    Field('Des_Eu_Pu_CN_Cua',type='integer'),
    Field('Des_Eu_Pu_CN_Fin',type='integer'),
    Field('Des_Eu_Pu_LI_Pri',type='integer'),
    Field('Des_Eu_Pu_LI_Seg',type='integer'),
    Field('Des_Eu_Pu_LI_Ter',type='integer'),
    Field('Des_Eu_Pu_LI_Fin',type='integer'),
    Field('Des_Eu_Asn_CN_Pri',type='integer'),
    Field('Des_Eu_Asn_CN_Seg',type='integer'),
    Field('Des_Eu_Asn_CN_Ter',type='integer'),
    Field('Des_Eu_Asn_CN_Cua',type='integer'),
    Field('Des_Eu_Asn_CN_Fin',type='integer'),
    Field('Des_Eu_Asn_LI_Pri',type='integer'),
    Field('Des_Eu_Asn_LI_Seg',type='integer'),
    Field('Des_Eu_Asn_LI_Ter',type='integer'),
    Field('Des_Eu_Asn_LI_Fin',type='integer'),
    Field('Des_Eu_Asp_CN_Pri',type='integer'),
    Field('Des_Eu_Asp_CN_Seg',type='integer'),
    Field('Des_Eu_Asp_CN_Ter',type='integer'),
    Field('Des_Eu_Asp_CN_Cua',type='integer'),
    Field('Des_Eu_Asp_CN_Fin',type='integer'),
    Field('Des_Eu_Asp_LI_Pri',type='integer'),
    Field('Des_Eu_Asp_LI_Seg',type='integer'),
    Field('Des_Eu_Asp_LI_Ter',type='integer'),
    Field('Des_Eu_Asp_LI_Fin',type='integer'),
    Field('Pro_Eu_CN_Pri',type='integer'),
    Field('Pro_Eu_CN_Seg',type='integer'),
    Field('Pro_Eu_CN_Ter',type='integer'),
    Field('Pro_Eu_CN_Cua',type='integer'),
    Field('Pro_Eu_CN_Fin',type='integer'),
    Field('Pro_Eu_LI_Pri',type='integer'),
    Field('Pro_Eu_LI_Seg',type='integer'),
    Field('Pro_Eu_LI_Ter',type='integer'),
    Field('Pro_Eu_LI_Fin',type='integer'),
    Field('Por_Eu_CN_As',type='integer'),
    Field('Por_Eu_CN_P',type='integer'),
    Field('Por_Eu_LI_As',type='integer'),
    Field('Por_Eu_LI_P',type='integer'),
    Field('Por_Area_efec',type='integer')
)



db.define_table('Dj_Guias',
    Field('Cod_DJ',type='integer', unique=True, notnull=True),
    Field('Guia',type='integer'),
    Field('Tonelaje',type='integer')
)

db.define_table('dtproperties',
    Field('objectid',type='integer'),
    Field('property',type='string'),
    Field('value',type='string'),
    Field('uvalue',type='string'),
    Field('lvalue',type='upload'),
    Field('version',type='integer')
)

db.define_table('Enfermedades',
    Field('Codigo',type='string', unique=True, notnull=True),
    Field('Especie',type='string'),
    Field('Hospedero',type='string'),
    Field('Organo',type='integer'),
    Field('Imagen1',type='upload'),
    Field('Imagen2',type='upload'),
    Field('Tipo',type='integer')
)

db.define_table('Monitoreos',
    Field('Codigo',type='integer', unique=True, notnull=True),
    Field('Fecha_Inicio',type='datetime'),
    Field('Tipo_Monitoreo',type='string'),
    Field('Estado',type='integer'),
    Field('Usuario',type='string'),
    Field('Area_total',type='double')
)

db.define_table('Otros',
    Field('Codigo',type='string', unique=True, notnull=True),
    Field('Descripcion',type='string'),
    Field('Tipo',type='integer'),
    Field('Tipo_Char',type='string')
)

db.define_table('Parcelas',
    Field('Codigo',type='integer', unique=True, notnull=True),
    Field('Fila',type='integer'),
    Field('Cod_Rodal',db.Rodales),
    Field('Fecha',type='datetime'),
    Field('Ind_Coneat',type='string'),
    Field('Tipo_Suelo',type='integer'),
    Field('Res_Cat1',type='integer'),
    Field('Res_Cat2',type='integer'),
    Field('Res_Cat3',type='integer'),
    Field('Res_Cat4',type='integer'),
    Field('Res_Cat5',type='integer'),
    Field('Res_Fus1',type='integer'),
    Field('Res_Fus2',type='integer'),
    Field('Res_Fus3',type='integer'),
    Field('Res_Fus4',type='integer'),
    Field('Res_Fus5',type='integer'),
    Field('Mes',type='integer'),
    Field('Año',type='integer'),
    Field('Mes_Dia',type='integer'),
    Field('Observaciones',type='string'),
    Field('Area',type='double')
)

db.define_table('Parcelas_Otros',
    Field('Codigo',type='integer', unique=True, notnull=True),
    Field('Cod_Parcela',db.Parcelas),
    Field('Cod_Agente',type='string'),
    Field('GMD',type='double'),
    Field('Por_AA',type='double'),
    Field('Tipo',type='string'),
    Field('Pos',type='integer'),
    Field('GMD_Rnd',type='integer'),
    Field('A1',type='double'),
    Field('A2',type='double'),
    Field('A3',type='double'),
    Field('A4',type='double'),
    Field('A5',type='double'),
    Field('A6',type='double'),
    Field('A7',type='double'),
    Field('A8',type='double'),
    Field('A9',type='double'),
    Field('A10',type='double'),
    Field('A11',type='double'),
    Field('A12',type='double'),
    Field('A13',type='double'),
    Field('A14',type='double'),
    Field('A15',type='double'),
    Field('A16',type='double'),
    Field('A17',type='double'),
    Field('A18',type='double'),
    Field('A19',type='double'),
    Field('A20',type='double'),
    Field('A21',type='double'),
    Field('A22',type='double'),
    Field('A23',type='double'),
    Field('A24',type='double'),
    Field('A25',type='double')
)

db.define_table('Plagas',
    Field('Codigo',type='string', unique=True, notnull=True),
    Field('Insecto',type='string'),
    Field('Familia',type='string'),
    Field('Orden',type='string'),
    Field('Hospedero',type='string'),
    Field('Tipo_de_Daño',type='string'),
    Field('Importancia',type='string'),
    Field('Imagen1',type='upload'),
    Field('Imagen2',type='upload'),
    Field('Tipo',type='integer')
)

db.define_table('Planes',
    Field('Codigo',type='integer', unique=True, notnull=True),
    Field('Codigo_Plan_Pro',type='integer'),
    Field('Fecha_Act',type='datetime'),
    Field('Año_Dec',type='integer'),
    Field('CodG_Dec',type='string'),
    Field('CodE_Dec',type='integer'),
    Field('Epo_Dec',type='string'),
    Field('Ha_Dec',type='double'),
    Field('Den_Dec',type='integer'),
    Field('E1_Dec',type='integer'),
    Field('E2_Dec',type='integer'),
    Field('E3_Dec',type='integer'),
    Field('Cal_Dec',type='string'),
    Field('Met_Dec',type='string'),
    Field('Sem_Dec',type='string'),
    Field('Planta_Dec',type='string'),
    Field('Tipo_Planta_Dec',type='string'),
    Field('Raleo_Dec',type='string'),
    Field('Poda_Dec',type='string'),
    Field('Corta_Dec',type='string'),
    Field('Objetivo_dec',type='string'),
    Field('Proyecto_g_dec',type='string'),
    Field('Observaciones',type='string')
)

db.define_table('Planes_Pro',
    Field('Codigo',type='integer', unique=True, notnull=True),
    Field('Codigo_Cp',type='integer'),
    Field('Fecha_Act',type='datetime'),
    Field('Año_Pro',type='integer'),
    Field('CodG_Pro',type='string'),
    Field('CodE_Pro',type='integer'),
    Field('Epo_Pro',type='string'),
    Field('Ha_Pro',type='double'),
    Field('Den_Pro',type='integer'),
    Field('E1_Pro',type='integer'),
    Field('E2_Pro',type='integer'),
    Field('E3_Pro',type='integer'),
    Field('Cal_Pro',type='string'),
    Field('Met_Pro',type='string'),
    Field('Sem_Pro',type='string'),
    Field('Planta_Pro',type='string'),
    Field('Tipo_Planta_Pro',type='string'),
    Field('Raleo_Pro',type='string'),
    Field('Poda_Pro',type='string'),
    Field('Corta_Pro',type='string'),
    Field('Objetivo_pro',type='string'),
    Field('Proyecto_g_pro',type='string'),
    Field('Observaciones',type='string')
)

db.define_table('Plantas',
    Field('CodG',type='string'),
    Field('CodE',type='integer'),
    Field('Genero',type='string'),
    Field('Especie',type='string'),
    Field('Descripcion',type='string'),
    Field('Apel',type='string'),
    Field('Carac','text'),
    Field('Foto',type='upload'),
    Field('Taxo',type='upload')
)

db.define_table('Propietarios',
    Field('Codigo',type='integer', unique=True, notnull=True),
    Field('Nombre',type='string'),
    Field('Direccion',type='string'),
    Field('Telefono',type='string'),
    Field('Representacion',type='string')
)

db.define_table('Proyecciones',
    Field('Cod_Sj',type='integer'),
    Field('Cod_Depto',db.Deptos),
    Field('Especie',type='integer'),
    Field('Año',type='integer'),
    Field('Valor',type='double')
)

db.define_table('Registro',
    Field('Codigo',type='integer'),
    Field('Codigo_Cp_Pr',type='integer'),
    Field('Codigo_Cp_Bn',type='integer'),
    Field('Cod_Depto',db.Deptos),
    Field('Codigo_Pad',type='integer'),
    Field('Anexo',type='string'),
    Field('Tipo_Bos',type='string'),
    Field('Cant_Bosques',type='integer'),
    Field('Cant_Tipo_Bosque',type='integer'),
    Field('Cant_Tipo_Bosque_Depto',type='integer'),
    Field('Resoluciones',type='string'),
    Field('Codigo_Prop',type='integer'),
    Field('Rep_Prop',type='string'),
    Field('Area',type='double'),
    Field('Tipo_Prop',type='string')
)

db.define_table('Agentes',
    Field('Codigo',type='string', unique=True, notnull=True),
    Field('nombre',type='string'),
    Field('tipo',type='string')
)

db.define_table('Rodales_Otros',
    Field('Codigo',type='integer', unique=True, notnull=True),
    Field('Cod_Rodal',db.Rodales),
    Field('Cod_Agente',db.Agentes),
    Field('Por_AA_Ha',type='double'),
    Field('Tipo',type='string'),
    Field('Pos',type='integer')
)

db.define_table('Seleccion',
    Field('Sesion',type='string'),
    Field('Codigo',type='string'),
    Field('GMD',type='integer')
)

db.define_table('Simbolos_Mon',
    Field('Codigo',type='integer', unique=True, notnull=True),
    Field('Sesion_Id',type='string'),
    Field('Monitoreo',type='integer'),
    Field('Rodal',type='integer'),
    Field('X',type='double'),
    Field('Y',type='double'),
    Field('Simbolo',type='string')
)

db.define_table('MAPINFO_MAPCATALOG',
    Field('SPATIALTYPE','float'),
    Field('TABLENAME',type='string'),
    Field('OWNERNAME',type='string'),
    Field('SPATIALCOLUMN',type='string'),
    Field('DB_X_LL','float'),
    Field('DB_Y_LL','float'),
    Field('DB_X_UR','float'),
    Field('DB_Y_UR','float'),
    Field('COORDINATESYSTEM',type='string'),
    Field('SYMBOL',type='string'),
    Field('XCOLUMNNAME',type='string'),
    Field('YCOLUMNNAME',type='string'),
    Field('RENDITIONTYPE',type='integer'),
    Field('RENDITIONCOLUMN',type='string'),
    Field('RENDITIONTABLE',type='string')
)
"""



"""

Tabla: Access
)

Tabla: Cambios_Areas
)

Tabla: Carpetas_BN
    primaryKey: 'Codigo',
)

Tabla: Carpetas_N
    primaryKey: 'Codigo',
)

Tabla: Carpetas_P
    primaryKey: 'Codigo',
)

Tabla: Coeficientes
)

Tabla: Deptos
    primaryKey: 'Codigo',
)

Tabla: Dj_Guias
    primaryKey: 'Cod_DJ',
    primaryKey: 'Guia',
)

Tabla: dtproperties
    primaryKey: 'id',
    primaryKey: 'property',
)

Tabla: Enfermedades
    primaryKey: 'Codigo',
)

Tabla: Monitoreos
    primaryKey: 'Codigo',
)

Tabla: Otros
    primaryKey: 'Codigo',
)

Tabla: Parcelas
    primaryKey: 'Codigo',
)

Tabla: Parcelas_Otros
)

Tabla: Plagas
    primaryKey: 'Codigo',
)

Tabla: Planes
    primaryKey: 'Codigo',
)

Tabla: Planes_Pro
    primaryKey: 'Codigo',
)

Tabla: Plantas
    primaryKey: 'CodG',
    primaryKey: 'CodE',
)

Tabla: Propietarios
    primaryKey: 'Codigo',
)

Tabla: Proyecciones
    primaryKey: 'Cod_Sj',
    primaryKey: 'Cod_Depto',
    primaryKey: 'Especie',
    primaryKey: 'Año',
)

Tabla: Registro
    primaryKey: 'Codigo',
)

Tabla: Rodales
    primaryKey: 'Codigo',
)

Tabla: Rodales_Otros
)

Tabla: Seleccion
)

Tabla: Simbolos_Mon
    primaryKey: 'Codigo',
)
"""

"""
Estos son los foreign key de las tablas
('DGF', 'dbo', 'Carpetas_BN', 'Nro_Carpeta', 'DGF', 'dbo', 'Cambios_Areas', 'Nro_Carpeta', 1, 1, 1, 'FK_Cambios_Areas_Carpetas_BN', 'IX_Carpetas_BN', 7)
('DGF', 'dbo', 'Carpetas_BN', 'Cod_Depto', 'DGF', 'dbo', 'Cambios_Areas', 'Cod_depto', 2, 1, 1, 'FK_Cambios_Areas_Carpetas_BN', 'IX_Carpetas_BN', 7)
('DGF', 'dbo', 'Carpetas_BN', 'Codigo', 'DGF', 'dbo', 'Plan_Manejo', 'Cod_Carp_BN', 1, 1, 1, 'FK_Plan_Manejo_Carpetas_BN', 'PK_Carpetas_BN', 7)
('DGF', 'dbo', 'Carpetas_N', 'Nro_Carpeta', 'DGF', 'dbo', 'Planes_N', 'Codigo_Cp', 1, 1, 1, 'FK_Planes_N_Carpetas_N', 'IX_Carpetas_N', 7)
('DGF', 'dbo', 'Carpetas_P', 'Nro_Carpeta', 'DGF', 'dbo', 'Planes_Pro', 'Codigo_Cp', 1, 1, 1, 'FK_Planes_Pro_Carpetas_P', 'IX_Carpetas_P', 7)
('DGF', 'dbo', 'Deptos', 'Codigo', 'DGF', 'dbo', 'Parcelas_inf', 'cod_depto', 1, 1, 1, 'FK_Parcelas_inf_Deptos', 'PK_Deptos', 7)
('DGF', 'dbo', 'Deptos', 'Codigo', 'DGF', 'dbo', 'Parcelas_Inf_Pro', 'cod_depto', 1, 1, 1, 'FK_Parcelas_inf_pro_Deptos', 'PK_Deptos', 7)
('DGF', 'dbo', 'Deptos', 'Codigo', 'DGF', 'dbo', 'Rodales', 'Cod_depto', 1, 1, 1, 'FK_Rodales_Deptos', 'PK_Deptos', 7)
('DGF', 'dbo', 'Monitoreos', 'Codigo', 'DGF', 'dbo', 'Rodales', 'Cod_Mon', 1, 1, 1, 'FK_Rodales_Monitoreos', 'PK_Monitoreos', 7)
('DGF', 'dbo', 'Planes', 'Codigo', 'DGF', 'dbo', 'Estados', 'Codigo_Pl', 1, 1, 1, 'FK_Estados_Planes', 'PK_Planes', 7)
('DGF', 'dbo', 'Planes_Pro', 'Codigo', 'DGF', 'dbo', 'Planes', 'Codigo_Plan_Pro', 1, 1, 1, 'FK_Planes_Planes_Pro', 'PK_Planes_Pro', 7)
('DGF', 'dbo', 'Plantas', 'CodG', 'DGF', 'dbo', 'Parcelas_inf', 'codg', 1, 1, 1, 'FK_Parcelas_inf_Plantas', 'PK_Plantas', 7)
('DGF', 'dbo', 'Plantas', 'CodE', 'DGF', 'dbo', 'Parcelas_inf', 'code', 2, 1, 1, 'FK_Parcelas_inf_Plantas', 'PK_Plantas', 7)
('DGF', 'dbo', 'Plantas', 'CodG', 'DGF', 'dbo', 'Parcelas_Inf_Pro', 'codg', 1, 1, 1, 'FK_Parcelas_inf_pro_Plantas', 'PK_Plantas', 7)
('DGF', 'dbo', 'Plantas', 'CodE', 'DGF', 'dbo', 'Parcelas_Inf_Pro', 'code', 2, 1, 1, 'FK_Parcelas_inf_pro_Plantas', 'PK_Plantas', 7)
('DGF', 'dbo', 'Plantas', 'CodG', 'DGF', 'dbo', 'Rodales', 'Codg', 1, 1, 1, 'FK_Rodales_Plantas', 'PK_Plantas', 7)
('DGF', 'dbo', 'Plantas', 'CodE', 'DGF', 'dbo', 'Rodales', 'Code', 2, 1, 1, 'FK_Rodales_Plantas', 'PK_Plantas', 7)
('DGF', 'dbo', 'Propietarios', 'Codigo', 'DGF', 'dbo', 'Registro', 'Codigo_Prop', 1, 1, 1, 'FK_Registro_Propietarios', 'PK_Propietarios', 7)
('DGF', 'dbo', 'Propietarios', 'Codigo', 'DGF', 'dbo', 'Usuarios_Emp', 'Propietario', 1, 1, 1, 'FK_Usuarios_Emp_Propietarios', 'PK_Propietarios', 7)
('DGF', 'dbo', 'Registro', 'Codigo', 'DGF', 'dbo', 'Certificados', 'Cod_Reg', 1, 1, 1, 'FK_Certificados_Registro1', 'PK_Registro', 7)
('DGF', 'dbo', 'Rodales', 'Codigo', 'DGF', 'dbo', 'Parcelas', 'Cod_Rodal', 1, 1, 1, 'FK_Parcelas_Rodales', 'PK_Rodales', 7)
('DGF', 'dbo', 'Rodales', 'Codigo', 'DGF', 'dbo', 'Rodales_Otros', 'Cod_Rodal', 1, 1, 0, 'FK_Rodales_Otros_Rodales', 'PK_Rodales', 7)

"""

