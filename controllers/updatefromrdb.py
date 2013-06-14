# -*- coding: utf-8 -*-

@auth.requires_membership('admin')
def index():
    """Default
    """
    return dict()


@auth.requires_membership('admin')
def update():
    """Update remote data to local database
    """
    from getremotedata.updatefromrdb import UpdateFromRDB
    from getremotedata.model import  DGFModel
    dgfdb = DGFModel().rdb
    uProc = UpdateFromRDB(db,dgfdb)
    uProc.uPlan()
    uProc.uRodalp()
    # print uProc.dCodToId()
    return dict()
