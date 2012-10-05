# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 09:43:19 2012

@author: geus
"""


class Utils():
    """
    def __init__(self,con):
        self.con = con
        self.cur = con.cursor()
        self.__setCarpetas()
    """
    
    def __init__(self):
        pass
        self.carpetas = [{'id': 1, 'nombre':'Carpeta 1'},{'id': 2, 'nombre':'Carpeta 2'}]
            
    def __setCarpetas(self):
        """Setea las carpetas que hay"""
        self.cursor.execute('SELECT Nro_Carpeta FROM Carpetas_P')
        rows = self.cursor.fetchall()
        if len(rows) > 0:
            self.carpetas = rows
        else:
            self.carpetas = None
            
    def getCarpetas(self):
        """Devuelve las carpetas que hay"""
        return self.carpetas