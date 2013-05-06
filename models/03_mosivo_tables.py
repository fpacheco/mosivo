"""
Mirror tables from DGF database
"""
db.define_table("departamento",
    Field("codigo",type="string",length=1,unique=True,notnull=True),
    Field("nombre",type="string",unique=True,notnull=True),
    Field("numero",type="integer",unique=True,notnull=True)
)

db.define_table("genero",
    Field("nombre",type="string",length=50,unique=True,notnull=True),
    Field("codigo",type="string",length=1,unique=True,notnull=True)
)

db.define_table("especie",
    Field("genero",db.genero),
    Field("nombre",type="string",length=50,unique=True,notnull=True),
    Field("codigo",type="string",length=1,unique=True,notnull=True)
)

db.define_table("destino",
    Field("destino",type="string",length=50,unique=True,notnull=True)
)

##### Datos de la base de datos DGF
db.define_table("bosqueplantado",
    # El numero de la carpeta
    Field('numero_carpeta',type='integer',unique=True,notnull=True),
    # El año de presentacion
    Field('fecha_presentacion',type='integer'),
    Field('departamento',db.departamento),    
    Field('sec_judicial',type='integer'),
    # Longitud en grados
    Field('lon',type='double'),
    # Latitud en grados
    Field('lat',type='double'),
    # No cuenta
    Field('baja',type='boolean'),
)

db.define_table("bpdeclarado",
    Field('bosqueplantado',db.bosqueplantado),
    Field('especie',db.especie),
    Field('anio_plantado',type='integer'),
    Field('area_afectada',type='float'),
)

##### Otros aspectos de la configuración
## Actualización de datos (desde DGF a base del modelo)
db.define_table("dia",
    Field('nombre',type='string',length=15,notnull=True,unique=True)
)

db.define_table("adatos",
    Field('dia',db.dia),
    Field('hora',type='time')
)

## Actualización de la modelación
db.define_table("amodelo",
    Field('dia',db.dia),
    Field('hora',type='time')
)

##### Coeficiente para estimar datos faltantes
## Coeficientes para corta o turno (ejemplo: eucalyptus globulus, aserrio = 20 anos)
db.define_table("cturno",
    Field("especie",db.especie),
    Field("destino",db.destino),
    Field("turno",type="float",notnull=True)
)
# Una especie con un destino = 1 solo valor de corta
db.cturno.turno.requires=IS_NOT_IN_DB(
    db((db.cturno.especie==request.vars.especie) & (db.cturno.destino==request.vars.destino)), 'cturno.turno')

## Cuanto crece por ano (ima=indice medio anual)
db.define_table("cima",
    Field("especie",db.especie),
    Field("departamento",db.departamento),
    Field("ima",type="float",notnull=True,label=u"Indice de crecimiento medio anual (m3/ha/año)")
)
# Una especie con un destino = 1 solo valor de corta
db.cima.ima.requires=IS_NOT_IN_DB(
    db((db.cima.especie==request.vars.especie) & (db.cima.departamento==request.vars.departamento)), 'cima.ima')

## Que porcentaje del bosque es area efectiva de plantacion
db.define_table("caefectiva",
    Field("especie",db.especie),
    Field("departamento",db.departamento),
    Field("aefectiva",type="float",notnull=True)
)
# Una especie con un destino = 1 solo valor de corta
db.caefectiva.aefectiva.requires=IS_NOT_IN_DB(
    db((db.caefectiva.especie==request.vars.especie) & (db.caefectiva.departamento==request.vars.departamento)), 
    'caefectiva.aefectiva')

## Que fraccion del destino tienen los bosques en teoría vale solo para grandis
db.define_table("cfdestino",
    Field("especie",db.especie),
    Field("departamento",db.departamento),
    Field("destino",db.destino),
    Field("fdestino",type="float",notnull=True)
)

# Una especie con un departamento y un destino = 1 solo valor de fraccion de destino
db.cfdestino.fdestino.requires=IS_NOT_IN_DB(
    db(
        (db.cfdestino.especie==request.vars.especie) & 
        (db.cfdestino.departamento==request.vars.departamento) & 
        (db.cfdestino.destino==request.vars.destino)
        ), 
    'cfdestino.fdestino')

# La suma de destinos para una misma especie en un mismo depto = 1
# ??????

## Una especie, en un departamento y con un destino se ralea a los tantos años (por ejemplo a los 7, 13 y 15 años)
db.define_table("caraleo",
    Field("especie",db.especie),
    Field("departamento",db.departamento),
    Field("destino",db.destino),
    Field("araleo",type="float",notnull=True),
    Field("vraleo",type="float",notnull=True),
)

# Cada raleo puede tener una fracion de cada destino (el primer raleo va a pulpa, el seguno 60% a pulpa y 30% a aserrio y así en delante)
db.define_table("cfdraleo",
    Field("caraleo",db.caraleo),
    Field("fdraleo",type="float",notnull=True)
)

# Grupo del suelo (cada tipo de suelo pertenece a un grupo de suelo)
db.define_table("gruposuelo",
    Field("nombre",type='string',notnull=True,unique=True),
    Field("codigo",type='string',notnull=True,unique=True),
    Field("descripcion",type='text')
)

# Tipo de suelo
db.define_table("suelo",
    Field("nombre",type='string',notnull=True,unique=True),
    Field("gruposuelo",db.gruposuelo),
    Field("codigo",type='string',notnull=True,unique=True),
    Field("descripcion",type='text')
)

db.define_table("cosecha",
    Field("nombre",type='string',notnull=True,unique=True),
    Field("descripcion",type='text')
)

db.define_table("cbcampo",
    Field("especie",db.especie),
    Field("suelo",db.suelo),
    Field("destino",db.destino),
    Field("cosecha",db.cosecha),
    Field("bcampo",type="float",notnull=True)
)

db.define_table("cbindustria",
    Field("especie",db.especie),
    Field("bindustria",type="float",notnull=True)
)
