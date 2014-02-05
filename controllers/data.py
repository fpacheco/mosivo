# -*- coding: utf-8 -*-


@auth.requires_membership('users')
def vplanes():
    """Muestra los datos de planes
    """
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.plan.id > 0) &
        (db.seccionjudicial.id==db.plan.sjudicial) &
        (db.departamento.id==db.seccionjudicial.departamento)
    )

    dm.gQuery( query )
    dm.actionTableName('planes')
    dm.gFieldId('id')
    dm.gFields( [
        ('plan','id'),
        ('plan','ncarpeta'),
        ('seccionjudicial','departamento'),
        ('plan','sjudicial'),
        ('plan','lon'),
        ('plan','lat'),
        ] )
    dm.gShowId(False)
    dm.showMActions(False)
    # dm.showDActions(False)
    # dm.rDetailsURL( "/%s/%s/%s.load" % (request.application, request.controller ,'mcdintervencionr') )
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
def vrodald():
    """Muestra los datos de rodales declarados
    """
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.ubicacionrodald.rodal==db.rodald.id) &
        (db.rodald.plan==db.plan.id) &
        (db.ubicacionrodald.sjudicial==db.seccionjudicial.id) &
        (db.seccionjudicial.departamento==db.departamento.id) &
        (db.rodald.especie==db.especie.id) &
        (db.especie.genero==db.genero.id) &
        (db.plan.cby==auth.user_id)
    )

    dm.gQuery( query )
    dm.actionTableName('ubicacionrodald')
    dm.gFieldId('id')
    dm.gFields( [
        ('ubicacionrodald','id'),
        ('plan','ncarpeta'),
        ('seccionjudicial','departamento'),
        ('seccionjudicial','nombre'),
        ('ubicacionrodald','lon'),
        ('ubicacionrodald','lat'),
        ('especie','genero'),
        ('rodald','especie'),
        ('rodald','anioplant'),
        ('rodald','areaafect'),
        ] )
    dm.gShowId(False)
    dm.showMActions(False)
    # dm.showDActions(False)
    # dm.rDetailsURL( "/%s/%s/%s.load" % (request.application, request.controller ,'mcdintervencionr') )
    return dict(toolbar=dm.toolBar(), grid=dm.grid())
