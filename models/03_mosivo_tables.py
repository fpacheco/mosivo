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


# Departamentos de UY. Generales, unicos y estaticos
db.define_table("departamento",
    Field("nombre", type="string", length=25, unique=True, notnull=True, label=T("Departamento")),
    format='%(nombre)s'
)


# Seccion judicial por departamento. Un conjunto para cada usuario y puede quedar SJ excluidas de la modelacion
db.define_table("seccionjudicial",
    Field("departamento", db.departamento),
    Field("nombre", type="integer", notnull=True, label=T('Sección judicial')),
    # Excluido de la modelacion?
    Field('exc', type='boolean', notnull=True, default=False, label=T('Excluída')),
    # Creado por ...
    Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# seccion and departamento must be uniques
db.seccionjudicial.nombre.requires=IS_NOT_IN_DB(
    db(
        (db.seccionjudicial.departamento == request.vars.departamento) &
        (db.seccionjudicial.cby == request.vars.cby)
    ),
    'seccionjudicial.nombre'
)
# Filtro comun para todas las consultas
db.seccionjudicial._common_filter = lambda query: (db.seccionjudicial.cby == auth.user_id) & (db.seccionjudicial.exc == False)


# Generos de arboles
db.define_table("genero",
    Field("nombre", type="string", length=50, notnull=True, label=T("Género")),
    Field("codigo", type="string", length=1, notnull=True, label=T("Código del género")),
    # Creado por ...
    Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
    format='%(nombre)s'
)
# Nombre and codigo uniques
db.genero.codigo.requires=IS_NOT_IN_DB(
    db(
        (db.genero.nombre==request.vars.nombre) &
        (db.genero.cby==request.vars.cby)
    ),
    'genero.codigo'
)
# Filtro comun para todas las consultas
db.genero._common_filter = lambda query: db.genero.cby == auth.user_id


# Especies para cada genero. Conjunto para cada usuario y pueden quedar excluidas de la modelacion
db.define_table("especie",
    Field("genero", db.genero, label=T(u"Género"),
      required=True, requires=IS_IN_DB(db, 'genero.id', '%(nombre)s'),
      represent=lambda id, r: db.genero(id).nombre
    ),
    Field("nombre", type="string", length=50, notnull=True, label=T("Especie")),
    Field("codigo", type="integer", notnull=True, label=T("Código de la especie")),
    # Excluido de la modelacion?
    Field('exc', type='boolean', notnull=True, default=False, label=T('Excluída')),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
    format='%(nombre)s'
)
# Genero y codigo son unicos
db.especie.codigo.requires=IS_NOT_IN_DB(
    db(
        (db.especie.genero==request.vars.genero)
    ),
    'especie.codigo'
)
# Filtro comun para todas las consultas
# db.especie._common_filter = lambda query: (db.genero.id == db.especie.genero) & (db.genero.cby == auth.user_id) & (db.especie.exc == False)
db.especie._common_filter = lambda query: (db.especie.exc == False)


# Grupo del suelo (cada tipo de suelo pertenece a un grupo de suelo)
db.define_table("gruposuelo",
    Field("nombre", type='string', length= 10, notnull=True, unique=True, label=T("Grupo suelo")),
    Field("descripcion", type='text', label=T("Descripción del grupo suelo")),
    format='%(nombre)s'
)


#Tipos de desperdicios en la industria:
db.define_table("tiporesiduoforestal",
    Field("nombre", type="string", length=25, unique=True, notnull=True, label=T("Residuo forestal")),
    format='%(nombre)s'
)


#Tipos de intervencion raleo, tala rasa, rebrote
db.define_table("tipointervencion",
    Field("nombre", type="string", length=25, unique=True, notnull=True, label=T("Tipo intervencion")),
    format='%(nombre)s'
)


#Subtipos de intervencion raleo: Raleo I, Raleo II, Raleo III, etc.
db.define_table("stintervencion",
    Field('tintervencion', db.tipointervencion, notnull=True, label=T('Tipo intervencion')),
    Field("nombre", type="string", length=25, unique=True, notnull=True, label=T("Sub-tipo intervencion")),
    Field("observaciones", type="string", length=250, label=T("Observaciones")),
    format='%(nombre)s'
)


from cascadingselect import CascadingSelect
# Widget para especie
cSelEsp = CascadingSelect(db.genero, db.especie)
cSelEsp.prompt = lambda table: T("Select %s") % str(table).capitalize()


# Destinos de los rodales
db.define_table("destino",
    Field("nombre", type="string", length=50, unique=True, notnull=True, label=T("Destino")),
    format='%(nombre)s'
)


# Tipo de cosechas
db.define_table("cosecha",
    Field("nombre", type='string', notnull=True, unique=True, label=T("Cosecha")),
    Field("descripcion", type='text'),
    format='%(nombre)s'
)


# tablas que puedo actualizar
db.define_table("tname",
    Field("nombre", type='string', notnull=True, unique=True, label=T("Table name")),
    format='%(nombre)s'
)


# registro de actualizaciones
db.define_table("tupdated",
    Field("fecha", type='datetime', notnull=True, label=T("Fecha actualización")),
    Field('tname', db.tname, notnull=True, label=T('Tabla')),
    # Creado por ...
    Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
    format='%(tname)s'
)


# Planes presentados a al DGF
db.define_table("plan",
    # El numero del plan de manejo
    Field('ncarpeta', type='integer', notnull=True, label=T('Número de carpeta')),
    # Seccion judicial para ese departamento
    Field('sjudicial', db.seccionjudicial, label=T('Sección judicial')),
    # Longitud en grados decimales
    Field('lon', type='double', label=T('Longitud (º)')),
    # Latitud en grados decimales
    Field('lat', type='double', label=T('Latitud(º)')),
    # Creado por ...
    Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por'))
)
# Filtro comun para todas las consultas
db.plan._common_filter = lambda query: (db.plan.cby == auth.user_id)
# Composite unique
db.plan.ncarpeta.requires=IS_NOT_IN_DB(
    db(
        (db.plan.cby == auth.user_id)
    ),
    'plan.ncarpeta'
)


# Datos de plan temporal (desde DGF)
db.define_table("plantmp",
    Field('ncarpeta', type='integer', notnull=True, label=T('Número de carpeta')),
    Field('depto', type='integer'),
    Field('sj', type='integer'),
    Field('lon', type='double', label=T('Longitud (º)')),
    Field('lat', type='double', label=T('Latitud(º)')),
    # Creado por ...
    Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por'))
)
# Filtro comun para todas las consultas
db.plantmp._common_filter = lambda query: (db.plantmp.cby == auth.user_id)
# Composite unique
db.plantmp.ncarpeta.requires=IS_NOT_IN_DB(
    db(
        (db.plantmp.cby == auth.user_id)
    ),
    'plantmp.ncarpeta'
)


# Montes declarados de la DGF
db.define_table("rodald",
    # Referencia al plan
    Field('plan', db.plan, notnull=True),
    # referencia a la especie
    Field('especie', db.especie, notnull=True),
    # Anio en que se planto el monte
    Field('anioplant', type='integer', notnull=True, label=T('Año plantado')),
    # Area afectada por el monte
    Field('areaafect', type='float', notnull=True, label=T('Área afectada(ha)')),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por'))
)
# Filtro comun para todas las consultas
# db.rodald._common_filter = lambda query: (db.rodald.cby == auth.user_id)


# Datos de rodales temporal (desde DGF)
db.define_table("rodaldtmp",
    Field('ncarpeta', type='integer', notnull=True),
    # Genero: Eucalyptus
    Field('ngen', type="string", notnull=True),
    # Especie: globolus spp
    Field('nesp', type='string', notnull=True),
    Field('anioplant', type='integer', notnull=True),
    Field('areaafect', type='float', notnull=True),
    # Creado por ...
    Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por'))
)
# Filtro comun para todas las consultas
# db.rodaldtmp._common_filter = lambda query: (db.rodaldtmp.cby == auth.user_id)


# Ubicacion montes declarados
db.define_table("ubicacionrodald",
    Field('rodal', db.rodald, unique=True, notnull=True),
    # Seccion judicial para ese departamento
    Field('sjudicial', db.seccionjudicial, notnull=True),
    # Longitud en grados decimales
    Field('lon', type='double'),
    # Latitud en grados decimales
    Field('lat', type='double'),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por'))
)
# Filtro comun para todas las consultas
# db.ubicacionrodald._common_filter = lambda query: (db.ubicacionrodald.cby == auth.user_id)


# Tipo suelo montes declarados
db.define_table("gruposuelorodald",
    Field('rodal', db.rodald, notnull=True),
    # Seccion judicial para ese departamento
    Field('gsuelo', db.gruposuelo, notnull=True),
    # Superficie
    Field('superficie', notnull=True, type='double', label=T('Superficie de tipo de suelo')),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por'))
)
# rodal and suelo uniques
db.gruposuelorodald.gsuelo.requires=IS_NOT_IN_DB(
    db((db.gruposuelorodald.rodal == request.vars.rodal)), 'gruposuelorodald.gsuelo'
)
# Filtro comun para todas las consultas
# db.gruposuelorodald._common_filter = lambda query: (db.gruposuelorodald.cby == auth.user_id)

# Intervención (raleo, corte, etc.) para montes declarados UNIQUE(raodal, anios)
db.define_table("intervrodald",
    Field('rodal', db.rodald, notnull=True),
    # tiempo en anios desde que se planta
    Field('stintervencion', db.stintervencion, notnull=True, label=T('Subtipo intervencion')),
    # tiempo en anios desde que se planta
    Field('adisp', type='float', notnull=True, label=T('Año de corte')),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.intervrodald._common_filter = lambda query: (db.intervrodald.cby == auth.user_id)


# Destinos de la intervencion en el rodal declarado
db.define_table("destinointervrodald",
    Field('irodal', db.intervrodald, notnull=True),
    # destino
    Field('destino', db.destino, notnull=True),
    # volumen de corta en m3
    Field('mcmcc', type='float', notnull=True, label=T('Volumen (m3 mcc)')),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.destinointervrodald._common_filter = lambda query: (db.destinointervrodald.cby == auth.user_id)


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
    Field('hora', type='time'),
    # Creado por ...
    Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por'))
)


# Dias y hora que actualiza el modelo
db.define_table("actualizamodelo",
    Field('dia', db.dia),
    Field('hora', type='time'),
    # Creado por ...
    Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por'))
)


##### Coeficiente para estimar datos faltantes
## Cuanto crece por ano (ima=indice medio anual)
db.define_table("cima",
    Field("especie", db.especie, label=T("Especie"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("departamento", db.departamento,
      required=True, requires=IS_IN_DB(db, 'departamento.id', '%(nombre)s'),
      represent=lambda id, r: db.departamento(id).nombre
    ),
    Field("ima", type="float", notnull=True, label=T(u"IMA (m3/ha/año)")),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.cima._common_filter = lambda query: (db.cima.cby == auth.user_id)
# Una especie con un destino = 1 solo valor de corta
db.cima.ima.requires=IS_NOT_IN_DB(
    db(
        (db.cima.especie == request.vars.especie) &
        (db.cima.departamento == request.vars.departamento)
        # (db.cima.cby == auth.user_id)
    ),
    'cima.ima'
)
db.cima.ima.requires = IS_FLOAT_IN_RANGE(0, 50, dot='.', error_message=T('Too small or to large'))
db.cima.especie.widget=cSelEsp.widget


## Que porcentaje del bosque es area efectiva de plantacion
db.define_table("caefectiva",
    Field("especie", db.especie, label=T("Especie"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("departamento", db.departamento,
      required=True, requires=IS_IN_DB(db, 'departamento.id', '%(nombre)s'),
      represent=lambda id, r: db.departamento(id).nombre
    ),
    Field("aefectiva", type="float", notnull=True, label=T("Área efectiva")),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.caefectiva._common_filter = lambda query: (db.caefectiva.cby == auth.user_id)
# Una especie con un destino = 1 solo valor de corta
db.caefectiva.aefectiva.requires = IS_NOT_IN_DB(
    db(
        (db.caefectiva.especie == request.vars.especie) &
        (db.caefectiva.departamento == request.vars.departamento)
        # (db.cima.cby == auth.user_id)
    ),
    'caefectiva.aefectiva'
)
db.caefectiva.aefectiva.requires = IS_FLOAT_IN_RANGE(0, 1, dot='.', error_message=T('Too small or to large'))
db.caefectiva.especie.widget=cSelEsp.widget


## Una especie, en un departamento se interviene (ralea, corta) a los tantos años (por ejemplo a los 7, 13 y 15 años) y se extrae un porcentaje de lo disponible (0-1)
db.define_table("cintervencionr",
    Field("especie", db.especie, label=T("Especie"),
      notnull=True, required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("departamento", db.departamento,
      notnull=True, required=True, requires=IS_IN_DB(db, 'departamento.id', '%(nombre)s'),
      represent=lambda id, r: db.departamento(id).nombre
    ),
    Field("stintervencion", db.stintervencion,
      notnull=True, required=True, requires=IS_IN_DB(db, 'stintervencion.id', '%(nombre)s'),
      represent=lambda id, r: db.stintervencion(id).nombre, label=T("Subtipo intervención")
    ),
    Field("aintervencion", type="decimal(5,3)", notnull=True, label=T(u"Tiempo (años)")),
    Field("fextraccion", type="float", notnull=True, label=T("Factor extracción")),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.cintervencionr._common_filter = lambda query: (db.cintervencionr.cby == auth.user_id)
db.cintervencionr.aintervencion.requires = IS_FLOAT_IN_RANGE(0, 50, dot='.', error_message=T('Too small or to large'))
db.cintervencionr.fextraccion.requires = IS_FLOAT_IN_RANGE(0, 1, dot='.', error_message=T('Too small or to large'))
db.cintervencionr.especie.widget=cSelEsp.widget


# Cada raleo puede tener una fracion de cada destino. El primer raleo va a pulpa (destino: Pulpa, fdestino:1), el seguno 60% plpa 40% aserrio (destino:Pulpa, fdestino:0.6; destino:Aserrio, fdestino:0.4)
db.define_table("cdintervencionr",
    Field("cintervencionr", db.cintervencionr),
    Field("destino", db.destino, label=T("Destino del rodal"),
        required=True, requires=IS_IN_DB(db, 'destino.id', '%(nombre)s'),
        represent=lambda id, r: db.destino(id).nombre
    ),
    Field("fdestino", type="float", notnull=True, label=T("Factor de destino")),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.cdintervencionr._common_filter = lambda query: (db.cdintervencionr.cby == auth.user_id)


## Una especie, en un departamento se interviene (ralea, corta) a los tantos años (por ejemplo a los 7, 13 y 15 años) y se extrae un porcentaje de lo disponible (0-1)
db.define_table("cintervenciona",
    Field("especie", db.especie, label=T("Especie"),
        notnull=True, required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
        represent=lambda id, r: db.especie(id).nombre
    ),
    Field("departamento", db.departamento,
        notnull=True, required=True, requires=IS_IN_DB(db, 'departamento.id', '%(nombre)s'),
        represent=lambda id, r: db.departamento(id).nombre
    ),
    Field("stintervencion", db.stintervencion,
      notnull=True, required=True, requires=IS_IN_DB(db, 'stintervencion.id', '%(nombre)s'),
      represent=lambda id, r: db.stintervencion(id).nombre, label=T("Subtipo intervención")
    ),
    Field("farea", type="float", notnull=True, label=T("Factor de área")),
    Field("aintervencion", type="decimal(5,3)", notnull=True, label=T(u"Tiempo (años)")),
    Field("fextraccion", type="float", notnull=True, label=T("Factor extracción")),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.cintervenciona._common_filter = lambda query: (db.cintervenciona.cby == auth.user_id)

db.cintervenciona.aintervencion.requires = IS_FLOAT_IN_RANGE(0, 50, dot='.', error_message=T('Too small or to large'))
db.cintervenciona.fextraccion.requires = IS_FLOAT_IN_RANGE(0, 1, dot='.', error_message=T('Too small or to large'))
db.cintervenciona.farea.requires = IS_FLOAT_IN_RANGE(0, 1, dot='.', error_message=T('Too small or to large'))
db.cintervenciona.especie.widget=cSelEsp.widget

# Cada raleo puede tener una fracion de cada destino. El primer raleo va a pulpa (destino: Pulpa, fdestino:1), el seguno 60% plpa 40% aserrio (destino:Pulpa, fdestino:0.6; destino:Aserrio, fdestino:0.4)
db.define_table("cdintervenciona",
    Field("cintervenciona", db.cintervenciona),
    Field("destino", db.destino, label=T("Destino del rodal"),
        required=True, requires=IS_IN_DB(db, 'destino.id', '%(nombre)s'),
        represent=lambda id, r: db.destino(id).nombre
    ),
    Field("fdestino", type="float", notnull=True, label=T("Factor de destino")),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.cdintervenciona._common_filter = lambda query: (db.cdintervenciona.cby == auth.user_id)


# Coeficientes de campo bcampo en m3 de madera solida
db.define_table("cbcampo",
    Field("especie", db.especie, label=T("Especie"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("gsuelo", db.gruposuelo, label=T("Grupo de suelo"),
        required=True, requires=IS_IN_DB(db, 'gruposuelo.id', '%(nombre)s'),
        represent=lambda id, r: db.gruposuelo(id).nombre
    ),
    Field("stintervencion", db.stintervencion,
      notnull=True, required=True, requires=IS_IN_DB(db, 'stintervencion.id', '%(nombre)s'),
      represent=lambda id, r: db.stintervencion(id).nombre, label=T("Subtipo intervención")
    ),
    Field("cosecha", db.cosecha, label=T("Tipo de cosecha"),
        required=True, requires=IS_IN_DB(db, 'cosecha.id', '%(nombre)s'),
        represent=lambda id, r: db.cosecha(id).nombre
    ),
    Field("bcampo", type="float", notnull=True, label=T("Fv (m3 MS)")),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.cbcampo._common_filter = lambda query: (db.cbcampo.cby == auth.user_id)
# No puede haber dos valores para especie, suelo, destino, cosecha
db.cbcampo.bcampo.requires=IS_NOT_IN_DB(
    db(
        (db.cbcampo.especie == request.vars.especie) &
        (db.cbcampo.gsuelo == request.vars.gsuelo) &
        (db.cbcampo.stintervencion == request.vars.stintervencion) &
        (db.cbcampo.cosecha == request.vars.cosecha)
        # (db.cbcampo.cby == auth.user_id)
    ),
    'cbcampo.bcampo'
)

db.cbcampo.especie.widget=cSelEsp.widget


# Coeficiente general en la industria
db.define_table("cbindustria",
    Field("especie", db.especie, label=T("Especie"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("bindustria", type="float", notnull=True, label=T("Coeficiente")),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.cbindustria._common_filter = lambda query: (db.cbindustria.cby == auth.user_id)

# No puede haber dos valores para una misma especie
db.cbindustria.bindustria.requires=IS_NOT_IN_DB(
    db(
        (db.cbindustria.especie == request.vars.especie)
        # (db.cbcampo.cby == auth.user_id)
    ),
    'cbindustria.bindustria'
)
db.cbindustria.especie.widget=cSelEsp.widget


# Particiones de destinos de biomasa en la industria
db.define_table("cbindustriatrf",
    Field("cbindustria", db.cbindustria, required=True),
    Field("trf", db.tiporesiduoforestal, label=T("Tipo residuo"),
      required=True, requires=IS_IN_DB(db, 'tiporesiduoforestal.id', '%(nombre)s'),
      represent=lambda id, r: db.tiporesiduoforestal(id).nombre
    ),
    Field("coeficiente", type="float", notnull=True, label=T("Coeficiente")),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.cbindustriatrf._common_filter = lambda query: (db.cbindustriatrf.cby == auth.user_id)
# No puede haber dos valores para una misma especie
db.cbindustriatrf.coeficiente.requires=IS_NOT_IN_DB(
    db(
        (db.cbindustriatrf.cbindustria == request.vars.cbindustria) &
        (db.cbindustriatrf.trf == request.vars.trf)
        # (db.cbcampo.cby == auth.user_id)
    ),
    'cbindustriatrf.coeficiente'
)


# No tengo grupo de suelos para cada rodal (si la seccion judicial) por lo caul por ahora le asigno un único grupo
# por sección judicial. Con esto saco el grupo de suelo de cada rodal.
db.define_table("cgsuelo",
    Field("sjudicial", db.seccionjudicial, label=T("Sección judicial"),
        unique=True, required=True, requires=IS_IN_DB(db, 'seccionjudicial.id', '%(nombre)s'),
        represent=lambda id, r: db.seccionjudicial(id).nombre
    ),
    Field("gsuelo", db.gruposuelo, label=T("Grupo de suelo"),
        required=True, requires=IS_IN_DB(db, 'gruposuelo.id', '%(nombre)s'),
        represent=lambda id, r: db.gruposuelo(id).nombre
    ),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.cgsuelo._common_filter = lambda query: (db.cgsuelo.cby == auth.user_id)

# Widget para seccion judicial
# cSelSJ = CascadingSelect(db.departamento, db.seccionjudicial)
# cSelSJ.prompt = lambda table: T("Select %s") % str(table).capitalize()
# db.cgsuelo.sjudicial.widget=cSelSJ.widget


# Cada especie y destino tiene un tipo de cosecha
db.define_table("ccosecha",
    Field("especie", db.especie, label=T("Especie"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("destino", db.destino, label=T("Destino"),
        required=True, requires=IS_IN_DB(db, 'destino.id', '%(nombre)s'),
        represent=lambda id, r: db.destino(id).nombre
    ),
    Field("cosecha", db.cosecha, label=T("Tipo de cosecha"),
        required=True, requires=IS_IN_DB(db, 'cosecha.id', '%(nombre)s'),
        represent=lambda id, r: db.cosecha(id).nombre
    ),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.ccosecha._common_filter = lambda query: (db.ccosecha.cby == auth.user_id)
db.ccosecha.especie.widget=cSelEsp.widget


# Conversion del coeficiente de biomasa por especie bcampo en toneladas de biomasa
db.define_table("cbcampoe",
    Field("especie", db.especie, label=T("Especie"),
        required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
        represent=lambda id, r: db.especie(id).nombre),
    Field("bcampo", type="float", notnull=True, label=T("Fv (T biomasa)")),
    # Creado por ...
    # Field('cby', db.auth_user, writable=False, readable=False, notnull=True, default=auth.user_id, label=T('Creado por')),
)
# Filtro comun para todas las consultas
# db.cbcampoe._common_filter = lambda query: (db.cbcampoe.cby == auth.user_id)
db.cbcampoe.especie.widget=cSelEsp.widget
