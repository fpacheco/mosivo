# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 09:43:19 2012

@author: geus
"""

class Utils():

    def __init__(self,con):
        self.con = con
        self.cur = con.cursor()
        self.__setCarpetas()

    def __setCarpetas(self):
        """Setea las carpetas que hay"""
        self.cur.execute('SELECT Nro_Carpeta FROM Carpetas_P')
        rows = self.cur.fetchall()
        data = []
        for row in rows:
            data.append(row[0])
            
        if len(rows) > 0:
            self.carpetas = data
        else:
            self.carpetas = None
            
    def getCarpetas(self):
        """Devuelve las carpetas que hay"""
        return self.carpetas
