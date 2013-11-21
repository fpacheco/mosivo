# -*- coding: utf-8 -*-

@auth.requires_membership('users')
def all():
    from plugin_dm.datamanager import DataManager
    dm=DataManager(database=db)
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

    dm.gQuery( query )
    dm.actionTableName('destinointervrodald')
    dm.gFieldId('id')
    dm.gFields( 
        [
            ('destinointervrodald','id'),
            ('plan','ncarpeta'),
            ('intervrodald','rodal'),
            ('departamento','nombre'),
            ('seccionjudicial','nombre'),
            ('genero','nombre'),
            ('especie','nombre'),
            ('tipointervencion','nombre'),
            ('intervrodald','adisp'),
            ('destinointervrodald','destino'),
            ('destinointervrodald','mcmcc'),
        ] 
    )
    dm.gShowId(False)
    dm.showMActions(False)
    return dict(toolbar=dm.toolBar(), grid=dm.grid())
    
