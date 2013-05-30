# -*- coding: utf-8 -*-
def index():
    """Default
    """
    return dict()
    
def update():
    """Update remote data to local database
    """
    from getremotedata.updatefromrdb import UpdateFromRDB
    from getremotedata.model import  DGFModel
    dgfdb = DGFModel().rdb
    uProc = UpdateFromRDB(db,dgfdb)
    uProc.uDepartamento()
    uProc.uGenero()
    print uProc.gCodToId()
    uProc.uEspecie()
    uProc.uCarpeta()
    # print uProc.dCodToId()
    return dict()