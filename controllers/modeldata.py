# -*- coding: utf-8 -*-

@auth.requires_membership('users')
def all():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.rodald.id==db.intervrodald.rodal) &
        (db.plan.id==db.rodald.plan) &
        (db.plan.cby==auth.user_id) &
        (db.especie.id==db.rodald.especie) &
        (db.genero.id==db.especie.genero) &
        (db.seccionjudicial.id==db.plan.sjudicial) &
        (db.departamento.id==db.seccionjudicial.departamento) &
        (db.intervrodald.id==db.destinointervrodald.irodal)  &
        (db.stintervencion.id==db.intervrodald.stintervencion)
    )

    dm.gQuery( query )
    dm.actionTableName('destinointervrodald')
    dm.gFieldId('id')
    dm.gFields(
        [
            ('destinointervrodald','id'),
            ('plan','ncarpeta'),
            ('intervrodald','rodal'),
            ('seccionjudicial','departamento'),
            ('plan','sjudicial'),
            ('especie','genero'),
            ('rodald','especie'),
            ('intervrodald','stintervencion'),
            ('intervrodald','adisp'),
            ('destinointervrodald','destino'),
            ('destinointervrodald','mcmcc'),
        ]
    )
    dm.gShowId(False)
    dm.showMActions(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
def gbygenero():
    """

    """
    #from plugin_dm.datamanager import DataManager
    #dm=DataManager(database=db)
    query=(
        (db.destinointervrodald.id > 0) &
        (db.rodald.id==db.intervrodald.rodal) &
        (db.plan.id==db.rodald.plan) &
        (db.especie.id==db.rodald.especie) &
        (db.genero.id==db.especie.genero) &
        (db.seccionjudicial.id==db.plan.sjudicial) &
        (db.departamento.id==db.seccionjudicial.departamento) &
        (db.intervrodald.id==db.destinointervrodald.irodal)  &
        (db.tipointervencion.id==db.intervrodald.tintervencion)
    )
    """
    dm.gQuery( query )
    dm.actionTableName('destinointervrodald')
    dm.groupby='genero'
    dm.gFieldId('id')
    dm.gFields(
        [
            ('destinointervrodald','id'),
            ('plan','ncarpeta'),
            ('intervrodald','rodal'),
            ('seccionjudicial','departamento'),
            ('plan','sjudicial'),
            ('especie','genero'),
            ('rodald','especie'),
            ('intervrodald','tintervencion'),
            ('intervrodald','adisp'),
            ('destinointervrodald','destino'),
            ('destinointervrodald','mcmcc'),
        ]
    )
    dm.gShowId(False)
    dm.showMActions(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())
    """
    fields=[
            db.destinointervrodald.id,
            db.plan.ncarpeta,
            db.intervrodald.rodal,
            db.seccionjudicial.departamento,
            db.plan.sjudicial,
            db.especie.genero,
            db.rodald.especie,
            db.intervrodald.tintervencion,
            db.intervrodald.adisp,
            db.destinointervrodald.destino,
            db.destinointervrodald.mcmcc,
        ]
    grid=SQLFORM.grid(
        query=query,
        fields=fields,
        field_id=db.destinointervrodald.id,
        groupby=db.especie.genero|db.especie.nombre
    )
    return dict(grid=grid)


@auth.requires_membership('users')
def bycriteria():
    # departamentos
    d = db(db.departamento).select(db.departamento.ALL,orderby=db.departamento.nombre)
    # generos
    g = db(db.genero).select(db.genero.ALL,orderby=db.genero.nombre)
    # destinos
    dt = db(db.destino).select(db.destino.ALL,orderby=db.destino.nombre)
    # tipos intervencion
    ti = db(db.tipointervencion).select(db.tipointervencion.ALL,orderby=db.tipointervencion.nombre)
    return dict(d=d,g=g,dt=dt,ti=ti)


@auth.requires_membership('users')
def sjudicial():
    if 'dids[]' in request.post_vars.keys():
        dids=[ int(e) if len(e)>0 else None for e in request.post_vars['dids[]'] ]
        print "dids: %s" % dids
        if len(dids)>0:
            q = reduce(lambda a,b:a|b, [db.departamento.id==d for d in dids])
            q = q & (db.departamento.id==db.seccionjudicial.departamento)
            sj = db(
                q
            ).select(
                db.seccionjudicial.id,
                db.seccionjudicial.nombre,
                db.departamento.nombre,
                orderby=db.departamento.nombre|db.seccionjudicial.nombre
            )
            print "%s" % sj
        else:
            pass
        return dict(result=True,sj=sj)
    else:
        return dict(result=False,message='No data')
