# -*- coding: utf-8 -*-

@auth.requires_membership('admins')
def nOfRows():
    """Number of rows in table
    """
    tName=request.post_vars.tName
    data={ 'nRows': nRows(tName) }
    return data


@auth.requires_membership('admins')
def updatedData():
    """Number of rows in table
    """
    tName=request.post_vars.tName
    ui = updatedInfo(tName)
    data={ 'updatedOn': ui[1], 'updatedBy': ui[2] }
    return data


@auth.requires_membership('admins')
def configupdatefromrdb():
    """Central page for update. Two tabs
    """
    mu="/%s/%s/%s" % (request.application, request.controller, 'mupdatefromrdb')
    au="/%s/%s/%s" % (request.application, request.controller, 'aupdatefromrdb')
    return dict(mu=mu, au=au)


@auth.requires_membership('admins')
def aupdatefromrdb():
    """Automatic update page
    """
    pass

@auth.requires_membership('admins')
def mupdatefromrdb():
    """Manual update page
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
                        db( db[ tnames[cont] ]['id']>0 ).count(), 
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
        _id="modelverify"
    )
    return dict(table=table)


@auth.requires_membership('admins')
def update():
    import json
    tnames=['genero','especie','plan','rodald']
    result=False
    res=[]
    try:
        updWhat=request.post_vars.updWhat
        from getdatafromdgf.updatefromrdb import UpdateFromRDB
        u = UpdateFromRDB(mDatabase=db, inDGF=False)
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
            return { 'result': insertTUpdated(updWhat) }
        else:
            return { 'result': False }
    except Exception as e:
        print "Error: %s" % e

@auth.requires_membership('admins')
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


@auth.requires_membership('admins')
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
@auth.requires_membership('admins')
def mdestino():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='destino')
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('admins')
def mtiporesiduoforestal():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='tiporesiduoforestal')
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('admins')
def mcosecha():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='cosecha')
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('admins')
def mtipointervencion():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='tipointervencion')
    dm.gShowId(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())
###


## Begin manage coefficients
@auth.requires_membership('admins')
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


@auth.requires_membership('admins')
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


@auth.requires_membership('admins')
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
        ('cintervencionr','tintervencion'),
        ('cintervencionr','aintervencion'),
        ('cintervencionr','fextraccion')
        ] )
    dm.gShowId(False)
    dm.showDActions(True)
    dm.rDetailsURL( "/%s/%s/%s.load" % (request.application, request.controller ,'mcdintervencionr') )
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('admins')
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
        ('cintervenciona','tintervencion'),
        ('cintervenciona','aintervencion'),
        ('cintervenciona','fextraccion')
        ] )
    dm.gShowId(False)
    dm.showDActions(True)
    dm.rDetailsURL( "/%s/%s/%s.load" % (request.application, request.controller ,'mcdintervenciona') )
    return dict(toolbar=dm.toolBar(), grid=dm.grid())


@auth.requires_membership('admins')
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


@auth.requires_membership('admins')
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



@auth.requires_membership('admins')
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


@auth.requires_membership('admins')
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


@auth.requires_membership('admins')
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


@auth.requires_membership('admins')
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

@auth.requires_membership('admins')
def loadDefaults():
    # Coeficients para area efectiva
    if db(db['caefectiva']['id']>0).isempty():
        db.executesql(
            "INSERT INTO caefectiva(especie,departamento,aefectiva) " \
            "(SELECT DISTINCT rd.especie, sj.departamento, 0.65 as aefectiva FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento);"
        )
    # Coeficientes para ima
    if db(db['cima']['id']>0).isempty():
        db.executesql(
            "INSERT INTO cima(especie,departamento,ima) " \
            "(SELECT DISTINCT rd.especie, sj.departamento, 20.0 as ima FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento);"
        )
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
            "INSERT INTO cintervencionr(especie,departamento,tintervencion,aintervencion,fextraccion) " \
            "(SELECT DISTINCT rd.especie, sj.departamento, 1 as tintervencion, 3 as aintervencion, 0.3 as fextraccion FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento);"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 2, 1 FROM cintervencionr WHERE tintervencion=1 AND aintervencion=3::numeric(5,3))"
        )        

        # 2
        db.executesql(
            "INSERT INTO cintervencionr(especie,departamento,tintervencion,aintervencion,fextraccion) " \
            "(SELECT DISTINCT rd.especie, sj.departamento, 1 as tintervencion, 8 as aintervencion, 0.3 as fextraccion FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento);"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 1, 0.8 FROM cintervencionr WHERE tintervencion=1 AND aintervencion=8::numeric(5,3))"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 2, 0.2 FROM cintervencionr WHERE tintervencion=1 AND aintervencion=8::numeric(5,3))"
        )

        # 3                 
        db.executesql(
            "INSERT INTO cintervencionr(especie,departamento,tintervencion,aintervencion,fextraccion) " \
            "(SELECT DISTINCT rd.especie, sj.departamento, 1 as tintervencion, 15 as aintervencion, 0.3 as fextraccion FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento);"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 1, 0.5 FROM cintervencionr WHERE tintervencion=1 AND aintervencion=15::numeric(5,3))"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 2, 0.5 FROM cintervencionr WHERE tintervencion=1 AND aintervencion=15::numeric(5,3))"
        )

        # 4                 
        db.executesql(
            "INSERT INTO cintervencionr(especie,departamento,tintervencion,aintervencion,fextraccion) " \
            "(SELECT DISTINCT rd.especie, sj.departamento, 2 as tintervencion, 20 as aintervencion, 1.00 as fextraccion FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento);"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 1, 0.8 FROM cintervencionr WHERE tintervencion=2 AND aintervencion=20::numeric(5,3))"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 2, 0.2 FROM cintervencionr WHERE tintervencion=2 AND aintervencion=20::numeric(5,3))"
        )

        # 5        
        db.executesql(
            "INSERT INTO cintervencionr(especie,departamento,tintervencion,aintervencion,fextraccion) " \
            "(SELECT DISTINCT rd.especie, sj.departamento, 3 as tintervencion, 40 as aintervencion, 0.97 as fextraccion FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento);"
        )
        db.executesql(
            "INSERT INTO cdintervencionr(cintervencionr,destino,fdestino) (SELECT id, 2, 1 FROM cintervencionr WHERE tintervencion=3 AND aintervencion=40::numeric(5,3))"
        )        
        
