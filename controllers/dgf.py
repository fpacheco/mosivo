# coding: utf8
# try something like
def departamentos():
    return dict( grid=SQLFORM.grid(dgfdb.Deptos) )

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

