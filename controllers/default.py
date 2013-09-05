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
        db.executesql('ALTER TABLE cintervencionr ADD CONSTRAINT cintervencionr_teda_ukey UNIQUE(especie, departamento, aintervencion)')
        db.executesql('ALTER TABLE cdintervencionr ADD CONSTRAINT cdintervencionr_cd_ukey UNIQUE(cintervencionr,destino)')
        db.executesql('ALTER TABLE cintervenciona ADD CONSTRAINT cintervenciona_teda_ukey UNIQUE(tcoeficiente, especie, departamento, aintervencion)')
        db.executesql('ALTER TABLE cdintervenciona ADD CONSTRAINT cdintervenciona_cd_ukey UNIQUE(cintervenciona,destino)')
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

def pygal():
    # Si lo quiero embebido
    # <embed src="http://localhost/yourapp/default/plot_pygal.svg" type="image/svg+xml" />
    # otra
    # SELECT c.cod_depto,p.ano_dec,sum(p.ha_dec) FROM planes p, planes_pro pp, carpetas_p c WHERE p.codigo_plan_pro=pp.codigo AND pp.codigo_cp==c.codigo GROUP BY c.cod_depto,p.ano_dec;
    import pygal
    from pygal.style import CleanStyle
    response.headers['Content-Type']='image/svg+xml'
    bar_chart = pygal.Bar(style=CleanStyle) # Then create a bar graph object
    bar_chart.title = 'Superficie plantada por departamento (Ha)'
    rdb = DAL('sqlite://dgf_database.db', migrate_enabled=False, migrate=False)
    rows=rdb.executesql("SELECT c.cod_depto,sum(p.ha_dec) FROM planes p, planes_pro pp, carpetas_p c WHERE p.codigo_plan_pro=pp.codigo AND pp.codigo_cp==c.codigo GROUP BY c.cod_depto")
    bar_chart.x_labels = [ r[0] for r in rows ]
    bar_chart.add(u'Áreas totales', [ r[1] for r in rows ] )
    # bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) # Add some values
    return bar_chart.render()