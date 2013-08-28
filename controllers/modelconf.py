# -*- coding: utf-8 -*-

## Begin manage coefficients
@auth.requires_login()
def mcima():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cima.id > 0) &
        (db.especie.id==db.cima.especie) &
        (db.genero.id==db.especie.genero)
        )
    dm.gQuery( query )
    dm.actionTableName('cima')
    dm.gFieldId('id')
    dm.gFields( [
        ('cima','id'),
        ('genero','nombre'),
        ('cima','especie'),
        ('cima','departamento'),
        ('cima','ima')
        ] )
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())

@auth.requires_login()
def mcaefectiva():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.caefectiva.id > 0) &
        (db.especie.id==db.caefectiva.especie) &
        (db.genero.id==db.especie.genero)
    )
    dm.gQuery( query )
    dm.actionTableName('caefectiva')
    dm.gFieldId('id')
    dm.gFields( [
        ('caefectiva','id'),
        ('genero','nombre'),
        ('caefectiva','especie'),
        ('caefectiva','departamento'),
        ('caefectiva','aefectiva')
        ] )
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_login()
def mcintervencion():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cintervencion.id > 0) &
        (db.especie.id==db.cintervencion.especie) &
        (db.genero.id==db.especie.genero) &
        (db.tipocoeficiente.id==db.cintervencion.tcoeficiente) &
        (db.departamento.id==db.cintervencion.departamento)
        )
    dm.gQuery( query )
    dm.actionTableName('cintervencion')
    dm.gFieldId('id')
    dm.gFields( [
        ('cintervencion','id'),
        ('cintervencion','tcoeficiente'),
        ('genero','nombre'),
        ('cintervencion','especie'),
        ('cintervencion','departamento'),
        ('cintervencion','aintervencion'),
        ('cintervencion','fextraccion')
        ] )
    dm.gShowId(False)
    dm.showDActions(True)
    dm.rDetailsURL( "/%s/%s/%s.load" % (request.application, request.controller ,'mcdintervencion') )
    return dict(toolbar=dm.toolBar(), grid=dm.grid())

@auth.requires_login()
def mcbcampo():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cbcampo.id > 0) &
        (db.especie.id==db.cbcampo.especie) &
        (db.genero.id==db.especie.genero) &
        (db.gruposuelo.id==db.cbcampo.gsuelo) &
        (db.destino.id==db.cbcampo.destino) &
        (db.cosecha.id==db.cbcampo.cosecha)
        )
    dm.gQuery( query )
    dm.actionTableName('cbcampo')
    dm.gFieldId('id')
    dm.gFields( [
        ('cbcampo','id'),
        ('genero','nombre'),
        ('cbcampo','especie'),
        ('cbcampo','gsuelo'),
        ('cbcampo','destino'),
        ('cbcampo','cosecha'),
        ('cbcampo','bcampo'),
        ] )
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())

@auth.requires_login()
def mcbindustria():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cbindustria.id > 0) &
        (db.especie.id==db.cbindustria.especie) &
        (db.genero.id==db.especie.genero) &
        (db.tiporesiduoforestal.id==db.cbindustria.trf)
        )
    dm.gQuery( query )
    dm.actionTableName('cbindustria')
    dm.gFieldId('id')
    dm.gFields( [
        ('cbindustria','id'),
        ('genero','nombre'),
        ('cbindustria','especie'),
        ('cbindustria','trf'),
        ('cbindustria','bindustria')
        ] )
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_login()
def mcgsuelo():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cgsuelo.id > 0) &
        (db.seccionjudicial.id==db.cgsuelo.sjudicial) &
        (db.departamento.id==db.seccionjudicial.departamento) &
        (db.gruposuelo.id==db.cgsuelo.gsuelo)
        )
    dm.gQuery( query )
    dm.actionTableName('cgsuelo')
    dm.gFieldId('id')
    dm.gFields( [
        ('cgsuelo','id'),
        ('departamento','nombre'),
        ('cgsuelo','sjudicial'),
        ('cgsuelo','gsuelo')
        ] )
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_login()
def mccosecha():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.ccosecha.id > 0) &
        (db.especie.id==db.ccosecha.especie) &
        (db.genero.id==db.especie.genero) &
        (db.destino.id==db.ccosecha.destino) &
        (db.cosecha.id==db.ccosecha.cosecha)
        )
    dm.gQuery( query )
    dm.actionTableName('ccosecha')
    dm.gFieldId('id')
    dm.gFields( [
        ('ccosecha','id'),
        ('genero','nombre'),
        ('ccosecha','especie'),
        ('ccosecha','destino'),
        ('ccosecha','cosecha')
        ] )
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())

def mcdintervencion():
    #Vendra por ajax, recibe un post con el id de intervencio
    #Se fija si tiene registros y arma tantas forms como destinos existan en al base de datos
    tableName='destino'
    idF='id'
    try:
        #Que registro
        idIntervencion=request.post_vars.idIntervencion
        destinos=db(db[tableName][idF]>0).select(db[tableName][idF])
        # destinos[0]['idF']
        forms=[]
        for c in range(0,ndest):
            record=db[tableName](id)
            if record:
                form = SQLFORM(db['cdintervencion'], record, showid=False, _id="cdintervencion-%s" % c)
            else:
                form = SQLFORM(db['cdintervencion'], showid=False, _id="cdintervencion-%s" % c)
            # Ocultar submit
            submit = form.element('input',_type='submit')
            submit['_style'] = 'display:none;'
            # Ocultar idIntervencion

            # Agregar a la lista
            forms.append(form)
    except:
        print "idIntervencion error"
        pass
    dict(forms=forms)

## End manage coefficients
