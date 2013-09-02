# -*- coding: utf-8 -*-
@auth.requires_login()
def verifymodel():
    import json
    cstr=[
        T('effective area'),
        T('annual average growth rate'),
        T('intervention by stands'),
        T('intervention by area'),
        T('harvest'),
        T('soil group'),
        T('biomass conversion'),
        T('field biomass'),
        T('biomass in the industry'),
    ]
    coef=[
        'caefectiva',
        'cima',
        'cintervencionr',
        'cintervenciona',
        'ccosecha',
        'cgsuelo',
        'cbcampoe',
        'cbcampo',
        'cbindustria'
    ]
    trs= [
        TR(
            TD( T('Verify %s coefficients') % cstr[cont] ),
            TD( SPAN( B( db( db[ coef[cont] ]['id']>0 ).count() ), T(' records') ) ),
            TD(
                DIV(
                    SPAN(
                        #Button
                        A(
                            SPAN(I(_class='icon-check icon-black'), T('Verify now')),
                            _class='btn btn-small',
                            _onclick="return aVerifyCoef('%s');" % coef[cont],
                            _id="v%sbutton" % coef[cont]
                        ),
                        IMG(
                            _src="/%s/static/images/pbar_loader.gif" % request.application,
                            _id="pb%s" % coef[cont],
                            _style="display:none;height:10px;"
                        ),
                        #Return labels
                        SPAN(
                            T('Success'),
                            _class="label label-success",
                            _id="s%sspan" % coef[cont],
                            _style="display:none",
                        ),
                        SPAN(
                            T('Fail'),
                            _class="label label-warning",
                            _id="f%sspan" % coef[cont],
                            _style="display:none",
                        ),
                        SPAN(
                            T('Error'),
                            _class="label label-important",
                            _id="e%sspan" % coef[cont],
                            _style="display:none",
                        )
                    ),
                    _id="rv%s" % coef[cont],
                    _class="div div-btn div-info",
                    _style="width:240px;"
                    )
                )
            ) for cont in range(0,len(coef))
    ]

    trs.append(
        TR(
            TD( B( T('Verify all') ), _colspan="2", _style="text-align:right"),
            TD(
                A(
                    SPAN(I(_class='icon-check icon-black'), T('Verify now')),
                    _class='btn btn-small',
                    _onclick="return aVerifyAllCoef(%s);" % json.dumps(coef)
                )
            )
        )
    )

    table=TABLE (
        TBODY( trs ),
        _class="table table-striped",
        _id="modelverify"
    )
    return dict(table=table)

def averifycoefs():
    import json
    result=False
    tableName=request.post_vars.tableName
    data={ 'result': result }
    return json.dumps(data)

###
@auth.requires_login()
def mdestino():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='destino')
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())

def mtiporesiduoforestal():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='tiporesiduoforestal')
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


def mcosecha():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='cosecha')
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())
###


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
def mcintervencionr():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cintervencionr.id > 0) &
        (db.especie.id==db.cintervencionr.especie) &
        (db.genero.id==db.especie.genero) &
        (db.departamento.id==db.cintervencionr.departamento)
        )
    dm.gQuery( query )
    dm.actionTableName('cintervencionr')
    dm.gFieldId('id')
    dm.gFields( [
        ('cintervencionr','id'),
        ('genero','nombre'),
        ('cintervencionr','especie'),
        ('cintervencionr','departamento'),
        ('cintervencionr','aintervencion'),
        ('cintervencionr','fextraccion')
        ] )
    dm.gShowId(False)
    dm.showDActions(True)
    dm.rDetailsURL( "/%s/%s/%s.load" % (request.application, request.controller ,'mcdintervencionr') )
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_login()
def mcintervenciona():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cintervenciona.id > 0) &
        (db.especie.id==db.cintervenciona.especie) &
        (db.genero.id==db.especie.genero) &
        (db.departamento.id==db.cintervenciona.departamento)
        )
    dm.gQuery( query )
    dm.actionTableName('cintervenciona')
    dm.gFieldId('id')
    dm.gFields( [
        ('cintervenciona','id'),
        ('genero','nombre'),
        ('cintervenciona','especie'),
        ('cintervenciona','departamento'),
        ('cintervenciona','farea'),
        ('cintervenciona','aintervencion'),
        ('cintervenciona','fextraccion')
        ] )
    dm.gShowId(False)
    dm.showDActions(True)
    dm.rDetailsURL( "/%s/%s/%s.load" % (request.application, request.controller ,'mcdintervenciona') )
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
def mcbcampoe():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cbcampoe.id > 0) &
        (db.especie.id==db.cbcampoe.especie) &
        (db.genero.id==db.especie.genero)
        )
    dm.gQuery( query )
    dm.actionTableName('cbcampoe')
    dm.gFieldId('id')
    dm.gFields( [
        ('cbcampoe','id'),
        ('genero','nombre'),
        ('cbcampoe','especie'),
        ('cbcampoe','bcampo'),
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

def mcdintervencionr():
    # Vendra por ajax, recibe un post con el id de intervencion
    # Se fija si tiene registros y arma tantas forms como destinos existan en al base de datos
    try:
        #Que registro
        idIntervencion=int(request.post_vars.dataId)
        #Que destinos hay
        destinos=db(
            db['destino']['id']>0
        ).select(
            db['destino']['id'],
            db['destino']['nombre'],
            orderby=db['destino']['nombre']
        )
        ndest=len(destinos)
        did=[ destinos[i]['id'] for i in range(0,ndest) ]
        dnombres=[ destinos[i]['nombre'] for i in range(0,ndest) ]
        forms=[]
        for c in range(0,ndest):
            q=db(
                ( db['cdintervencionr']['cintervencionr']==idIntervencion ) &
                ( db['cdintervencionr']['destino']==did[c] )
            )
            if q.isempty():
                form = SQLFORM(db['cdintervencionr'], showid=True, _id="cdintervencionr_%s" % c)
            else:
                s=q.select()
                record=db['cdintervencionr']( s[0]['id'] )
                form = SQLFORM(db['cdintervencionr'], record, showid=True, _id="cdintervencionr_%s" % c)
                # Ocultar id
                fid = form.element('span',_id='cdintervencionr_id')
                fid['_style'] = 'display:none;'

            # Ocultar submit
            submit = form.element('input',_type='submit')
            submit['_style'] = 'display:none;'
            # Ocultar idIntervencion
            fcintervencionr = form.element('input',_id='cdintervencionr_cintervencionr')
            fcintervencionr['_value'] = idIntervencion
            fcintervencionr['_style'] = 'display:none;'
            fcintervencionr['_disabled'] = 'disabled'
            # Valor del destino
            fdestino = form.element('select',_id='cdintervencionr_destino')
            fdestino['_disabled'] = 'disabled'
            fdestino['_style'] = 'display:none;'
            val = fdestino.element('option',_value="%s" % did[c])
            val['_selected'] = 'selected'
            # Valor del fdestino
            ffdestino = form.element('input',_id='cdintervencionr_fdestino')
            ffdestino['_onblur'] = "checkFDestino(%d);" % c
            # Agregar a la lista
            forms.append(form)
        return dict(dnombres=dnombres, forms=forms)
    except Exception as e:
        print "%s" % e
        try:
            print "request.post_vars: %s" % request.post_vars
            print "request.post_vars.cdir_fdestino: %s" % request.post_vars['cdir_fdestino[]']
            if 'cdir_id[]' in request.post_vars.keys():
                ids=[ int(e) if len(e)>0 else None for e in request.post_vars['cdir_id[]'] ]
            else:
                ids=[ None for i in range( 0, len(request.post_vars['cdir_fdestino[]']) ) ]
            cintervencionrs=[ int(e) if len(e)>0 else None for e in request.post_vars['cdir_cintervencionr[]'] ]
            destinos=[ int(e) if len(e)>0 else None for e in request.post_vars['cdir_destino[]'] ]
            fdestinos=[ float(e) if len(e)>0 else None for e in request.post_vars['cdir_fdestino[]'] ]
            cont=0
            for f in fdestinos:
                if f==None:
                    if ids[cont]!=None:
                        print "deleting"
                        db( db['cdintervencionr']['id']==ids[cont] ).delete()
                    else:
                        pass
                else:
                    if ids[cont]!=None:
                        print "updating"
                        db( db['cdintervencionr']['id']==ids[cont] ).update(
                            fdestino=fdestinos[cont]
                        )
                    else:
                        print "inserting"
                        db['cdintervencionr'].insert(
                            cintervencionr=cintervencionrs[cont],
                            destino=destinos[cont],
                            fdestino=fdestinos[cont]
                        )
                cont=cont+1
        except Exception as e:
            print "%s" % e


def mcdintervenciona():
    # Vendra por ajax, recibe un post con el id de intervencion
    # Se fija si tiene registros y arma tantas forms como destinos existan en al base de datos
    try:
        #Que registro
        idIntervencion=int(request.post_vars.dataId)
        #Que destinos hay
        destinos=db(
            db['destino']['id']>0
        ).select(
            db['destino']['id'],
            db['destino']['nombre'],
            orderby=db['destino']['nombre']
        )
        ndest=len(destinos)
        did=[ destinos[i]['id'] for i in range(0,ndest) ]
        dnombres=[ destinos[i]['nombre'] for i in range(0,ndest) ]
        forms=[]
        for c in range(0,ndest):
            q=db(
                ( db['cdintervenciona']['cintervenciona']==idIntervencion ) &
                ( db['cdintervenciona']['destino']==did[c] )
            )
            if q.isempty():
                form = SQLFORM(db['cdintervenciona'], showid=True, _id="cdintervenciona_%s" % c)
            else:
                s=q.select()
                record=db['cdintervenciona']( s[0]['id'] )
                form = SQLFORM(db['cdintervenciona'], record, showid=True, _id="cdintervenciona_%s" % c)
                # Ocultar id
                fid = form.element('span',_id='cdintervenciona_id')
                fid['_style'] = 'display:none;'

            # Ocultar submit
            submit = form.element('input',_type='submit')
            submit['_style'] = 'display:none;'
            # Ocultar idIntervencion
            fcintervenciona = form.element('input',_id='cdintervenciona_cintervenciona')
            fcintervenciona['_value'] = idIntervencion
            fcintervenciona['_style'] = 'display:none;'
            fcintervenciona['_disabled'] = 'disabled'
            # Valor del destino
            fdestino = form.element('select',_id='cdintervenciona_destino')
            fdestino['_disabled'] = 'disabled'
            fdestino['_style'] = 'display:none;'
            val = fdestino.element('option',_value="%s" % did[c])
            val['_selected'] = 'selected'
            # Valor del fdestino
            ffdestino = form.element('input',_id='cdintervenciona_fdestino')
            ffdestino['_onblur'] = "checkFDestino(%d);" % c
            # Agregar a la lista
            forms.append(form)
        return dict(dnombres=dnombres, forms=forms)
    except Exception as e:
        print "%s" % e
        try:
            print "request.post_vars: %s" % request.post_vars
            print "request.post_vars.cdia_fdestino: %s" % request.post_vars['cdia_fdestino[]']
            if 'cdia_id[]' in request.post_vars.keys():
                ids=[ int(e) if len(e)>0 else None for e in request.post_vars['cdia_id[]'] ]
            else:
                ids=[ None for i in range( 0, len(request.post_vars['cdia_fdestino[]']) ) ]
            cintervencionas=[ int(e) if len(e)>0 else None for e in request.post_vars['cdia_cintervenciona[]'] ]
            destinos=[ int(e) if len(e)>0 else None for e in request.post_vars['cdia_destino[]'] ]
            fdestinos=[ float(e) if len(e)>0 else None for e in request.post_vars['cdia_fdestino[]'] ]
            cont=0
            for f in fdestinos:
                if f==None:
                    if ids[cont]!=None:
                        print "deleting"
                        db( db['cdintervenciona']['id']==ids[cont] ).delete()
                    else:
                        pass
                else:
                    if ids[cont]!=None:
                        print "updating"
                        db( db['cdintervenciona']['id']==ids[cont] ).update(
                            fdestino=fdestinos[cont]
                        )
                    else:
                        print "inserting"
                        db['cdintervenciona'].insert(
                            cintervenciona=cintervencionas[cont],
                            destino=destinos[cont],
                            fdestino=fdestinos[cont]
                        )
                cont=cont+1
        except Exception as e:
            print "%s" % e

## End manage coefficients
