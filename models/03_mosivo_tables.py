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

# Departamentos de UY
db.define_table("departamento",
    Field("nombre", type="string", length=25, unique=True, notnull=True, label=T("Departamento")),
    format='%(nombre)s'
)

# Seccion judicial por departamento
db.define_table("seccionjudicial",
    Field("departamento", db.departamento),
    Field("nombre", type="integer", notnull=True, label=T('Seccion judicial')),
)
# seccion and departamento must be uniques
db.seccionjudicial.nombre.requires=IS_NOT_IN_DB(
    db((db.seccionjudicial.departamento == request.vars.departamento)), 'seccionjudicial.nombre'
)

# Generos de arboles
db.define_table("genero",
    Field("nombre", type="string", length=50, unique=True, notnull=True, label=T("Género")),
    Field("codigo", type="string", length=1, notnull=True),
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
    Field("nombre", type="string", length=50, notnull=True, label=T("Especie")),
    Field("codigo", type="integer", notnull=True, label=T("Código de la especie")),
    format='%(nombre)s'
)
# Genero and codigo uniques
db.especie.codigo.requires=IS_NOT_IN_DB(
    db((db.especie.genero==request.vars.genero)), 'especie.codigo'
)

# Grupo del suelo (cada tipo de suelo pertenece a un grupo de suelo)
db.define_table("gruposuelo",
    Field("nombre", type='string', length= 10, notnull=True, unique=True, label=T("Grupo suelo")),
    Field("descripcion", type='text', label=T("Descripción del grupo suelo")),
    format='%(nombre)s'
)

#Tipos de desperdicios en la industria
db.define_table("tiporesiduoforestal",
    Field("nombre", type="string", length=25, unique=True, notnull=True, label=T("Residuo forestal")),
    format='%(nombre)s'
)

#Tipos de coeficientes es decir se aplican a nivel de Area o de rodal
db.define_table("tipocoeficiente",
    Field("nombre", type="string", length=25, unique=True, notnull=True, label=T("Tipo coeficiente")),
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

# Planes presentados a al DGF
db.define_table("plan",
    # El numero del Plan de manejo
    Field('numerocarpeta', type='integer', unique=True, notnull=True),
    # Seccion judicial para ese departamento
    Field('sjudicial', db.seccionjudicial),
    # Longitud en grados decimales
    Field('lon', type='double'),
    # Latitud en grados decimales
    Field('lat', type='double'),
)

# Montes declarados
db.define_table("rodald",
    # Referencia al plan
    Field('plan', db.plan, notnull=True),
    # referencia a la especie
    Field('especie', db.especie, notnull=True),
    # Anio en que se planto el monte
    Field('anioplant', notnull=True, type='integer'),
    # Area afectada por el monte
    Field('areaafect', notnull=True, type='float'),
)

# Ubicacion montes declarados
db.define_table("ubicacionrodald",
    Field('rodal', db.rodald, unique=True, notnull=True),
    # Seccion judicial para ese departamento
    Field('sjudicial', db.seccionjudicial, notnull=True),
    # Longitud en grados decimales
    Field('lon', type='double'),
    # Latitud en grados decimales
    Field('lat', type='double'),
)

# Tipo suelo montes declarados
db.define_table("gruposuelorodald",
    Field('rodal', db.rodald, notnull=True),
    # Seccion judicial para ese departamento
    Field('gsuelo', db.gruposuelo, notnull=True),
    # Superficie
    Field('superficie', notnull=True, type='double')
)
# rodal and suelo uniques
db.gruposuelorodald.gsuelo.requires=IS_NOT_IN_DB(
    db((db.gruposuelorodald.rodal == request.vars.rodal)), 'gruposuelorodald.gsuelo'
)

# Intervención (raleo, corte, etc.) para montes declarados UNIQUE(raodal, anios)
db.define_table("intervrodald",
    Field('rodal', db.rodald, notnull=True),
    # tiempo en anios desde que se planta
    Field('aintervencion', type='float', notnull=True, label=u'Corte (años)'),
    # volumen de corta en m3/ha
    # Field('volumen', type='float', notnull=True, label=u'Volumen(m3)'),
)

# Destinos de la intervencion en el rodal declarado
db.define_table("destinointervrodald",
    Field('irodal', db.intervrodald, notnull=True),
    # destino
    Field('destino', db.destino, notnull=True),
    # volumen de corta en m3/ha
    Field('volumen', type='float', notnull=True, label=u'Volumen(m3)'),
)

# Montes proyectados
db.define_table("rodalp",
    # Referencia a la carpeta
    Field('plan', db.plan, notnull=True),
    # referencia a la especie
    Field('especie', db.especie, notnull=True),
    # Anio en que se planto el monte
    Field('anioplant', notnull=True, type='integer'),
    # Area afectada por el monte
    Field('areaafect', notnull=True, type='float')
)

# Ubicacion montes proyectados
db.define_table("ubicacionrodalp",
    Field('rodal', db.rodalp, unique=True, notnull=True),
    # Seccion judicial para ese departamento
    Field('sjudicial', db.seccionjudicial, notnull=True),
    # Longitud en grados decimales
    Field('lon', type='double'),
    # Latitud en grados decimales
    Field('lat', type='double'),
)

# Tipo suelo montes proyectados
db.define_table("gruposuelorodalp",
    Field('rodal', db.rodalp, notnull=True),
    # Seccion judicial para ese departamento
    Field('gsuelo', db.gruposuelo, notnull=True),
    # Superficie
    Field('superficie', notnull=True, type='double')
)
# rodal and suelo uniques
db.gruposuelorodalp.gsuelo.requires = IS_NOT_IN_DB(
    db((db.gruposuelorodalp.rodal == request.vars.rodal)), 'gruposuelorodalp.gsuelo'
)

# Intervención (raleo, corte, etc.) para montes declarados UNIQUE(raodal, anios)
db.define_table("intervrodalp",
    Field('rodal', db.rodalp, notnull=True),
    # tiempo en anios desde que se planta
    Field('aintervencion', type='float', notnull=True, label=u'Corte (años)'),
    # volumen de corta en m3/ha
    # Field('volumen', type='float', notnull=True, label=u'Volumen(m3)'),
)

# Destinos de la intervencion en el rodal declarado
db.define_table("destinointervrodalp",
    Field('irodal', db.intervrodalp, notnull=True),
    # destino
    Field('destino', db.destino, notnull=True),
    # volumen de corta en m3/ha
    Field('volumen', type='float', notnull=True, label=u'Volumen(m3)'),
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
    Field("especie", db.especie, label=T("Especie"),
      required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
      represent=lambda id, r: db.especie(id).nombre
    ),
    Field("departamento", db.departamento,
      required=True, requires=IS_IN_DB(db, 'departamento.id', '%(nombre)s'),
      represent=lambda id, r: db.departamento(id).nombre
    ),
    Field("aefectiva", type="float", notnull=True, label=T("Área efectiva"))
)
# Una especie con un destino = 1 solo valor de corta
db.caefectiva.aefectiva.requires = IS_NOT_IN_DB(
    db((db.caefectiva.especie == request.vars.especie) & (db.caefectiva.departamento == request.vars.departamento)),
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
    Field("aintervencion", type="decimal(5,3)", notnull=True, label=T(u"Tiempo (años)")),
    Field("fextraccion", type="float", notnull=True, label=T("Factor extracción")),
)
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
    Field("fdestino", type="float", notnull=True, label=T("Factor de destino"))
)

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
    Field("farea", type="float", notnull=True, label=T("Factor de área")),
    Field("aintervencion", type="decimal(5,3)", notnull=True, label=T(u"Tiempo (años)")),
    Field("fextraccion", type="float", notnull=True, label=T("Factor extracción")),
)
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
    Field("fdestino", type="float", notnull=True, label=T("Factor de destino"))
)


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
    Field("destino", db.destino, label=T("Destino"),
        required=True, requires=IS_IN_DB(db, 'destino.id', '%(nombre)s'),
        represent=lambda id, r: db.destino(id).nombre
    ),
    Field("cosecha", db.cosecha, label=T("Tipo de cosecha"),
        required=True, requires=IS_IN_DB(db, 'cosecha.id', '%(nombre)s'),
        represent=lambda id, r: db.cosecha(id).nombre
    ),
    Field("bcampo", type="float", notnull=True, label=T("Fv (m3 MS)"))
)
# No puede haber dos valores para especie, suelo, destino, cosecha
db.cbcampo.bcampo.requires=IS_NOT_IN_DB(
    db(
        (db.cbcampo.especie == request.vars.especie) &
        (db.cbcampo.gsuelo == request.vars.gsuelo) &
        (db.cbcampo.destino == request.vars.destino) &
        (db.cbcampo.cosecha == request.vars.cosecha)
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
    Field("trf", db.tiporesiduoforestal, label=T("Tipo residuo"),
      required=True, requires=IS_IN_DB(db, 'tiporesiduoforestal.id', '%(nombre)s'),
      represent=lambda id, r: db.tiporesiduoforestal(id).nombre
    ),
    Field("bindustria", type="float", notnull=True, label=T("Coeficiente"))
)
# No puede haber dos valores para una misma especie
db.cbindustria.bindustria.requires=IS_NOT_IN_DB(
    db(
        (db.cbindustria.especie == request.vars.especie) &
        (db.cbindustria.trf == request.vars.trf)
    ),
    'cbindustria.bindustria'
)
db.cbindustria.especie.widget=cSelEsp.widget


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
    )
)
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
)
db.ccosecha.especie.widget=cSelEsp.widget

# Conversion del coeficiente de biomasa por especie bcampo en toneladas de biomasa
db.define_table("cbcampoe",
    Field("especie", db.especie, label=T("Especie"),
        required=True, requires=IS_IN_DB(db, 'especie.id', '%(nombre)s'),
        represent=lambda id, r: db.especie(id).nombre),
    Field("bcampo", type="float", notnull=True, label=T("Fv (T biomasa)"))
)
db.cbcampoe.especie.widget=cSelEsp.widget


