# -*- coding: utf-8 -*-

@auth.requires_login()
def mcima():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db,tablename='cima')
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
    return dict(toolbar=dm.toolBar(), grid=dm.grid())
    
