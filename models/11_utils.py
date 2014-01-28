# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) to local database (mosivo)
"""
def nRows(tablename):
    """Numbers of rows in table
    """
    if tablename in db.tables:
        return db(db[tablename]['id']>0).count()
    else:
        return -1


def updatedInfo(tablename):
    """Numbers of rows in table
    """
    if tablename in db.tables:
        sql = "SELECT tu.fecha, u.email FROM tupdated tu, tname tn, auth_user u " \
            "WHERE tn.nombre='%s' AND tu.tname=tn.id AND u.id=tu.cby ORDER BY tu.fecha DESC" % tablename
        rows=db.executesql(sql)
        if len(rows)>0:
            return ( True, rows[0][0], rows[0][1] )
        else:
            return (False, 'No info', 'No info')
    else:
        return (False, 'No table', 'No table')


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

