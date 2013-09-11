# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) to local database (mosivo)
"""

@auth.requires_membership('admins')
def insertTUpdated(namea):
    """Insert a record in tupdated table
    Return datetime and number of records in other table
    """
    from datetime import datetime
    un=datetime.now()
    q=db( db['tname']['nombre']==namea )
    if not q.isempty():
        _id=q.select( db['tname']['id'] )[0]['id']
        db['tupdated'].insert(
            fecha=un,
            tname=_id,
            uid=auth.user_id
        )
        uemail=db( db['auth_user']['id']==auth.user_id ).select( db['auth_user']['email'] )[0]['email']
        return (True, un, db(db[namea]['id']>0).count(), uemail)
    else:
        return (False, -1, -1, -1)

@auth.requires_membership('admins')
def tUpdated(namea):
    qq=db( db['tname']['nombre']==namea )
    if not qq.isempty():
        _id=qq.select(db['tname']['id'])[0]['id']
        q=db(
            ( db['tupdated']['tname']==_id ) &
            ( db['tupdated']['uid']==db['auth_user']['id'] )
        )
        if not q.isempty():
            row = q.select(
                db['tupdated']['fecha'],
                db['auth_user']['email'],
                orderby=~db['tupdated']['fecha']
            )
            return (True, row[0]['tupdated']['fecha'], row[0]['auth_user']['email'])
        else:
            return (False, -1, -1)
    else:
        return (False, -100, -100)
