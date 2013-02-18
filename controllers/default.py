# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

def index():
    return dict()
    
   
def carpetas():    
    #from gluon.debug import dbg
    #dbg.set_trace() # stop here!
    utils = local_import('utils' , reload=True).Utils(mssqlcon)
    return "Carpetas: %s" % utils.getCarpetas()
    
def getCarpetas():
    page = request.get_vars['page']
    limit = request.get_vars['rows']
    sidx = request.get_vars['sidx']
    sord = request.get_vars['sord']
    ret = []
    utils = local_import('utils' , reload=True).Utils(mssqlcon)
    #utils = local_import('utils' , reload=True).Utils()
    carpetas = utils.getCarpetas() 
    for carpeta in carpetas:
        cell = {'id':carpeta['id'], 'cell': [carpeta['nombre'], carpeta['id']]}
        ret.append(cell)
    #cell = {'cell': [parcela.nombre, round(volumenHtcc,6), round(volumenHtsc,6) , round(volumenHccc,6), round(volumenHcsc,6)]}
    #ret.append(cell)
    rows = 10
    if request.get_vars['rows']:
        rows = int(request.get_vars['rows'])
    import gluon.contrib.simplejson
    return gluon.contrib.simplejson.dumps({'total':len(ret)/rows, 'page':page, 'records':len(ret), 'rows': ret})
    
def showCarpeta():
    if request.get_vars['id']:
        proyecto = local_import('msv/proyecto' , reload=True).Proyecto(mssqlcon, int(request.get_vars['id']))
        proyecto = local_import('msv/proyecto' , reload=True).Proyecto(int(request.get_vars['id']))
        return dict(proyectado=proyecto.getBProyectado().data, plantado=proyecto.getBPlantado().data)
        #proy = [{'id': '1', 'nombre': 'proy1', 'raleo': '[2008, 2010, 2012]'}]
        #plant = [{'id': '1', 'nombre': 'plant1'}]
        #return dict(id=request.get_vars['id'],proyectado=proy, plantado=plant)
        
def getProyecto():   
    if request.get_vars['id']:
        proyecto = local_import('msv/proyecto' , reload=True).Proyecto(mssqlcon, int(request.get_vars['id']))
        proyecto = local_import('msv/proyecto' , reload=True).Proyecto(int(request.get_vars['id']))

def testFolder():
    folder_id = -1
    if request.get_vars['folder_id']:
        folder_id = int(request.get_vars['folder_id'])
    folder = local_import('folder' , reload=True).Folder(mssqlcon.cursor(), folder_id)
    if request.get_vars['query'] == "location":
        return folder.location()
    elif request.get_vars['query'] == "registries":
        return folder.registries()
    elif request.get_vars['query'] == "cuts":
        return folder.cuts()
    elif request.get_vars['query'] == "justiceSection":
        return folder.justiceSection()
    elif request.get_vars['query'] == "policeSection":
        return folder.policeSection()
    elif request.get_vars['query'] == "cadastralSection":
        return folder.cadastralSection()

def toggleFooter():
    if request.post_vars['action']:
        if request.post_vars['action'] == 'show':
            session.showFooter = True
        elif request.post_vars['action'] == 'hide':
            session.showFooter = False

