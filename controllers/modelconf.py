# -*- coding: utf-8 -*-
# Data acction for the data
dataActions=['new','edit','delete','deleteAll']

@auth.requires_login()
def dataupdate():
    pass

@auth.requires_login()
def modelupdate():
    pass

@auth.requires_login()
def mcraleo():
    return dict()

@auth.requires_login()
def mcturno():
    db.cturno.id.readable=True
    query=(
        (db.cturno.id > 0) &
        (db.especie.id==db.cturno.especie) &
        (db.genero.id==db.especie.genero)
    )
    # RFPV - Must have this (<tr id=>) !!!!!!
    ## db(db['cturno']['id'] > 3).select()
    field_id = db.cturno.id
    fields = [db.cturno.id, db.genero.nombre, db.cturno.especie, db.cturno.destino, db.cturno.turno]    
    headers = {'cturno.id': T('Id'),
        'genero.nombre': T('Género plantado'),
        'cturno.especie': T('Especie plantada'),
        'cturno.destino': T('Destino del monte'),
        'cturno.turno': T('Años hasta el corte'),
        #'links':  T('Acciones'), 
    }    
    default_sort_order=[db.genero.nombre]
    actionURL='/%s/%s/%s' % (request.application, request.controller, 'nedcturno.load')
   
    ## RFPV - Todo si es usaurio comun no hay links
    links = [
        lambda row: SPAN(
                    A(I(_class='icon-pencil icon-white'),
                      _class='btn btn-inverse btn-mini',
                      _title=T('Edit this record'),
                      #_href=URL(request.controller, 'nedcturno', args=["e", row.cturno.id]),
                      _onclick="return editDialogShow('%s',%d);" % (actionURL, row.cturno.id)                      
                    ),
                    A(I(_class='icon-remove icon-white'),
                      _class='btn btn-warning btn-mini',
                      _title=T('Delete this record'),
                      #_href=URL(request.controller, 'nedcturno', args=["d", row.cturno.id]),
                      _onclick="return deleteDialogShow('%s',%d);" % (actionURL, row.cturno.id)
                    )
                )             
    ]
    grid = SQLFORM.grid(query=query, fields=fields, headers=headers, links=links, field_id=field_id, orderby=default_sort_order, 
        details=False, create=False, deletable=False, editable=False, maxtextlength=64, paginate=20,
        showbuttontext=False, ui='web2py', formstyle='table3cols', _class="web2py_grid",
    )        
    return dict(grid=grid, actionURL=actionURL)

@auth.requires_membership('admin')
def nada():
    """
    form = SQLFORM(db.yourtable)
    my_extra_element = TR(LABEL('I agree to the terms and conditions'),                       INPUT(_name='agree',value=True,_type='checkbox'))
    form[0].insert(-1,my_extra_element)
    #
    """
    # request.get_vars.id --> HTTP GET
    # request.post_vars.id --> HTTP POST    
    #record=db['cturno'](1)
    pass

@auth.requires_membership('admin')
def nedcturno():
    """
    new, edit, delete cturno. All variables come from POST 
    """
    dataAction=request.post_vars.dataAction
    if dataAction=='new':
        print "nedcturno: new"
        form = SQLFORM(db.cturno, _id="cturno-new")
        dai = INPUT(_name='dataAction',id='cturno_dataAction', value='new', _type='hidden')
        form.insert(-1,dai)
    elif dataAction=='edit':        
        id=request.post_vars.dataId
        print "nedcturno: edit - %s" % id
        record=db.cturno(id) or redirect(URL('default','index'))
        form = SQLFORM(db.cturno, record, showid=False, _id="cturno-edit")
        dai = INPUT(_name='dataAction',id='cturno_dataAction', value='edit', _type='hidden')
        form.insert(-1,dai)
        did = INPUT(_name='dataId',id='cturno_dataId', value=id, _type='hidden')
        form.insert(-1,did)        
    elif dataAction=='delete':        
        # Just delete, dont show form
        id=request.post_vars.dataId
        if db(db.cturno.id==id).isempty():
            response.flash = T('No record deleted')
            if request.ajax:
                return response.json( {'result': False, 'msg':T('No record with this %s' % id)}  )            
        else:
            db(db.cturno.id==id).delete()
            response.flash = T('Record deleted')
            if request.ajax:
                return response.json( {'result': True } )
    elif dataAction=='deleteAll':
        if db(db.cturno.id>0).isempty():
            response.flash = T('No record deleted')
            if request.ajax:
                return response.json( {'result': False, 'msg':T('No records found') }  )        
        else:
            # WARNING: Delete all record in the table!!!
            db.commit()
            try:
                db(db.cturno.id>0).delete()
                db.executesql("SELECT setval('cturno_id_seq', 1, true)")
                response.flash = T('Records deleted')
                if request.ajax:
                    return response.json( {'result': True } )
            except:
                db.rollback()
    else:
        redirect(URL('default','index'))
    
    #Remove submit button it's ajax
    if request.ajax:        
        submit = form.element('input',_type='submit')
        submit['_style'] = 'display:none;'     
    else:
        pass
    
    if form.process().accepted:
        response.flash = T('Form accepted')
        if request.ajax:
            return response.json( {'result': True } )
    elif form.errors:
        response.flash = T('Form has errors')
        if request.ajax:
            return response.json( {'result': False, 'msg':form.errors} )        
    else:
        response.flash = T('Please fill the form')
    return dict(form=form)
    