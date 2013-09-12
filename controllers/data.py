# -*- coding: utf-8 -*-


@auth.requires_membership('users')
def vplanes():
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
        ('departamento','nombre'),
        ('seccionjudicial','nombre'),
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
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.rodald.id > 0) &
        (db.rodald.plan==db.plan.id) &
        (db.rodald.especie==db.especie.id) &
        (db.especie.genero==db.genero.id) &
        (db.seccionjudicial.id==db.plan.sjudicial) &
        (db.seccionjudicial.departamento==db.departamento.id) 
    )

    dm.gQuery( query )
    dm.actionTableName('planes')
    dm.gFieldId('id')
    dm.gFields( [
        ('rodald','id'),
        ('plan','ncarpeta'),
        ('departamento','nombre'),
        ('seccionjudicial','nombre'),
        ('genero','nombre'),
        ('especie','nombre'),
        ('rodald','anioplant'),
        ('rodald','areaafect')
        ] )
    dm.gShowId(False)
    dm.showMActions(False)
    # dm.showDActions(False)
    # dm.rDetailsURL( "/%s/%s/%s.load" % (request.application, request.controller ,'mcdintervencionr') )
    return dict(toolbar=dm.toolBar(), grid=dm.grid())
