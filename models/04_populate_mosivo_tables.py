# -*- coding: utf-8 -*-

def departamento():
    q = db(
           db.departamento
        ).select(
            db.departamento.ALL
        )

    if len(q)==0:
        # Set sequence in departamento
        db.executesql("ALTER SEQUENCE departamento_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('departamento_id_seq', 0, true);")
        # Lista de departamentos
        departamentos = [
            'Artigas',
            'Canelones',
            'Cerro Largo',
            'Colonia',
            'Durazno',
            'Flores',
            'Florida',
            'Lavalleja',
            'Maldonado',
            'Montevideo',
            u'Paysandú',
            u'Río Negro',
            'Rivera',
            'Rocha',
            'Salto',
            u'San José',
            'Soriano',
            u'Tacuarembó',
            'Treinta y Tres'
        ]
        for d in departamentos:
            db.departamento.insert(nombre = d)
        db.commit()

def destino():
    q = db(
           db.destino
        ).select(
            db.destino.ALL
        )

    if len(q)==0:
        # Set sequence in departamento
        db.executesql("ALTER SEQUENCE destino_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('destino_id_seq', 0, true);")
        # Lista de destinos
        destinos = [
            u'Madera sólida',
            'Pulpa'
        ]
        for d in destinos:
            db.destino.insert(nombre = d)
        db.commit()

def dia():
    q = db(
           db.dia
        ).select(
            db.dia.ALL
        )

    if len(q)==0:
        # Set sequence in departamento
        db.executesql("ALTER SEQUENCE dia_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('dia_id_seq', 0, true);")
        # Lista de destinos
        dias = [
            'Domingo',
            'Lunes',
            'Martes',
            'Miércoles',
            'Jueves',
            'Viernes',
            'Sábado'
        ]
        for d in dias:
            db.dia.insert(nombre = d)
        db.commit()


# Populate
departamento()
destino()
dia()
