# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) database to local database (mosivo)
"""

class IPlugin(object):
    id = None

    def __init__(self):
        self.isLoaded = False
        self.__readPluginInfo()

    def __readPluginInfo(self):
        from os import listdir
        from os.path import isfile, isdir, join, basename, abspath 
        from ConfigParser import ConfigParser
      
        ldir = listdir( '.' )
        ldir.sort()
        for f in ldir:
            if isfile( f ) and f.endswith('mosivoplugin'):                
                self.id = f.split('.')[0]                            
                config = ConfigParser()
                config.read( f )
                self.name = config.get(self.id,'name')
                self.version = config.get(self.id,'version')
                self.category = config.get(self.id,'category')
                self.description = config.get(self.id,'description')
                self.author = config.get(self.id,'author')
                self.email = config.get(self.id,'email')
                self.webpage = config.get(self.id,'webpage')
                self.dirname = basename( basename( abspath(f) ) )

        
    def load(self):
        if self.name and self.version and self.author and self.email:
            try:
                self.activate()
                self.isLoaded = True                
            except:
                print "Can not load module (id: %s, name: %s, version: %s). " % (self.id, self.name, self.version)            
            

    def unload(self):
        if self.isLoaded:
            try:            
                self.deactivate()
                self.isLoaded = False
            except:
                print "Can not unload module (id: %s, name: %s, version: %s). " % (self.id, self.name, self.version)
                
    def info(self):
        return (self.id, self.name, self.version, self.category, self.description, self.author, self.email, self.webpage)

    def activate(self):
        pass

    def deactivate(self):
        pass

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
