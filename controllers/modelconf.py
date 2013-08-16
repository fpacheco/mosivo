# -*- coding: utf-8 -*-

def dataupdate():
    pass

def modelupdate():
    pass

def mcraleo():
    return dict()

def mcturno():
    form = 1    
    db.cturno.id.readable=False
    query=(
        (db.cturno.id > 0) &
        (db.especie.id==db.cturno.especie) &
        (db.genero.id==db.especie.genero)
    )
    fields = [db.cturno.id, db.genero.nombre, db.cturno.especie, db.cturno.destino, db.cturno.turno]
    headers = {'cturno.id': T('Id'),
        'genero.nombre': T('Género plantado'),
        'cturno.especie': T('Especie plantada'),
        'cturno.destino': T('Destino del monte'),
        'cturno.turno': T('Años hasta el corte'),
        #'links':  T('Acciones'), 
    }    
    default_sort_order=[db.genero.nombre]
    links = [
        lambda row: SPAN(
                    A(I(_class='icon-pencil icon-white'),
                      SPAN(' ',T('Edit')),
                      _class='btn btn-inverse btn-mini',
                      _title=T('Edit this record'),
                      _href=URL(request.controller, 'nedcturno', args=["e", row.cturno.id])
                    ),
                    A(I(_class='icon-remove icon-white'),
                      SPAN(' ',T('Delete')),
                      _class='btn btn-warning btn-mini',
                      _title=T('Delete this record'),
                      _href=URL(request.controller, 'nedcturno', args=["d", row.cturno.id])
                    )
                )             
    ]
    grid = SQLFORM.grid(query=query, fields=fields, headers=headers, orderby=default_sort_order,
        details=False, create=False, deletable=False, editable=False, maxtextlength=64, paginate=25,
        showbuttontext=True, ui='web2py', formstyle='table3cols', _class="web2py_grid", links=links
    )        
    return dict(grid=grid, form=form)


@auth.requires_membership('admin')
def nedcturno():
    """
    new, edit, delete cturno 
    """
    """
    form = SQLFORM(db.yourtable)
    my_extra_element = TR(LABEL('I agree to the terms and conditions'),                       INPUT(_name='agree',value=True,_type='checkbox'))
    form[0].insert(-1,my_extra_element)
    #
    """
    caction=request.args(0)
    if caction=='e':
        print "nedcturno: Edit - %s" % request.args(1)  
        id=int(request.args(1))
        record=db.cturno(id) or redirect(URL('index'))
        form = SQLFORM(db.cturno, record)
    elif caction=='n':
        print "nedcturno: New"
        form = SQLFORM(db.cturno)
    elif caction=='d':
        print "nedcturno: Delete - %s" % request.args(1)
        id=int(request.args(1))
        record=db.cturno(id) or redirect(URL('index'))
        db(db.cturno.id==id).delete()
    else:
        pass    
    if form.process().accepted:
       response.flash = 'form accepted'
    elif form.errors:
       response.flash = 'form has errors'
    return dict(form=form)
    