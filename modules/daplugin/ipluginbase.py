# -*- coding: utf-8 -*-


class IPluginBase(object):
    """Base Interface plugin class

    This class declare minimal interface for plugin implementation 
    """


    def __init__(self):
        self.__readPluginInfo()
        self.__isLoaded = False


    def __readPluginInfo(self):
        print "IPluginBase.__readPluginInfo"
        from os import listdir
        from os.path import isfile, basename, abspath 
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
                self.minmosver = config.get(self.id,'minmosver')
                self.dirname = basename( abspath('.') )     
 

    def activate(self):
        self.__isLoaded = True


    def deactivate(self):
        self.__isLoaded = False

    
    def info(self):
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
        return ( self.__isLoaded == True )    