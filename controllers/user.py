# coding: utf8
u"""Controlador que permite gestionar los datos básicos al usuario"""

@auth.requires_membership('users')
def profile():
    u"""Permite que el usaurio vea y modifique sus datos personales"""
    redirect( URL('default','user',args='profile') )

@auth.requires_membership('users')
def change_password():
    u"""Permite que el usaurio cambie su contraseña"""
    redirect( URL('default','user',args='change_password') )
