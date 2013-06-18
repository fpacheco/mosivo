# -*- coding: utf-8 -*-
# From modules directory 
from daplugin.iplugin import IPlugin
# From this directory
from model import DGFModel

class Plugin(IPlugin):
    
    def __init__(self,plugpath):
        super(Plugin, self).__init__( plugpath )
        
   
    def load(self):
        super(Plugin, self).load()
        self.rdb = DGFModel().db()


    def unload(self):        
        super(Plugin, self).unload()   
        # Close db????

       
    def planes(self):
        res = []
        q = self.rdb(
            (self.rdb.Carpetas_P.Codigo != None) &                     
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
                [r.Codigo, r.Nro_Carpeta, r.Longitud, r.Latitud]
            )
        return res