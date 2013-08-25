# -*- coding: utf-8 -*-

def departamento():
    q = db(
           db.departamento
        ).select(
            db.departamento.ALL
        )

    if len(q) == 0:
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
    if len(q) == 0:
        # Lista de destinos
        destinos = [
            u'Madera sólida',
            'Pulpa',
            u'Energía'
        ]
        db.commit()
        try:
            # Set sequence in departamento
            db.executesql("ALTER SEQUENCE destino_id_seq MINVALUE 0;")
            db.executesql("SELECT setval('destino_id_seq', 0, true);")
            for d in destinos:
                db.destino.insert(nombre = d)
            db.commit()
        except:
            db.rollback()


def dia():
    q = db(
           db.dia
        ).select(
            db.dia.ALL
        )
    if len(q) == 0:
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
        db.commit()
        try:
            # Set sequence in departamento
            db.executesql("ALTER SEQUENCE dia_id_seq MINVALUE 0;")
            db.executesql("SELECT setval('dia_id_seq', 0, true);")
            for d in dias:
                db.dia.insert(nombre=d)
            db.commit()
        except:
            db.rollback()


def genero():
    q = db(
           db.genero
        ).select(
            db.genero.ALL
        )
    if len(q) == 0:
        # Lista de generos
        generos = [
            ('O', 'Acacia'),
            ('E', 'Eucaliptus'),
            ('O', 'Fraxinus'),
            ('M', 'Mezcla'),
            ('A', 'No se define'),
            ('O', 'Patanus'),
            ('P', 'Pinus'),
            ('S', 'Populus'),
            ('O', 'Querqus'),
            ('S', 'Salix'),
            ('O', 'Taxodium'),
        ]
        db.commit()
        try:
            # Set sequence in departamento
            db.executesql("ALTER SEQUENCE genero_id_seq MINVALUE 0;")
            db.executesql("SELECT setval('genero_id_seq', 0, true);")
            for d in generos:
                db.genero.insert(codigo=d[0], nombre=d[1])
            db.commit()
        except:
            db.rollback()


def especie():
    q = db(
           db.especie
        ).select(
            db.especie.ALL
        )

    if len(q) == 0:
        # Set sequence in departamento
        db.executesql("ALTER SEQUENCE especie_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('especie_id_seq', 0, true);")
        # Lista de especies
        especies = [
            # O = 1 Acacia
            (1, 0, 'Sp.'),
            (1, 3, 'Longifolia'),
            # E = 2 Eucalyptus
            (2, 0, 'Sp.'),
            (2, 1, 'Botryoides'),
            (2, 2, 'Camaldulensis (rostrata)'),
            (2, 3, 'Corinocalix'),
            (2, 4, 'Bicostata'),
            (2, 5, 'Diversicolor'),
            (2, 6, 'Globulus ssp. globulus'),
            (2, 7, 'Gomphocephala'),
            (2, 8, 'Grandis'),
            (2, 10, 'Hempholia'),
            (2, 11, 'Leucoxylon'),
            (2, 12, 'Marcarthuri'),
            (2, 13, 'Melliodora'),
            (2, 14, 'Paniculata'),
            (2, 15, 'Punctata'),
            (2, 16, 'Resinifera'),
            (2, 17, 'Robusta'),
            (2, 18, 'Rudis'),
            (2, 19, 'Saligna'),
            (2, 20, 'Smithii'),
            (2, 21, 'Sideroxylon'),
            (2, 22, 'Tereticornis (umbellata)'),
            (2, 23, 'Viminalis'),
            (2, 24, 'Globulus ssp. maidenii'),
            (2, 25, 'Cinerea'),
            (2, 26, 'Grandis + maidenii'),
            (2, 27, 'Bosistoana'),
            (2, 28, 'Dunnii'),
            (2, 29, 'Grandis + saligna'),
            (2, 30, 'Mezcla'),
            (2, 31, 'Ssp. globulus + ssp. maidenii'),
            (2, 32, 'Crebra'),
            (2, 33, 'Nitens'),
            # O = 3 Fraxinus
            (3, 19, 'Sp.'),
            # M = 4 Mezcla
            (4, 0, 'Mezcla'),
            # A = 5 no se define
            (5, 0, 'No se define'),
            # O = 6 Pantanus
            (6, 16, 'Sp.'),
            # P = 7 Pinus
            (7, 0, 'Sp.'),
            (7, 1, 'Canariensis'),
            (7, 2, 'Elliottii'),
            (7, 3, 'Patula'),
            (7, 4, 'Pinaster'),
            (7, 5, 'Radiata'),
            (7, 6, 'Taeda'),
            (7, 7, 'Elliottii + taeda'),
            (7, 8, 'Elliottii + pinaster'),
            (7, 9, 'Mezcla'),
            (7, 10, 'Roxbughii'),
            # S = 8 Populus
            (8, 0, 'Sp.'),
            (8, 1, 'Deltoides'),
            (8, 2, 'X euroamericana 74D'),
            (8, 3, 'X euroamericana I-214'),
            (8, 4, 'X euroamericana 63/51'),
            (8, 7, 'X euroamericana I-15'),
            # O = 9 Querqus
            (9, 21, 'Sp.'),
            # S = 10 Salix
            (10, 5, 'Alba var. coerulea'),
            (10, 6, 'Otros'),
            (10, 8, 'Babylonica x alba cv. 131/25 y 131/27'),
            # O = 11 Taxodium
            (11, 20, 'Distinchum'),
        ]
        for d in especies:
            db.especie.insert(genero=d[0], codigo=d[1], nombre=d[2])
        db.commit()

def seccionjudicial():
    q = db(
           db.seccionjudicial
        ).select(
            db.seccionjudicial.ALL
        )

    if len(q) == 0:
        # Set sequence in departamento
        db.executesql("ALTER SEQUENCE seccionjudicial_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('seccionjudicial_id_seq', 0, true);")
        # Lista de secciones por departamento
        # RFPV: Revisar
        secciones = [
            # (departamento, de, hasta)
            (1, 1, 20),
            (2, 1, 20),
            (3, 1, 20),
            (4, 1, 20),
            (5, 1, 20),
            (6, 1, 20),
            (7, 1, 20),
            (8, 1, 20),
            (9, 1, 20),
            (10, 1, 20),
            (11, 1, 20),
            (12, 1, 20),
            (13, 1, 20),
            (14, 1, 20),
            (15, 1, 20),
            (16, 1, 20),
            (17, 1, 20),
            (18, 1, 20),
            (19, 1, 20)
        ]
        for d in secciones:
            for s in xrange(d[1], d[2]):
                db.seccionjudicial.insert(departamento=d[0], nombre=s)
        db.commit()

def cosecha():
    q = db(
           db.cosecha
        ).select(
            db.cosecha.ALL
        )

    if len(q) == 0:
        # Set sequence in departamento
        db.executesql("ALTER SEQUENCE cosecha_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('cosecha_id_seq', 0, true);")
        # Lista de cosechas
        cosechas = [
            #(nombre, descripcion)
            ('Mecanizada', 'Harvester-Forwarder o Feller-Skidder'),
            ('Semimecanizada', 'Intermedio'),
            ('Manual', 'Motosierra')
        ]
        for d in cosechas:
            db.cosecha.insert(nombre=d[0], descripcion=d[1])
        db.commit()

def tiporesiduoforestal():
    q = db(
           db.tiporesiduoforestal
        ).select(
            db.tiporesiduoforestal.ALL
        )

    if len(q) == 0:
        # Set sequence in departamento
        db.executesql("ALTER SEQUENCE tiporesiduoforestal_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('tiporesiduoforestal_id_seq', 0, true);")
        # Lista de tipos
        tipo = [
            ('Aserrío'),
            ('Biruta'),
            ('Corteza'),
            ('Costaneros'),
            ('Despuntes'),
            ('Otros'),
            ('Polvos')
        ]
        db.commit()
        try:
            for d in tipo:
                db.tiporesiduoforestal.insert(nombre=d[0])
            db.commit()
        except:
            db.rollback()


def tipocoeficiente():
    q = db(
            db.tipocoeficiente
        ).select(
            db.tipocoeficiente.ALL
        )

    if len(q) == 0:
        # Set sequence in departamento
        db.executesql("ALTER SEQUENCE tipocoeficiente_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('tipocoeficiente_id_seq', 0, true);")
        # Lista de coef
        tipo = [
            #(nombre)
            ('Área'),
            ('Rodal'),
        ]
        db.commit()
        try:
            for d in tipo:
                db.tipocoeficiente.insert(nombre=d[0])
            db.commit()
        except:
            db.rollback()


# Populate mosivo database
departamento()
destino()
dia()
genero()
especie()
seccionjudicial()
cosecha()
tipocoeficiente()
tiporesiduoforestal()

