# -*- coding: utf-8 -*-

if 0:
    import static

def addUsersAndGropups():
    if db(db['auth_group']['id']>0).isempty():
        db.executesql("ALTER SEQUENCE auth_group_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('auth_group_id_seq', 0, true);")
        db.auth_group.insert(
            #id=1,
            role='admins',
            description='Administrators',
        )
        db.auth_group.insert(
            #id=2,
            role='users',
            description='Users',
        )
        db.auth_group.insert(
            #id=3,
            role='eusers',
            description='External users',
        )
    if db(db['auth_user']['id']>0).isempty():
        db.executesql("ALTER SEQUENCE auth_user_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('auth_user_id_seq', 0, true);")
        db.auth_user.insert(
            #id=1,
            first_name='FAdministrator',
            last_name='LAdministrator',
            email='admin@admin.com',
            password=db.auth_user.password.validate('12admin12')[0]
        )
        db.auth_user.insert(
            #id=2,
            first_name='FUser',
            last_name='LUser',
            email='user@user.com',
            password=db.auth_user.password.validate('12user12')[0]
        )
        db.auth_user.insert(
            #id=3,
            first_name='FEuser',
            last_name='LEuser',
            email='euser@euser.com',
            password=db.auth_user.password.validate('12euser12')[0]
        )
    if db(db['auth_membership']['id']>0).isempty():
        db.auth_membership.insert(
            user_id=1,
            group_id=1
        )
        db.auth_membership.insert(
            user_id=1,
            group_id=2
        )
        db.auth_membership.insert(
            user_id=2,
            group_id=2
        )
        db.auth_membership.insert(
            user_id=3,
            group_id=3
        )

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
    """No cby
    """
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


def seccionjudicial():
    if auth.user_id:
        q = db(
               (db.seccionjudicial.id>0) &
               (db.seccionjudicial.cby == auth.user_id)
            ).select(
                db.seccionjudicial.ALL
            )

        if len(q) == 0:
            # Set sequence in departamento
            # db.executesql("ALTER SEQUENCE seccionjudicial_id_seq MINVALUE 0;")
            # db.executesql("SELECT setval('seccionjudicial_id_seq', 0, true);")

            # Lista de secciones por departamento
            # RFPV: Revisar
            secciones = [
                # (departamento, de, hasta)
                (1, 1, 25),
                (2, 1, 25),
                (3, 1, 25),
                (4, 1, 25),
                (5, 1, 25),
                (6, 1, 25),
                (7, 1, 25),
                (8, 1, 25),
                (9, 1, 25),
                (10, 1, 25),
                (11, 1, 25),
                (12, 1, 25),
                (13, 1, 25),
                (14, 1, 25),
                (15, 1, 25),
                (16, 1, 25),
                (17, 1, 25),
                (18, 1, 25),
                (19, 1, 25)
            ]
            for d in secciones:
                for s in xrange(d[1], d[2]):
                    db.seccionjudicial.insert(departamento=d[0], nombre=s)
            db.commit()
    else:
        pass


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
    """No cby
    """
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
            u'Aserrín',
            'Viruta',
            'Corteza',
            'Costaneros',
            'Despuntes',
            'Otros',
            'Polvos'
        ]
        db.commit()
        try:
            for d in tipo:
                print d[0]
                db.tiporesiduoforestal.insert(nombre=d)
            db.commit()
        except:
            print "error"
            db.rollback()


def tipointervencion():
    """No cby
    """
    q = db(
            db.tipointervencion
        ).select(
            db.tipointervencion.ALL
        )

    if len(q) == 0:
        # Set sequence in departamento
        db.executesql("ALTER SEQUENCE tipointervencion_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('tipointervencion_id_seq', 0, true);")
        # Lista de coef
        tipo = [
            'Raleo',
            'Tala rasa',
            'Rebrote'
        ]
        db.commit()
        try:
            for d in tipo:
                db.tipointervencion.insert(nombre=d)
            db.commit()
        except:
            db.rollback()


def stintervencion():
    q = db(
            db.stintervencion
        ).select(
            db.stintervencion.ALL
        )

    if len(q) == 0:
        # Set sequence in departamento
        db.executesql("ALTER SEQUENCE stintervencion_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('stintervencion_id_seq', 0, true);")
        # Lista de coef
        tipo = [
            [1,'Raleo Tipo I'],
            [1,'Raleo Tipo II'],
            [1,'Raleo Tipo III'],
            [1,'Raleo Tipo IV'],
            [2,'Tala Rasa'],
            [3,'Rebrote'],
        ]
        db.commit()
        try:
            for d in tipo:
                db.stintervencion.insert(tintervencion=d[0],nombre=d[1])
            db.commit()
        except:
            db.rollback()


def gruposuelo():
    q = db(
        db.gruposuelo
    ).select(
        db.gruposuelo.ALL
    )
    if len(q) == 0:
        # Set sequence in departamento
        db.executesql("ALTER SEQUENCE gruposuelo_id_seq MINVALUE 0;")
        db.executesql("SELECT setval('gruposuelo_id_seq', 0, true);")
        # Lista de coef
        """
        tipo = [
            '1.10a',
            '1.10b',
            '1.11a',
            '1.11b',
            '1.12',
            '1.20',
            '1.21',
            '1.22',
            '1.23',
            '1.24',
            '1.25',
            '2.10',
            '2.11a',
            '2.11b',
            '2.12',
            '2.13',
            '2.14',
            '2.20',
            '2.21',
            '2.22',
            '3.10',
            '3.11',
            '3.12',
            '3.13',
            '3.14',
            '3.15',
            '3.2',
            '3.30',
            '3.31',
            '3.40',
            '3.41',
            '3.50',
            '3.51',
            '3.52',
            '3.53',
            '3.54',
            '03.10',
            '03.11',
            '03.2',
            '03.3',
            '03.40',
            '03.41',
            '03.51',
            '03.52',
            '03.6',
            'B03.1',
            'G03.10',
            'G03.11',
            'G03.21',
            'G03.22',
            'G03.3',
            '4.1',
            '4.2',
            '5.01a',
            '5.01b',
            '5.01c',
            '5.02a',
            '5.02b',
            '5.3',
            '5.4',
            '5.5',
            '6.1/1',
            '6.1/2',
            '6.1/3',
            '6.2',
            '6.3',
            '6.4',
            '6.5',
            '6.6',
            '6.7',
            '6.8',
            '6.9',
            '6.10a',
            '6.10b',
            '6.11',
            '6.12',
            '6.13',
            '6.14',
            '6.15',
            '6.16',
            '6.17',
            '7.1',
            '7.2',
            '7.31',
            '7.32',
            '7.33',
            '7.41',
            '7.42',
            '07.1',
            '07.2',
            '8.1',
            '8.02a',
            '8.02b',
            '8.3',
            '8.4',
            '8.5',
            '8.6',
            '8.7',
            '8.8',
            '8.9',
            '8.10',
            '8.11',
            '8.12',
            '8.13',
            '8.14',
            '8.15',
            '8.16',
            '9.1',
            '9.2',
            '9.3',
            '9.41',
            '9.42',
            '9.5',
            '9.6',
            '9.7',
            '9.8',
            '9.9',
            '09.1',
            '09.2',
            '09.3',
            '09.4',
            '09.5',
            'S09.10',
            'S09.11',
            'S09.20',
            'S09.21',
            'S09.22',
            '10.1',
            '10.2',
            '10.3',
            '10.4',
            '10.5',
            '10.6a',
            '10.6b',
            '10.7',
            '10.8a',
            '10.8b',
            '10.9',
            '10.10',
            '10.11',
            '10.12',
            '10.13',
            '10.14',
            '10.15',
            '10.16',
            'D10.1',
            'D10.2',
            'D10.3',
            'G10.1',
            'G10.2',
            'G10.3',
            'G10.4',
            'G10.5',
            'G10.6a',
            'G10.6b',
            'G10.7',
            'G10.8',
            'G10.9',
            'G10.10',
            'S10.10',
            'S10.11',
            'S10.12',
            'S10.13',
            'S10.20',
            'S10.21',
            '11.1',
            '11.2',
            '11.3',
            '11.4',
            '11.5',
            '11.6',
            '11.7',
            '11.8',
            '11.9',
            '11.10',
            '12.10',
            '12.11',
            '12.12',
            '12.13',
            '12.20',
            '12.21',
            '12.22',
            '13.1',
            '13.2',
            '13.31',
            '13.32',
            '13.4',
            '13.5',
        ]
        """
        tipo = [
            '1',
            '2',
            '3',
            '03',
            'B03',
            'G03',
            '4',
            '5',
            '6',
            '7',
            '07',
            '8',
            '9',
            '09',
            'S09',
            '10',
            'D10',
            'G10',
            'S10',
            '11',
            '12',
            '13',
        ]
        db.commit()
        try:
            for d in tipo:
                db.gruposuelo.insert(nombre=d)
                db.commit()
        except:
            db.rollback()


def tname():
    q = db(
           db.tname
        ).select(
            db.tname.ALL
        )
    if len(q) == 0:
        # Lista de destinos
        tnames = [
            'genero',
            'especie',
            'plan',
            'rodald',
            'ubicacionrodald'
        ]
        db.commit()
        try:
            # Set sequence in departamento
            db.executesql("ALTER SEQUENCE tname_id_seq MINVALUE 0;")
            db.executesql("SELECT setval('tname_id_seq', 0, true);")
            for t in tnames:
                db.tname.insert(nombre = t)
            db.commit()
        except:
            db.rollback()


# Populate mosivo database
addUsersAndGropups()
departamento()
destino()
dia()
cosecha()
tipointervencion()
stintervencion()
tiporesiduoforestal()
gruposuelo()
tname()
if auth.user_id:
    seccionjudicial()
