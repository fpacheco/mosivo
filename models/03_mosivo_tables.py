# -*- coding: utf-8 -*-
"""
Mirror tables from DGF database
"""
### RFPV: Borrar
# from model import *

# Departamentos de UY
db.define_table("departamento", 
    Field("nombre", type="string", length=25, unique=True, notnull=True),
)

# Seccion judicial por departamento
db.define_table("seccionjudicial",
    Field("departamento", db.departamento),
    Field("seccion", type="integer", notnull=True),
)
# seccion and departamento must be uniques
db.seccionjudicial.seccion.requires=IS_NOT_IN_DB(
    db((db.seccionjudicial.departamento == request.vars.departamento)), 'seccionjudicial.seccion'
)

# Generos de arboles
db.define_table("genero",
    Field("nombre", type="string", length=50, unique=True, notnull=True),
    # Field("codigo", type="string", length=1,notnull=True)
)
# Nombre and codigo uniques
# db.genero.codigo.requires=IS_NOT_IN_DB(
#     db((db.genero.nombre==request.vars.nombre)), 'genero.codigo'
# )

# Especies para cada genero
db.define_table("especie",
    Field("genero", db.genero),
    Field("nombre", type="string", length=50, notnull=True),
    # Field("codigo", type="integer", notnull=True)
)
# Genero and codigo uniques
# db.especie.codigo.requires=IS_NOT_IN_DB(
#     db((db.especie.genero==request.vars.genero)), 'especie.codigo'
# )

# Grupo del suelo (cada tipo de suelo pertenece a un grupo de suelo)
db.define_table("gruposuelo",
    Field("nombre", type='string', notnull=True, unique=True),
    Field("codigo", type='string', notnull=True, unique=True),
    Field("descripcion", type='text')
)

# Tipo de suelo
db.define_table("tiposuelo",
    Field("nombre", type='string', notnull=True, unique=True),
    Field("gruposuelo", db.gruposuelo),
    Field("codigo", type='string', notnull=True, unique=True),
    Field("descripcion", type='text')
)
# gruposuelo and codigo uniques
db.tiposuelo.codigo.requires=IS_NOT_IN_DB(
    db((db.tiposuelo.gruposuelo == request.vars.gruposuelo)), 'suelo.codigo'
)

# Destinos de los rodales
db.define_table("destino", 
    Field("nombre", type="string", length=50, unique=True, notnull=True)
)

# Planes presentados a al DGF 
db.define_table("plan", 
    # El numero del Plan de manejo
    Field('numerocarpeta', type='integer', unique=True, notnull=True),
    # Seccion judicial para ese departamento    
    Field('seccionjudicial', db.seccionjudicial),
    # Longitud en grados decimales
    Field('lon', type='double'),
    # Latitud en grados decimales
    Field('lat', type='double'),
)

# Montes declarados
db.define_table("rodald", 
    # Referencia al plan 
    Field('plan', db.plan),
    # referencia a la especie
    Field('especie', db.especie),
    # Anio en que se planto el monte
    Field('anioplantacion', type='integer'),
    # Area afectada por el monte
    Field('areaafectacion', type='float'),
    # Destino principal del bosque
    Field('destino', db.destino,notnull=False),
)

# Ubicacion montes declarados
db.define_table("ubicacionrodald", 
    Field('rodal', db.rodald),
    # Seccion judicial para ese departamento    
    Field('seccionjudicial', db.seccionjudicial),
    # Longitud en grados decimales
    Field('lon', type='double'),
    # Latitud en grados decimales
    Field('lat', type='double'),
)

# Tipo suelo montes declarados
db.define_table("tiposuelorodald", 
    Field('rodal', db.rodald),
    # Seccion judicial para ese departamento    
    Field('tiposuelo', db.tiposuelo),
    # Superficie
    Field('superficie', type='double')
)
# rodal and suelo uniques
db.tiposuelorodald.tiposuelo.requires=IS_NOT_IN_DB(
    db((db.tiposuelorodald.rodal==request.vars.rodal)), 'tiposuelorodald.tiposuelo'
)

# Turnos de cortes para montes declarados
db.define_table("turnorodald", 
    Field('rodal', db.rodald),
    # tiempo en anios desde que se planta
    Field('turno', type='float', label=u'Raleo(años)'),
    # volumen de corta en m3/ha
    Field('volumen', type='float', label=u'Volumen(m3/Ha)'),
)

# Turnos de raleo para montes declarados
db.define_table("raleorodald", 
    Field('rodal', db.rodald),
    # tiempo en anios desde que se planta
    Field('turno', type='float', label=u'Raleo(años)'),
    # volumen de raleo en m3/ha
    Field('volumen', type='float', label=u'Volumen(m3/Ha)'),
)

# Montes proyectados
db.define_table("rodalp",
    # Referencia a la carpeta
    Field('plan', db.plan),
    # referencia a la especie
    Field('especie', db.especie),
    # Anio en que se planto el monte
    Field('anioplantacion', type='integer'),
    # Area afectada por el monte
    Field('areaafectacion', type='float'),
    # Destino principal del bosque
    Field('destino', db.destino,notnull=False),
)

# Ubicacion montes proyectados
db.define_table("ubicacionrodalp",
    Field('rodal', db.rodalp),
    # Seccion judicial para ese departamento    
    Field('seccionjudicial', db.seccionjudicial),
    # Longitud en grados decimales
    Field('lon', type='double'),
    # Latitud en grados decimales
    Field('lat', type='double'),
)

# Tipo suelo montes proyectados
db.define_table("tiposuelorodalp",
    Field('rodal', db.rodalp),
    # Seccion judicial para ese departamento
    Field('tiposuelo', db.tiposuelo),
    # Superficie
    Field('superficie', type='double')
)
# rodal and suelo uniques
db.tiposuelorodalp.tiposuelo.requires = IS_NOT_IN_DB(
    db((db.tiposuelorodalp.rodal == request.vars.rodal)), 'tiposuelorodalp.tiposuelo'
)

# Turnos de cortes para montes proyectados
db.define_table("turnorodalp",
    Field('rodal', db.rodalp),
    # tiempo en anios desde que se planta
    Field('turno', type='float'),
    # volumen de corta en m3/ha
    Field('volumen', type='float'),
)

# Turnos de raleo para montes proyectados
db.define_table("raleorodalp",
    Field('rodal', db.rodalp),
    # tiempo en anios desde que se planta
    Field('turno', type='float'),
    # volumen de raleo en m3/ha
    Field('volumen', type='float'),
)

##### Otros aspectos de la configuración
## Actualización de datos (desde BD remota a la base del modelo)
# Dias de la semana
db.define_table("dia",
    Field('nombre', type='string', length=15, notnull=True, unique=True)
)

# Dias y hora que actualiza los datos
db.define_table("actualizadato",
    Field('dia', db.dia),
    Field('hora', type='time')
)
# Dias y hora que actualiza el modelo
db.define_table("actualizamodelo", 
    Field('dia', db.dia),
    Field('hora', type='time')
)

##### Coeficiente para estimar datos faltantes
## Coeficientes para corta o turno (ejemplo: eucalyptus globulus, aserrio = 20 anos)
db.define_table("cturno", 
    Field("especie", db.especie),
    Field("destino", db.destino),
    Field("turno", type="float", notnull=True)
)
# Una especie con un destino = 1 solo valor de corta
db.cturno.turno.requires=IS_NOT_IN_DB(
    db((db.cturno.especie==request.vars.especie) & (db.cturno.destino==request.vars.destino)), 'cturno.turno')

## Cuanto crece por ano (ima=indice medio anual)
db.define_table("cima", 
    Field("especie", db.especie),
    Field("departamento", db.departamento),
    Field("ima", type="float", notnull=True, label=u"Indice de crecimiento medio anual (m3/ha/año)")
)
# Una especie con un destino = 1 solo valor de corta
db.cima.ima.requires=IS_NOT_IN_DB(
    db((db.cima.especie == request.vars.especie) & (db.cima.departamento == request.vars.departamento)), 'cima.ima')

## Que porcentaje del bosque es area efectiva de plantacion
db.define_table("caefectiva",
    Field("especie", db.especie),
    Field("departamento", db.departamento),
    Field("aefectiva", type="float", notnull=True)
)
# Una especie con un destino = 1 solo valor de corta
db.caefectiva.aefectiva.requires = IS_NOT_IN_DB(
    db((db.caefectiva.especie == request.vars.especie) & (db.caefectiva.departamento==request.vars.departamento)), 
    'caefectiva.aefectiva')

## Que fraccion del destino tienen los bosques en teoría vale solo para grandis
db.define_table("cfdestino", 
    Field("especie", db.especie),
    Field("departamento", db.departamento),
    Field("destino", db.destino),
    Field("fdestino", type="float", notnull=True)
)

# Una especie con un departamento y un destino = 1 solo valor de fraccion de destino
db.cfdestino.fdestino.requires=IS_NOT_IN_DB(
    db(
        (db.cfdestino.especie == request.vars.especie) & 
        (db.cfdestino.departamento == request.vars.departamento) & 
        (db.cfdestino.destino == request.vars.destino)
        ), 
    'cfdestino.fdestino')

# La suma de destinos para una misma especie en un mismo depto = 1
# ??????

## Una especie, en un departamento y con un destino se ralea a los tantos años (por ejemplo a los 7, 13 y 15 años)
db.define_table("caraleo", 
    Field("especie", db.especie),
    Field("departamento", db.departamento),
    Field("destino", db.destino),
    Field("araleo", type="float", notnull=True),
    Field("vraleo", type="float", notnull=True),
)

# Cada raleo puede tener una fracion de cada destino (el primer raleo va a pulpa, el seguno 60% a pulpa y 30% a aserrio y así en delante)
db.define_table("cfdraleo", 
    Field("caraleo", db.caraleo),
    Field("fdraleo", type="float", notnull=True)
)

# Tipo de cosechas 
db.define_table("cosecha", 
    Field("nombre", type='string', notnull=True,unique=True),
    Field("descripcion", type='text')
)

# Coeficientes de campo
db.define_table("cbcampo", 
    Field("especie", db.especie),
    Field("suelo", db.tiposuelo),
    Field("destino", db.destino),
    Field("cosecha", db.cosecha),
    Field("bcampo", type="float", notnull=True)
)

# Coeficiente general en la industria
db.define_table("cbindustria", 
    Field("especie", db.especie),
    Field("bindustria", type="float", notnull=True)
)
