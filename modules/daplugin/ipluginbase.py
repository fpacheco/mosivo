# -*- coding: utf-8 -*-


class IPluginBase(object):
    """Base Interface plugin class

    This class declare minimal interface for plugin implementation 
    """


    def __init__(self, dirpath):
        """Class initialization
        """        
        self.__dirPath = dirpath
        self.__isLoaded = False
        self.__readPluginInfo()        
        

    def __readPluginInfo(self):
        """Class initialization
        """        
        from os import listdir
        from os.path import isdir, isfile, basename, abspath, join 
        from ConfigParser import ConfigParser
        if len(self.__dirPath)>0 and isdir(self.__dirPath):
            ldir = listdir( self.__dirPath )
            ldir.sort()
            for f in ldir:
                ff = join(self.__dirPath, f)
                if isfile( ff ) and f.endswith('mosivoplugin'):                
                    self.id = f.split('.')[0]                             
                    config = ConfigParser()                    
                    config.read( ff )
                    self.name = config.get(self.id,'name')
                    self.version = config.get(self.id,'version')
                    self.category = config.get(self.id,'category')
                    self.description = config.get(self.id,'description')
                    self.author = config.get(self.id,'author')
                    self.email = config.get(self.id,'email')
                    self.webpage = config.get(self.id,'webpage')
                    self.minmosver = config.get(self.id,'minmosver')
                    self.dirname = basename( abspath('.') )
                    return      


    def activate(self):
        """Class initialization
        """        
        self.__isLoaded = True


    def deactivate(self):
        """Class initialization
        """        
        self.__isLoaded = False

    
    def metadata(self):
        """Class initialization
        """        
        ret = {
            'id': self.id,
            'name': self.name,
            'version': self.version,
            'category': self.category,
            'description': self.description,
            'author': self.author,
            'email': self.email,
            'webpage': self.webpage,
            'minmosver': self.minmosver,
            'dirname': self.dirname
        }
        return ( ret )

    
    def isLoaded(self):
        """Class initialization
        """        
        return ( self.__isLoaded )