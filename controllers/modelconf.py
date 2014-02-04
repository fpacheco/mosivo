# -*- coding: utf-8 -*-
from gluon.tools import Service
service=Service()

def call():
    return service()

@service.json
@auth.requires_membership('users')
def nOfRows():
    """Number of rows in table
    """
    tName=request.post_vars.tName
    data={ 'nRows': nRows(tName) }
    return data


@service.json
@auth.requires_membership('users')
def updatedData():
    """Number of rows in table
    """
    tName=request.post_vars.tName
    ui = updatedInfo(tName)
    data={ 'updatedOn': ui[1], 'updatedBy': ui[2] }
    return data


@auth.requires_membership('users')
def configupdatefromrdb():
    """Central page for update. Two tabs. See mupdatefromrdb and aupdatefromrdb
    """
    mu="/%s/%s/%s" % (request.application, request.controller, 'mupdatefromrdb')
    au="/%s/%s/%s" % (request.application, request.controller, 'aupdatefromrdb')
    return dict(mu=mu, au=au)


@auth.requires_membership('users')
def aupdatefromrdb():
    """Automatic update page from remote database
    """
    return dict()

@auth.requires_membership('users')
def mupdatefromrdb():
    """Manual update page from remote database
    """
    import json
    cstr=[
        T('Genero'),
        T('Especie'),
        T('Plan'),
        T('Rodald')
    ]
    tnames=[
        'genero',
        'especie',
        'plan',
        'rodald'
    ]

    lastUpdate=[ updatedInfo(tnames[cont])[1] for cont in range(0,len(tnames)) ]
    byUser=[ updatedInfo(tnames[cont])[2] for cont in range(0,len(tnames)) ]

    trs= [
        TR(
            TD( T('Update %s') % cstr[cont] ),
            TD(
                SPAN(
                    T('Number of records: '),
                    SPAN(
                        nRows( tnames[cont] ),
                        _id="%s_nrecords" % tnames[cont],
                        _class="label"
                    )
                )
            ),
            TD(
                SPAN(
                    T('Last update on: '),
                    SPAN(
                        lastUpdate[cont],
                        _id="%s_lastupdate" % tnames[cont],
                        _class="label",
                        _title=T("By: %s") % byUser[cont]
                    )
                )
            ),
            TD(
                DIV(
                    SPAN(
                        #Button
                        A(
                            SPAN(I(_class=' icon-repeat icon-black'), T('Update now')),
                            _class='btn btn-small',
                            _onclick="return updateFromRDB('%s');" % tnames[cont],
                            _id="u%sbutton" % tnames[cont]
                        ),
                        IMG(
                            _src="/%s/static/images/pbar_loader.gif" % request.application,
                            _id="pb%s" % tnames[cont],
                            _style="display:none;height:10px;"
                        ),
                        #Return labels
                        SPAN(
                            T('Success'),
                            _class="label label-success",
                            _id="s%sspan" % tnames[cont],
                            _style="display:none",
                        ),
                        SPAN(
                            T('Fail'),
                            _class="label label-warning",
                            _id="f%sspan" % tnames[cont],
                            _style="display:none",
                        ),
                        SPAN(
                            T('Error'),
                            _class="label label-important",
                            _id="e%sspan" % tnames[cont],
                            _style="display:none",
                        )
                    ),
                    _id="ru%s" % tnames[cont],
                    _class="div div-btn div-info",
                    _style="width:240px;"
                )
            ),
            _id="%s" % tnames[cont]
        ) for cont in range(0,len(tnames))
    ]

    trs.append(
        TR(
            TD( B( T('Update all') ), _colspan="3", _style="text-align:right"),
            TD(
                A(
                    SPAN(I(_class=' icon-repeat icon-black'), T('Update now')),
                    _class='btn btn-small',
                    _onclick="return aUpdateAllCoef(%s);" % json.dumps(tnames),
                    _disabled="disabled"
                )
            )
        )
    )

    table=TABLE (
        TBODY( trs ),
        _class="table table-striped",
        _id="modelupdate"
    )
    return dict(table=table)


# @auth.requires_membership('users')
@service.json
def update():
    tnames=['genero','especie','plan','rodald']
    result=False
    res=[]
    try:
        updWhat=request.post_vars.updWhat
        if IN_DGF:
            print "You are in DGF!!!!!!"
        else:
            print "You are in InGeSur!!!!!!"
        print "updWhat: %s" % updWhat

        from getdatafromdgf.updatefromrdb import UpdateFromRDB
        u = UpdateFromRDB(mDatabase=db, mUid=auth.user_id, inDGF=IN_DGF)
        if updWhat=='genero':
            result=u.uGenero()
        elif updWhat=='especie':
            result=u.uEspecie()
        elif updWhat=='plan':
            result=u.uPlan()
        elif updWhat=='rodald':
            result=u.uRodalD()
        # elif updWhat=='all':
        #    res=u.uAll()
        else:
            print "Not here!"

        if result==True:
            return dict( result=insertTUpdated(updWhat) )
        else:
            return dict( result=False )
    except Exception as e:
        print "Error: %s" % e
        return dict( result=False )

@auth.requires_membership('users')
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


@auth.requires_membership('users')
def averifycoefs():
    import json
    result=False
    try:
        tableName=request.post_vars.tableName
        from mmodel.mmodel import MModel
        model = MModel(mDatabase=db)
        if tableName=='cima':
            result=model.checkCima()
        elif tableName=='caefectiva':
            result=model.checkCaefectiva()
        elif tableName=='cintervencionr':
            result=model.checkCintervencionr()
        elif tableName=='cintervenciona':
            result=model.checkCintervenciona()
        elif tableName=='cgsuelo':
            result=model.checkCgsuelo()
        elif tableName=='ccosecha':
            result=model.checkCcosecha()
        elif tableName=='cbcampoe':
            result=model.checkCbcampoe()
        elif tableName=='cbcampo':
            result=model.checkCbcampo()
        elif tableName=='cbindustria':
            result=model.checkCbindustria()
        else:
            print "Not here!"
        data={'result': result}
        return json.dumps(data)
    except Exception as e:
        print "Error: %s" % e


###
@auth.requires_membership('users')
def mdestino():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='destino')
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
def mtiporesiduoforestal():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='tiporesiduoforestal')
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
def mcosecha():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='cosecha')
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
def mtipointervencion():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='tipointervencion')
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
def mstintervencion():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='stintervencion')
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())
###


## Begin manage coefficients
@auth.requires_membership('users')
def mcima():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cima.id > 0) &
        (db.especie.id==db.cima.especie) &
        (db.genero.id==db.especie.genero) &
        (db.genero.cby==auth.user_id)
        )
    dm.gQuery( query )
    dm.actionTableName('cima')
    dm.gFieldId('id')
    dm.gFields( [
        ('cima','id'),
        ('especie','genero'),
        ('cima','especie'),
        ('cima','departamento'),
        ('cima','ima')
        ] )
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
def mcaefectiva():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.caefectiva.id > 0) &
        (db.especie.id==db.caefectiva.especie) &
        (db.genero.id==db.especie.genero) &
        (db.genero.cby==auth.user_id)
    )
    dm.gQuery( query )
    dm.actionTableName('caefectiva')
    dm.gFieldId('id')
    dm.gFields( [
        ('caefectiva','id'),
        ('especie','genero'),
        ('caefectiva','especie'),
        ('caefectiva','departamento'),
        ('caefectiva','aefectiva')
        ] )
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
def mcintervencionr():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cintervencionr.id > 0) &
        (db.especie.id==db.cintervencionr.especie) &
        (db.genero.id==db.especie.genero) &
        (db.genero.cby==auth.user_id) &
        (db.departamento.id==db.cintervencionr.departamento)
        )
    dm.gQuery( query )
    dm.actionTableName('cintervencionr')
    dm.gFieldId('id')
    dm.gFields( [
        ('cintervencionr','id'),
        ('especie','genero'),
        ('cintervencionr','especie'),
        ('cintervencionr','departamento'),
        ('cintervencionr','stintervencion'),
        ('cintervencionr','aintervencion'),
        ('cintervencionr','fextraccion')
        ] )
    dm.gShowId(False)
    dm.showDActions(True)
    dm.rDetailsURL( "/%s/%s/%s.load" % (request.application, request.controller ,'mcdintervencionr') )
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
def mcintervenciona():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cintervenciona.id > 0) &
        (db.especie.id==db.cintervenciona.especie) &
        (db.genero.id==db.especie.genero) &
        (db.genero.cby==auth.user_id) &
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
        ('cintervenciona','tintervencion'),
        ('cintervenciona','aintervencion'),
        ('cintervenciona','fextraccion')
        ] )
    dm.gShowId(False)
    dm.showDActions(True)
    dm.rDetailsURL( "/%s/%s/%s.load" % (request.application, request.controller ,'mcdintervenciona') )
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
def mcbcampo():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cbcampo.id > 0) &
        (db.especie.id==db.cbcampo.especie) &
        (db.genero.id==db.especie.genero) &
        (db.genero.cby==auth.user_id) &
        (db.gruposuelo.id==db.cbcampo.gsuelo) &
        (db.stintervencion.id==db.cbcampo.stintervencion) &
        (db.cosecha.id==db.cbcampo.cosecha)
        )
    dm.gQuery( query )
    dm.actionTableName('cbcampo')
    dm.gFieldId('id')
    dm.gFields( [
        ('cbcampo','id'),
        ('especie','genero'),
        ('cbcampo','especie'),
        ('cbcampo','gsuelo'),
        ('cbcampo','stintervencion'),
        ('cbcampo','cosecha'),
        ('cbcampo','bcampo'),
        ] )
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
def mcbcampoe():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cbcampoe.id > 0) &
        (db.especie.id==db.cbcampoe.especie) &
        (db.genero.id==db.especie.genero) &
        (db.genero.cby==auth.user_id)
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



@auth.requires_membership('users')
def mcbindustria():
    # Coeficiente de biomasa en la industria
    # Un coeficiente por especie que se puede desglosar (o no) por tipos de residuos forestales
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.cbindustria.id > 0) &
        (db.especie.id==db.cbindustria.especie) &
        (db.genero.id==db.especie.genero) &
        (db.genero.cby==auth.user_id)
        )
    dm.gQuery( query )
    dm.actionTableName('cbindustria')
    dm.gFieldId('id')
    dm.gFields( [
        ('cbindustria','id'),
        ('genero','nombre'),
        ('cbindustria','especie'),
        ('cbindustria','bindustria')
        ] )
    dm.gShowId(False)
    dm.showDActions(True)
    dm.rDetailsURL( "/%s/%s/%s.load" % (request.application, request.controller ,'mcbindustriatrf') )
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
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
        ('seccionjudicial','departamento'),
        ('cgsuelo','sjudicial'),
        ('cgsuelo','gsuelo')
        ] )
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


"""
@auth.requires_membership('admins')
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
"""


@auth.requires_membership('users')
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


@auth.requires_membership('users')
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


@auth.requires_membership('users')
def mcbindustriatrf():
    # Vendra por ajax, recibe un post con el id de cbindustria
    # Se fija si tiene registros y arma tantas forms como destinos existan en al base de datos
    # Destinos para biomasa en la industria
    try:
        #Que registro
        idCBIndustria=int(request.post_vars.dataId)
        #Que destinos hay
        trf=db(
            db['tiporesiduoforestal']['id']>0
        ).select(
            db['tiporesiduoforestal']['id'],
            db['tiporesiduoforestal']['nombre'],
            orderby=db['tiporesiduoforestal']['nombre']
        )
        ntrf=len(trf)
        trfid=[ trf[i]['id'] for i in range(0,ntrf) ]
        trfnombres=[ trf[i]['nombre'] for i in range(0,ntrf) ]

        #print ntrf
        #print trfid
        #print trfnombres

        forms=[]
        for c in range(0,ntrf):
            q=db(
                ( db['cbindustriatrf']['cbindustria']==idCBIndustria ) &
                ( db['cbindustriatrf']['trf']==trfid[c] )
            )
            if q.isempty():
                form = SQLFORM(db['cbindustriatrf'], showid=True, _id="cbindustriatrf_%s" % c)
                #print form
            else:
                s=q.select()
                record=db['cbindustriatrf']( s[0]['id'] )
                form = SQLFORM(db['cbindustriatrf'], record, showid=True, _id="cbindustriatrf_%s" % c)
                # Ocultar id
                fid = form.element('span',_id='cbindustriatrf_id')
                fid['_style'] = 'display:none;'

            # Ocultar submit
            submit = form.element('input',_type='submit')
            submit['_style'] = 'display:none;'
            # Ocultar idCBIndustria
            fcintervencionr = form.element('input',_id='cbindustriatrf_cbindustria')
            fcintervencionr['_value'] = idCBIndustria
            fcintervencionr['_style'] = 'display:none;'
            fcintervencionr['_disabled'] = 'disabled'
            # Valor del destino
            fdestino = form.element('select',_id='cbindustriatrf_trf')
            fdestino['_disabled'] = 'disabled'
            fdestino['_style'] = 'display:none;'
            val = fdestino.element('option',_value="%s" % trfid[c])
            val['_selected'] = 'selected'
            # Valor del fdestino
            ffdestino = form.element('input',_id='cbindustriatrf_coeficiente')
            ffdestino['_onblur'] = "checkCoeficiente(%d);" % c
            # Agregar a la lista
            forms.append(form)
        return dict(trfnombres=trfnombres, forms=forms)
    except Exception as e:
        print "Error: %s" % e
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


@auth.requires_membership('users')
def loadDefaults():
    # Coeficients para area efectiva
    if db(
        (db['caefectiva']['id']>0) &
        (db['caefectiva']['especie']==db['especie']['id']>0) &
        (db['especie']['genero']==db['genero']['id']>0) &
        (db['genero']['cby']==auth.user_id)
    ).isempty():
        sql1="INSERT INTO caefectiva(especie,departamento,aefectiva)"
        sql2="SELECT DISTINCT rd.especie, sj.departamento, 0.65 as aefectiva FROM rodald rd, plan p, seccionjudicial sj, especie e, genero g " \
            "WHERE rd.plan=p.id AND sj.id=p.sjudicial AND rd.especie=e.id AND e.genero=g.id AND g.cby=%i AND p.cby=%i AND e.exc='F' " \
            "ORDER BY sj.departamento" % (auth.user_id, auth.user_id)
        sql = "%s ( %s )" % (sql1, sql2)
        print sql
        db.executesql( sql )
    # Coeficientes para ima
    if db(
        db['cima']['id']>0 &
        (db['cima']['especie']==db['especie']['id']>0) &
        (db['especie']['genero']==db['genero']['id']>0) &
        (db['genero']['cby']==auth.user_id)
    ).isempty():
        sql1= "INSERT INTO cima(especie,departamento,ima) "
        sql2="(SELECT DISTINCT rd.especie, sj.departamento, 20.0 as ima FROM rodald rd, plan p, seccionjudicial sj, especie e, genero g  " \
            "WHERE rd.plan=p.id AND sj.id=p.sjudicial AND rd.especie=e.id AND e.genero=g.id AND g.cby=%i AND p.cby=%i AND e.exc='F' "\
            "ORDER BY sj.departamento)" % (auth.user_id, auth.user_id)
        sql = "%s ( %s )" % (sql1, sql2)
        print sql
        db.executesql( sql )
    # cgsuelo
    if db(db['cgsuelo']['id']>0).isempty():
        db.executesql(
            "INSERT INTO cgsuelo(sjudicial,gsuelo) " \
            "(SELECT DISTINCT p.sjudicial, 5 as gsuelo FROM plan p, seccionjudicial sj WHERE sj.id=p.sjudicial ORDER BY p.sjudicial);"
        )
    # Coeficientes para cintervencionr
    if db(db['cintervencionr']['id']>0).isempty():
        # 1
        db.executesql(
            "INSERT INTO cintervencionr(especie,departamento,stintervencion,aintervencion,fextraccion) " \
            "(SELECT DISTINCT rd.especie, sj.departamento, 1 as stintervencion, 3 as aintervencion, 0.3 as fextraccion FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento);"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 2, 1 FROM cintervencionr WHERE stintervencion=1 AND aintervencion=3::numeric(5,3))"
        )

        # 2
        db.executesql(
            "INSERT INTO cintervencionr(especie,departamento,stintervencion,aintervencion,fextraccion) " \
            "(SELECT DISTINCT rd.especie, sj.departamento, 2 as stintervencion, 8 as aintervencion, 0.3 as fextraccion FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento);"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 1, 0.8 FROM cintervencionr WHERE stintervencion=2 AND aintervencion=8::numeric(5,3))"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 2, 0.2 FROM cintervencionr WHERE stintervencion=2 AND aintervencion=8::numeric(5,3))"
        )

        # 3
        db.executesql(
            "INSERT INTO cintervencionr(especie,departamento,stintervencion,aintervencion,fextraccion) " \
            "(SELECT DISTINCT rd.especie, sj.departamento, 3 as stintervencion, 15 as aintervencion, 0.3 as fextraccion FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento);"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 1, 0.5 FROM cintervencionr WHERE stintervencion=3 AND aintervencion=15::numeric(5,3))"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 2, 0.5 FROM cintervencionr WHERE stintervencion=3 AND aintervencion=15::numeric(5,3))"
        )

        # 4
        db.executesql(
            "INSERT INTO cintervencionr(especie,departamento,stintervencion,aintervencion,fextraccion) " \
            "(SELECT DISTINCT rd.especie, sj.departamento, 5 as stintervencion, 20 as aintervencion, 1.00 as fextraccion FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento);"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 1, 0.8 FROM cintervencionr WHERE stintervencion=5 AND aintervencion=20::numeric(5,3))"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 2, 0.2 FROM cintervencionr WHERE stintervencion=5 AND aintervencion=20::numeric(5,3))"
        )

        # 5
        db.executesql(
            "INSERT INTO cintervencionr(especie,departamento,stintervencion,aintervencion,fextraccion) " \
            "(SELECT DISTINCT rd.especie, sj.departamento, 6 as stintervencion, 40 as aintervencion, 0.97 as fextraccion FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento);"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 2, 1 FROM cintervencionr WHERE stintervencion=6 AND aintervencion=40::numeric(5,3))"
        )


### Model update and run
@auth.requires_membership('users')
def modelupdate():
    """Central page for update. Two tabs
    """
    mmu="/%s/%s/%s" % (request.application, request.controller, 'mmodelupdate')
    amu="/%s/%s/%s" % (request.application, request.controller, 'amodelupdate')
    return dict(mmu=mmu, amu=amu)


@auth.requires_membership('users')
def mmodelupdate():
    import json
    tnames=[]

    trs= [
        TR(
            TD( B( T('Run model without full requirement verification') )),
            TD(
                DIV(

                    SPAN(
                        #Button
                        A(
                            SPAN(I(_class=' icon-repeat icon-black'), T('Run now')),
                            _class='btn btn-small',
                            _onclick="return modelrun();",
                            _id="ubutton"
                        ),
                        IMG(
                            _src="/%s/static/images/pbar_loader.gif" % request.application,
                            _id="pb",
                            _style="display:none;height:10px;"
                        ),
                        #Return labels
                        SPAN(
                            T('Success'),
                            _class="label label-success",
                            _id="sspan",
                            _style="display:none",
                        ),
                        SPAN(
                            T('Fail'),
                            _class="label label-warning",
                            _id="fspan",
                            _style="display:none",
                        ),
                        SPAN(
                            T('Error'),
                            _class="label label-important",
                            _id="espan",
                            _style="display:none",
                        )
                    ),
                    _id="ru",
                    _class="div div-btn div-info",
                    _style="width:240px;"
                )
            )
        )
    ]

    table=TABLE (
        TBODY( trs ),
        _class="table table-striped",
        _id="modelupdate"
    )
    return dict(table=table)


@auth.requires_membership('users')
def amodelupdate():
    return dict()


@auth.requires_membership('users')
@service.json
def modelrun():
    """Run the model
    """
    try:
        from mmodel.mmodel import MModel
        m = MModel(mDatabase=db)
        result = m.run()
        return dict( result=False )
    except Exception as e:
        print "Error: %s" % e
        return dict( result=False )

@auth.requires_membership('users')
def pspecies():
    # Tiene common_filter!
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.especie.id > 0) &
        (db.genero.id==db.especie.genero)
        # (db.genero.cby==auth.user_id)
        )
    dm.gQuery( query )
    dm.actionTableName('especie')
    dm.gFieldId('id')
    dm.gFields( [
        ('especie','genero'),
        ('especie','nombre'),
        ('especie','exc')
        ] )
    dm.gShowId(False)
    dm.showMActions(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('users')
def pregions():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
    query=(
        (db.seccionjudicial.id > 0) &
        (db.seccionjudicial.departamento==db.departamento.id)
        )
    dm.gQuery( query )
    dm.actionTableName('seccionjudicial')
    dm.gFieldId('id')
    dm.gFields( [
        ('departamento','nombre'),
        ('seccionjudicial','nombre'),
        ('seccionjudicial','exc')
        ] )
    dm.gShowId(False)
    dm.showMActions(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())
