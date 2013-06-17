# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) database to local database (mosivo)
"""
from daplugin.pluginmanager import PluginManager

class RemoteData(object):
    """Only one plugin at time
    """
    
    def __init__(self,plugdir):
        self.pm = PluginManager()
        if len(plugdir)>0:            
            self.pm.setPluginsDir( plugdir )
        self.__loadPluginId = None
        self.__plugin = None
        
        
    def pluginsMetadata(self):
        return ( self.pm.pluginsMetadata() )
    
    
    def loadPlugin(self,plugid):
        """Only one plugin at time
        """
        print "RemoteData.loadPlugin: %s" % plugid
        self.pm.unloadAll()
        self.pm.loadPlugin(plugid)
        self.__loadPluginId = plugid
        self.__plugin = self.pm.plugin(plugid)
    
    def planes(self):
        self.__plugin.planes()
        
    
    def unloadPlugin(self):
        self.pm.unloadPlugin( self.__loadPluginId )
        self.__loadPluginId = None
        self.__plugin = None

        
            
    
    
          
