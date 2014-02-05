# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) to local database (mosivo)
"""

@auth.requires_membership('users')
def updatedInfo(tablename):
    """Numbers of rows in table
    """
    if tablename in db.tables:
        sql = "SELECT tu.fecha, u.email FROM tupdated tu, tname tn, auth_user u " \
            "WHERE tn.nombre='%s' AND tu.tname=tn.id AND u.id=tu.cby AND tu.cby=%i ORDER BY tu.fecha DESC" % (tablename,auth.user_id)
        rows=db.executesql(sql)
        if len(rows)>0:
            return ( True, rows[0][0], rows[0][1] )
        else:
            return (False, 'No info', 'No info')
    else:
        return (False, 'No table', 'No table')

@auth.requires_membership('users')
def deleteTable(tName):
    """Custom delete for tables for this user
    """
    if (tName=='genero') or (tName=='plan') or (tName=='seccionjudicial'):
        db.commit()
        try:
            db(
                (db[tName]['cby']==auth.user_id)
            ).delete()
            return True
        except Exception,e:
            db.rollback()
            print str(e)
            return False
    elif tName=='especie':
        db.commit()
        try:
            sql1 = "DELETE FROM %s WHERE genero" % (tName,)
            sql2 = "SELECT id FROM genero WHERE cby=%i" % (auth.user_id,)
            sql = "%s IN (%s)" % (sql1,sql2)
            db.executesql( sql )
            return True
        except Exception,e:
            db.rollback()
            print str(e)
            return False
    elif tName=='rodald':
        db.commit()
        try:
            sql1 = "DELETE FROM %s WHERE plan" % (tName,)
            sql2 = "SELECT id FROM plan WHERE cby=%i" % (auth.user_id,)
            sql = "%s IN (%s)" % (sql1,sql2)
            db.executesql( sql )
            return True
        except Exception,e:
            db.rollback()
            print str(e)
            return False
    elif tName in ['caefectiva', 'cima', 'ccosecha', 'cbcampo', 'cbcampoe', 'cbindustria', 'cintervencionr', 'cintervenciona']:
        db.commit()
        try:
            sql1 = "DELETE FROM %s WHERE especie" % (tName,)
            sql2 = "SELECT e.id FROM especie e, genero g WHERE e.genero=g.id AND g.cby=%i" % (auth.user_id,)
            sql = "%s IN (%s)" % (sql1,sql2)
            db.executesql( sql )
            return True
        except Exception,e:
            db.rollback()
            print str(e)
            return False
    elif tName in ['cgsuelo', ]:
        db.commit()
        try:
            sql1 = "DELETE FROM %s WHERE sjudicial" % (tName,)
            sql2 = "SELECT id FROM seccionjudicial WHERE cby=%i" % (auth.user_id,)
            sql = "%s IN (%s)" % (sql1,sql2)
            db.executesql( sql )
            return True
        except Exception,e:
            db.rollback()
            print str(e)
            return False
    else:
        return False

@auth.requires_membership('users')
def nRows(tName):
    """Custom numbers of records in tables for that user
    """
    if (tName=='genero') or (tName=='plan'):
        return db(
            (db[ tName ]['cby']==auth.user_id)
        ).count()
    elif tName=='especie':
        return db(
            (db['especie']['id']>0) &
            (db['especie']['genero']==db['genero']['id']) &
            (db['genero']['cby']==auth.user_id)
        ).count()
    elif tName=='rodald':
        return db(
            (db['rodald']['id']>0) &
            (db['rodald']['plan']==db['plan']['id']) &
            (db['plan']['cby']==auth.user_id)
        ).count()
    elif tName in ['caefectiva', 'cima', 'ccosecha', 'cbcampo', 'cbcampoe', 'cbindustria', 'cintervencionr', 'cintervenciona']:
        return db(
            (db[tName]['especie']==db['especie']['id']) &
            (db['especie']['genero']==db['genero']['id']) &
            (db['genero']['cby']==auth.user_id)
        ).count()
    elif tName in ['cgsuelo', ]:
        return db(
            (db[tName]['sjudicial']==db['seccionjudicial']['id']) &
            (db['seccionjudicial']['cby']==auth.user_id)
        ).count()
    else:
        return -1

@auth.requires_membership('users')
def insertTUpdated(namea):
    """Insert a record in tupdated table
    Return datetime and number of records in other table
    """
    from datetime import datetime
    if namea in db.tables:
        un=datetime.now()
        q=db( db['tname']['nombre']==namea )
        if not q.isempty():
            _id=q.select( db['tname']['id'] )[0]['id']
            db['tupdated'].insert(
                fecha=un,
                tname=_id,
                cby=auth.user_id
            )
            return True
        else:
            return False
    else:
        return False

