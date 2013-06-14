# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) database to local database (mosivo)
"""
if 0:
    from static import *

@auth.requires_membership('admin')
def index():
    pass

# @auth.requires_membership('admin')
def cturno():
    db.cturno.id.readable=False        
    grid = SQLFORM.smartgrid(db.cturno, user_signature=False)
    return dict(grid=grid)


# @auth.requires_membership('admin')
def cima():
    db.cima.id.readable=False
    grid=SQLFORM.smartgrid(db.cima, user_signature=False)
    return locals()

# @auth.requires_membership('admin')
def caefectiva():
    db.caefectiva.id.readable=False
    grid=SQLFORM.smartgrid(db.caefectiva, user_signature=False)
    return locals()

# @auth.requires_membership('admin')
def cfdestino():
    db.cfdestino.id.readable=False
    grid=SQLFORM(db.cfdestino, user_signature=False)
    return locals()

# @auth.requires_membership('admin')
def cbcampo():
    db.cbcampo.id.readable=False
    grid=SQLFORM.smartgrid(db.cbcampo, user_signature=False)
    return locals()
