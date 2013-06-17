# -*- coding: utf-8 -*-
from ipluginbase import IPluginBase

class IPlugin(IPluginBase):
    """Interface plugin class

    This class declare minimal interface for plugin implementation 
    """


    def __init__(self):
        super(IPluginBase, self).__init__() 


    def load(self):
        """Plugin load interface
        
        Here you can declare your database connection and others. Don't forget
        to call self.activate()  
        """
        if not self.isLoaded() and self.id and self.name and self.version and self.minmosver:
            try:
                self.activate()
            except:
                print "Can't load module (id: %s, name: %s, version: %s). " % (self.id, self.name, self.version)            
            

    def unload(self):
        """Plugin unload interface
        
        Here you can delete your database connection and others. Don't forget
        to call self.deactivate()  
        """        
        if self.isLoaded():
            try:            
                self.deactivate()
            except:
                print "Can't unload module (id: %s, name: %s, version: %s). " % (self.id, self.name, self.version)
                

    def planes(self):
        """Retrieves planes data from remote database
    
        Returns:
            A list of list [id, numerocarpeta,longitude,latitude]. 
            For example:            
            
            [
            [55, 3125, -59.654321,-32.123456,],
            [56, 3126, -58.654321,-33.123456,],
            others,
            ]
        """
        pass


    def rodalesd(self):
        """Retrieves declared forest from remote database
    
        Returns:
            A list of list [idplan, idespecie, anioplantado, areaafectacion, iddestino]. 
            For example:            
            
            [
            [55, 45, 2008, 345.22, 3],
            [55, 47, 2012, 123.98, 2],
            others,
            ]
        """        
        pass


    def ubicacionrodalesd(self):
        """Retrieves declared forest from remote database
    
        Returns:
            A list of list [idplan, idespecie, anioplantado, areaafectacion, iddestino]. 
            For example:            
            
            [
            [55, 45, 2008, 345.22, 3],
            [55, 47, 2012, 123.98, 2],
            others,
            ]
        """        
        pass


    def gruposuelorodalesd(self):
        """Retrieves declared forest from remote database
    
        Returns:
            A list of list [idplan, idespecie, anioplantado, areaafectacion, iddestino]. 
            For example:            
            
            [
            [55, 45, 2008, 345.22, 3],
            [55, 47, 2012, 123.98, 2],
            others,
            ]
        """        
        pass


    def turnorodalesd(self):
        """Retrieves declared forest from remote database
    
        Returns:
            A list of list [idplan, idespecie, anioplantado, areaafectacion, iddestino]. 
            For example:            
            
            [
            [55, 45, 2008, 345.22, 3],
            [55, 47, 2012, 123.98, 2],
            others,
            ]
        """        
        pass


    def raleorodalesd(self):
        """Retrieves declared forest from remote database
    
        Returns:
            A list of list [idplan, idespecie, anioplantado, areaafectacion, iddestino]. 
            For example:            
            
            [
            [55, 45, 2008, 345.22, 3],
            [55, 47, 2012, 123.98, 2],
            others,
            ]
        """        
        pass


    def rodalesp(self):
        """Retrieves projected forest from remote database. See
        """        
        pass


    def ubicacionrodalesp(self):
        """Retrieves projected forest from remote database. See
        """        
        pass


    def gruposuelorodalesp(self):
        """Retrieves projected forest from remote database. See
        """        
        pass


    def turnorodalesp(self):
        """Retrieves projected forest from remote database. See
        """        
        pass


    def raleorodalesp(self):
        """Retrieves projected forest from remote database. See
        """
        pass
