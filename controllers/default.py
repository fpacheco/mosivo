# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

def index():
    return dict()

@auth.requires_membership('admin')  
def arreglaBase():    
    db.commit()
    try:
        db.executesql('ALTER TABLE caefectiva ADD CONSTRAINT caefectiva_especie_departamento_ukey UNIQUE (especie,departamento)')
        db.executesql('ALTER TABLE cturno ADD CONSTRAINT cturno_especie_destino_ukey UNIQUE (especie,destino)')
    except:
        db.rollback()
    return dict()
