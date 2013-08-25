# -*- coding: utf-8 -*-
### required - do no delete
def user():
    return dict(form=auth())

def download():
    return response.download(request,db)

def call():
    return service()
### end requires

def index():
    return dict()

@auth.requires_membership('admin')
def estableceConstraints():
    """Establece Constraints sobre la base de datos
    """
    res = False

    db.commit()
    try:
        db.executesql('ALTER TABLE caefectiva ADD CONSTRAINT caefectiva_especie_departamento_ukey UNIQUE (especie,departamento)')
        db.executesql('ALTER TABLE cima ADD CONSTRAINT cima_especie_departamento_ukey UNIQUE (especie,departamento)')
        db.executesql('ALTER TABLE cbcampo ADD CONSTRAINT cbcampo_egdc_ukey UNIQUE (especie,gruposuelo,destino,cosecha)')
        db.executesql('ALTER TABLE cbindustria ADD CONSTRAINT cbindustria_especie_ukey UNIQUE (especie, trf)')
        db.executesql('ALTER TABLE cintervencion ADD CONSTRAINT cintervencion_teda_ukey UNIQUE(tcoeficiente, especie, departamento, aintervencion)')
        db.executesql('ALTER TABLE cdintervencion ADD CONSTRAINT cdintervencion_cd_ukey UNIQUE(cintervencion,destino)')
        db.executesql('ALTER TABLE destinointervrodald ADD CONSTRAINT destinointervrodald_id_ukey UNIQUE(irodal,destino)')
        db.executesql('ALTER TABLE destinointervrodalp ADD CONSTRAINT destinointervrodalp_id_ukey UNIQUE(irodal,destino)')
        db.executesql('ALTER TABLE especie ADD CONSTRAINT especie_gn_ukey UNIQUE(genero,nombre)')
        db.executesql('ALTER TABLE gruposuelorodald ADD CONSTRAINT gruposuelorodald_rg_ukey UNIQUE(rodal,gsuelo)')
        db.executesql('ALTER TABLE gruposuelorodalp ADD CONSTRAINT gruposuelorodalp_rg_ukey UNIQUE(rodal,gsuelo)')
        db.executesql('ALTER TABLE seccionjudicial ADD CONSTRAINT seccionjudicial_dn_ukey UNIQUE(departamento,nombre)')
        res = True
    except:
        db.rollback()

    return dict()
