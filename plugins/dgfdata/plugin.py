# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) database to local database (mosivo)
"""
from daplugin.iplugin import IPlugin
from model import DGFModel

class Plugin(IPlugin):
    
    def __init__(self):                
        super(Plugin, self).__init__()
        print "dgfdata plugin __init__"
        
   
    def activate(self):
        super(Plugin, self).activate()
        self.rdb = DGFModel().db()
        print "dgfdata plugin activate"


    def deactivate(self):
        super(Plugin, self).deactivate()        
        # Close db????
        print "dgfdata plugin deactivate"

        
    def planes(self):
        res = []
        q = self.rdb(
            (self.rdb.Carpetas_P.Nro_Carpeta != None) & 
            (self.rdb.Carpetas_P.Longitud != None) &
            (self.rdb.Carpetas_P.Latitud != None) &
            (self.rdb.Carpetas_P.Baja != None ) &             
            (self.rdb.Carpetas_P.Baja != 0)            
        ).select(
            self.rdb.Carpetas_P.Codigo,
            self.rdb.Carpetas_P.Nro_Carpeta,
            self.rdb.Carpetas_P.Longitud,
            self.rdb.Carpetas_P.Latitud,
            orderby=self.rdb.Carpetas_P.Nro_Carpeta
        )
        for r in q:            
            res.append(
                [r.Codigo, r.Nro_Carpeta,r.Longitud,r.Latitud]
            )
        return res

