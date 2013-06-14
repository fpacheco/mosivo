# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) database to local database (mosivo)
"""

class IPlugin(object):
    id = None
    name = None
    version = None
    category = None
    description=None
    author = None
    email = None
    webpage = None
        
    def __init__(self):
        if self.name and self.version and self.author and self.email:
            self.activate()
            self.deactivate()
    
    def info(self):
        return (self.id, self.name, self.version, self.category, self.description, self.author, self.email, self.webpage)
    
    def activate(self):
        pass
    
    def deactivate(self):
        pass   

    """    
    def getDepartamentos(self):
        pass

    def getGeneros(self):
        pass

    def getEspecies(self):
        pass

    def getSuelos(self):
        pass
    """

    def planes(self):
        pass
    
    def rodalesd(self):
        pass
    
    def ubicacionrodalesd(self):
        pass
    
    def gruposuelorodalesd(self):
        pass
    
    def turnorodalesd(self):
        pass
    
    def raleorodalesd(self):
        pass
    
    def rodalesp(self):
        pass
    
    def ubicacionrodalesp(self):
        pass
    
    def gruposuelorodalesp(self):
        pass
    
    def turnorodalesp(self):
        pass
    
    def raleorodalesp(self):
        pass       