# coding: utf8
# try something like

from getdatafromdgf.model import DGFModel
dgfdb = DGFModel().rdb

def index():
    urls = ["","","","",""]
    return dict()


# @auth.requires_membership('admin')
def departamentos():
    q = dgfdb(
        dgfdb.Deptos
    ).select(
        dgfdb.Deptos.Nombre,
        orderby=dgfdb.Deptos.Nombre
    )
    return dict( grid=q )
    #return dict( grid=SQLFORM.grid(dgfdb.Deptos) )


def carpetas_p():
    return dict( grid=SQLFORM.grid(dgfdb.Carpetas_P) )


def planes_pro():
    return dict( grid=SQLFORM.grid(dgfdb.Planes_Pro) )


def planes():
    return dict( grid=SQLFORM.grid(dgfdb.Planes) )


def plantas():
    return dict( grid=SQLFORM.grid(dgfdb.Plantas) )


def propietarios():
    return dict( grid=SQLFORM.grid(dgfdb.Propietarios) )    


def registro():
    return dict( grid=SQLFORM.grid(dgfdb.Registro) )

