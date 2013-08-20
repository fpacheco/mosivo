# -*- coding: utf-8 -*-
"""
Mirror tables from DGF database
"""
if 0:
    from static import *


def integer_input_HTML5_widget(field, value):
    return INPUT(_name=field.name,
                 _id="%s_%s" % (field._tablename, field.name),
                 _class=field.type,
                 _value=value,
                 requires=field.requires,
                 _type="number",
                 _min=field.requires.minimum,
                 _max=field.requires.maximum,
                 _onkyup="this.value = this.value.replace(/[^0-9]/g,'');"
                 )

def float_input_HTML5_widget(field, value):
    return INPUT(_name=field.name,
                 _id="%s_%s" % (field._tablename, field.name),
                 _class=field.type,
                 _value=value,
                 requires=field.requires,
                 _type="number",
                 _min=field.requires.minimum,
                 _max=field.requires.maximum,
                 _onkeyup="this.value = this.value.replace(/[^0-9\.]/g,'');"
                 )


### RFPV: Borrar
# from model import *

# Departamentos de UY
db.define_table("departamento",
    Field("nombre", type="string", length=25, unique=True, notnull=True),
    format='%(nombre)s'
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
    Field("codigo", type="string", length=1,notnull=True),
    format='%(nombre)s'
)
# Nombre and codigo uniques
db.genero.codigo.requires=IS_NOT_IN_DB(
    db((db.genero.nombre==request.vars.nombre)), 'genero.codigo'
)

# Especies para cada genero
db.define_table("especie",
    Field("genero", db.genero, label=T(u"Género de la especie"),
      required=True, requires=IS_IN_DB(db, 'genero.id', '%(nombre)s'),
      represent=lambda id, r: db.genero(id).nombre
    ),
    Field("nombre", type="string", length=50, notnull=True, label=T("Nombre de la especie")),
    Field("codigo", type="integer", notnull=True, label=T("Código de la especie")),
    format='%(nombre)s'
)
# Genero and codigo uniques
db.especie.codigo.requires=IS_NOT_IN_DB(
    db((db.especie.genero==request.vars.genero)), 'especie.codigo'
)


# Grupo del suelo (cada tipo de suelo pertenece a un grupo de suelo)
db.define_table("gruposuelo",
    Field("nombre", type='string', length= 10, notnull=True, unique=True, label=T("Código del grupo suelo")),
    Field("descripcion", type='text', label=T("Descripción del grupo suelo")),
    format='%(nombre)s'
)

"""
# Tipo de suelo
db.define_table("gruposuelo",
    Field("nombre", type='string', notnull=True, unique=True, label=T("Nombre del suelo")),
    Field("gruposuelo", db.gruposuelo),
    Field("codigo", type='string', notnull=True, unique=True, label=T("Código de suelo")),
    Field("descripcion", type='text', label=T("Descripción del suelo"))
)
# gruposuelo and codigo uniques
db.gruposuelo.codigo.requires=IS_NOT_IN_DB(
    db((db.gruposuelo.gruposuelo == request.vars.gruposuelo)), 'suelo.codigo'
)
"""

from cascadingselect import CascadingSelect
cSelEsp = CascadingSelect(db.genero,db.especie)
cSelEsp.prompt = lambda table: T("Select %s") % str(table).capitalize()

# Destinos de los rodales
db.define_table("destino",
    Field("nombre", type="string", length=50, unique=True, notnull=True, label=T("Destino")),
    format='%(nombre)s'
)

# Tipo de cosechas
db.define_table("cosecha",
    Field("nombre", type='string', notnull=True,unique=True),
    Field("descripcion", type='text'),
    format='%(nombre)s'
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
    Field('destino', db.destino, notnull=False),
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
db.define_table("gruposuelorodald",
    Field('rodal', db.rodald),
    # Seccion judicial para ese departamento
    Field('gruposuelo', db.gruposuelo),
    # Superficie
    Field('superficie', type='double')
)
# rodal and suelo uniques
db.gruposuelorodald.gruposuelo.requires=IS_NOT_IN_DB(
    db((db.gruposuelorodald.rodal == request.vars.rodal)), 'gruposuelorodald.gruposuelo'
)

# Turnos de cortes para montes declarados
db.define_table("turnorodald",
    Field('rodal', db.rodald),
    # tiempo en anios desde que se planta
    Field('turno', type='float', label=u'Corte (años)'),
    # volumen de corta en m3/ha
    Field('volumen', type='float', label=u'Volumen(m3/Ha)'),
)

# Turnos de raleo para montes declarados
db.define_table("raleorodald",
    Field('rodal', db.rodald),
    # tiempo en anios desde que se planta
    Field('turno', type='float', label=u'Raleo(años)'),
    # Destino del raleo
    Field('destino', db.destino, notnull=False),
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
    Field('destino', db.destino, notnull=False),
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
db.define_table("gruposuelorodalp",
    Field('rodal', db.rodalp),
    # Seccion judicial para ese departamento
    Field('gruposuelo', db.gruposuelo),
    # Superficie
    Field('superficie', type='double')
)
# rodal and suelo uniques
db.gruposuelorodalp.gruposuelo.requires = IS_NOT_IN_DB(
    db((db.gruposuelorodalp.rodal == request.vars.rodal)), 'gruposuelorodalp.gruposuelo'
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
    # Destino del raleo
    Field('destino', db.destino, notnull=False),
    # volumen de raleo en m3/ha
    Field('volumen', type='float'),
)

##### Otros aspectos de la configuración
## Actualización de datos (desde BD remota a la base del modelo)
# Dias de la semana
db.define_table("dia",
    Field('nombre', type='string', length=15, notnull=True, unique=True),
    format='%(nombre)s'
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
    Field("especie", db.especie, label=T("Especie plantada"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("destino", db.destino, label=T("Destino del rodal"),
        required=True, requires=IS_IN_DB(db, 'destino.id', '%(nombre)s'),
        represent=lambda id, r: db.destino(id).nombre
    ),
    Field("turno", type="float", notnull=True, label=T(u"Años hasta el corte"), widget=float_input_HTML5_widget)
)
# Una especie con un destino = 1 solo valor de corta
db.cturno.turno.requires = IS_NOT_IN_DB(
    db((db.cturno.especie == request.vars.especie) & (db.cturno.destino==request.vars.destino)), 'cturno.turno')
db.cturno.turno.requires = IS_FLOAT_IN_RANGE(0.0, 50.0, dot='.', error_message=T('Too small o to large'))

db.cturno.especie.widget=cSelEsp.widget  

## Cuanto crece por ano (ima=indice medio anual)
db.define_table("cima",
    Field("especie", db.especie, label=T("Especie plantada"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("departamento", db.departamento,
      required=True, requires=IS_IN_DB(db, 'departamento.id', '%(nombre)s'),
      represent=lambda id, r: db.departamento(id).nombre
    ),
    Field("ima", type="float", notnull=True, label=T(u"IMA (m3/ha/año)"))
)
# Una especie con un destino = 1 solo valor de corta
db.cima.ima.requires=IS_NOT_IN_DB(
    db((db.cima.especie == request.vars.especie) & (db.cima.departamento == request.vars.departamento)),
    'cima.ima'
)
db.cima.ima.requires = IS_FLOAT_IN_RANGE(0, 50, dot='.', error_message=T('Too small or to large'))
db.cima.especie.widget=cSelEsp.widget


## Que porcentaje del bosque es area efectiva de plantacion
db.define_table("caefectiva",
    Field("especie", db.especie, label=T("Especie plantada"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("departamento", db.departamento,
      required=True, requires=IS_IN_DB(db, 'departamento.id', '%(nombre)s'),
      represent=lambda id, r: db.departamento(id).nombre
    ),
    Field("aefectiva", type="float", notnull=True, label=T("Área efectiva (Ha)"))
)
# Una especie con un destino = 1 solo valor de corta
db.caefectiva.aefectiva.requires = IS_NOT_IN_DB(
    db((db.caefectiva.especie == request.vars.especie) & (db.caefectiva.departamento == request.vars.departamento)),
    'caefectiva.aefectiva'
)
db.caefectiva.aefectiva.requires = IS_FLOAT_IN_RANGE(0, 1000000, dot='.', error_message=T('Too small or to large'))

db.caefectiva.especie.widget=cSelEsp.widget


## Que fraccion del destino tienen los bosques en teoría vale solo para grandis
db.define_table("cfdestino",
    Field("especie", db.especie, label=T("Especie plantada"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("departamento", db.departamento,
      required=True, requires=IS_IN_DB(db, 'departamento.id', '%(nombre)s'),
      represent=lambda id, r: db.departamento(id).nombre
    ),
    Field("destino", db.destino, label=T("Destino del rodal"),
        required=True, requires=IS_IN_DB(db, 'destino.id', '%(nombre)s'),
        represent=lambda id, r: db.destino(id).nombre
    ),
    Field("fdestino", type="float", notnull=True, label=T(u"Fracción de destino"))
)
# Una especie con un departamento y un destino = 1 solo valor de fraccion de destino
db.cfdestino.fdestino.requires=IS_NOT_IN_DB(
    db(
        (db.cfdestino.especie == request.vars.especie) &
        (db.cfdestino.departamento == request.vars.departamento) &
        (db.cfdestino.destino == request.vars.destino)
    ),
    'cfdestino.fdestino'
)
db.cfdestino.fdestino.requires = IS_FLOAT_IN_RANGE(0, 1, dot='.', error_message=T('Too small or to large'))


# La suma de destinos para una misma especie en un mismo depto = 1
# ??????

## Una especie, en un departamento y con un destino se ralea a los tantos años (por ejemplo a los 7, 13 y 15 años)
db.define_table("caraleo",
    Field("especie", db.especie, label=T("Especie plantada"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("departamento", db.departamento,
      required=True, requires=IS_IN_DB(db, 'departamento.id', '%(nombre)s'),
      represent=lambda id, r: db.departamento(id).nombre
    ),
    Field("destino", db.destino, label=T("Destino del rodal"),
        required=True, requires=IS_IN_DB(db, 'destino.id', '%(nombre)s'),
        represent=lambda id, r: db.destino(id).nombre
    ),
    Field("araleo", type="float", notnull=True, label=T(u"Años hasta el raleo")),
    Field("vraleo", type="float", notnull=True, label=T("Volumen de madera (m3/ha")),
)

# Cada raleo puede tener una fracion de cada destino (el primer raleo va a pulpa, el seguno 60% a pulpa y 30% a aserrio y así en delante)
db.define_table("cfdraleo",
    Field("caraleo", db.caraleo),
    Field("fdraleo", type="float", notnull=True)
)

# Coeficientes de campo
db.define_table("cbcampo",
    Field("especie", db.especie, label=T("Especie plantada"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("gruposuelo", db.gruposuelo, label=T("Grupo de suelo"),
        required=True, requires=IS_IN_DB(db, 'gruposuelo.id', '%(nombre)s'),
        represent=lambda id, r: db.gruposuelo(id).nombre
    ),
    Field("destino", db.destino, label=T("Destino del rodal"),
        required=True, requires=IS_IN_DB(db, 'destino.id', '%(nombre)s'),
        represent=lambda id, r: db.destino(id).nombre
    ),
    Field("cosecha", db.cosecha, label=T("Tipo de cosecha"),
        required=True, requires=IS_IN_DB(db, 'cosecha.id', '%(nombre)s'),
        represent=lambda id, r: db.cosecha(id).nombre
    ),
    Field("bcampo", type="float", notnull=True)
)
# No puede haber dos valores para especie, suelo, destino, cosecha
db.cbcampo.bcampo.requires=IS_NOT_IN_DB(
    db(
        (db.cbcampo.especie == request.vars.especie) &
        (db.cbcampo.gruposuelo == request.vars.gruposuelo) &
        (db.cbcampo.destino == request.vars.destino) &
        (db.cbcampo.cosecha == request.vars.cosecha)
    ),
    'cbcampo.bcampo'
)

# Coeficiente general en la industria
db.define_table("cbindustria",
    Field("especie", db.especie, label=T("Especie plantada"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("bindustria", type="float", notnull=True)
)
# No puede haber dos valores para una misma especie
db.cbindustria.bindustria.requires=IS_NOT_IN_DB(
    db(
        (db.cbcampo.especie == request.vars.especie)
    ),
    'cbindustria.bindustria'
)


## Almacenamiento de los resultados del modelo en el escenario B
# Anio de corte
# db.define_table("anio",
#     Field("anio", type='integer', notnull=True, unique=True),
# )
# # Volumen de corte por anio y rodal (declarado)
# db.define_table("corted",
#     Field("anio", db.anio),
#     Field("rodald", db.rodald),
#     Field("volumen", type="float", notnull=True)
# )
# # Volumen de raleo por anio y rodal (declarado) 
# db.define_table("raleod",
#     Field("anio", db.anio),
#     Field("rodald", db.rodald),
#     Field("volumen", type="float", notnull=True)
# )

## Lo proyectado no se modela en el escenario B
# # Volumen de corte por anio y rodal (proyectado) 
# db.define_table("cortep",
#     Field("anio", db.anio),
#     Field("rodald", db.rodald),
#     Field("volumen", type="float", notnull=True)
# )
# # Volumen de raleo por anio y rodal (proyectado) 
# db.define_table("raleop",
#     Field("anio", db.anio),
#     Field("rodald", db.rodald),
#     Field("volumen", type="float", notnull=True)
# )

