# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) to local database (mosivo)
"""

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

def nRows(tName):
    """Numbers of records in tbles for that user
    """
    if (tName=='genero') or (tName=='plan'):
        return db(
            db[ tName ]['id']>0
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
    else:
        return -1


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

