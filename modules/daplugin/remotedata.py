# -*- coding: utf-8 -*-
from pluginmanager import PluginManager

class RemoteData(object):
    """Get data from remote data source
    
    .. warning:: Only one plugin at time
    """

    
    def __init__(self,plugdir):
        self.pm = PluginManager()
        if len(plugdir)>0:            
            self.pm.setPluginsDir( plugdir )
        self.__loadPluginId = None
        self.__plugin = None
        
        
    def pluginsMetadata(self):
        """Get metadata for all plugins 
        """
        return ( self.pm.pluginsMetadata() )
    
    
    def loadPlugin(self,plugid):
        """Load plugin by his id
        
        :param plugid: id string for the plugin
        :type plugid: str                
        """
        self.pm.unloadAll()
        self.pm.loadPlugin(plugid)
        self.__loadPluginId = plugid
        # self.__plugin = self.pm.loadedPlugins()[0]
        self.__plugin = self.pm.loadedPlugin(plugid)


    def loadedPlugins(self):
        """Get metadata for all plugins
        
        :returns: List of loaded plugins
        :rtype: IPlugin         
        """        
        return self.pm.loadedPlugins()

    
    def planes(self):
        """Get data for table planes in MoSiVo database
        
        :returns: List Planes table data
        :rtype: list         
        """        
        return self.__plugin.planes()        


    def rodalesd(self):
        """Get data for table planes in MoSiVo database
        
        :returns: List Planes table data
        :rtype: list         
        """        
        return self.__plugin.rodalesd()

    
    def ubicacionrodalesd(self):
        """Get data for table planes in MoSiVo database
        
        :returns: List Planes table data
        :rtype: list         
        """        
        return self.__plugin.ubicacionrodalesd()    


    def gruposuelorodald(self):
        """Get data for table planes in MoSiVo database
        
        :returns: List Planes table data
        :rtype: list         
        """        
        return self.__plugin.gruposuelorodald()


    def raleorodalesd(self):
        """Get data for table planes in MoSiVo database
        
        :returns: List Planes table data
        :rtype: list         
        """        
        return self.__plugin.raleorodalesd()

    
    def turnorodalesd(self):
        """Get data for table planes in MoSiVo database
        
        :returns: List Planes table data
        :rtype: list         
        """        
        return self.__plugin.turnorodalesd()
 
    
    def rodalesp(self):
        """Get data for table planes in MoSiVo database
        
        :returns: List Planes table data
        :rtype: list         
        """        
        return self.__plugin.rodalesp()

    
    def ubicacionrodalesp(self):
        """Get data for table planes in MoSiVo database
        
        :returns: List Planes table data
        :rtype: list         
        """        
        return self.__plugin.ubicacionrodalesp()    


    def gruposuelorodalp(self):
        """Get data for table planes in MoSiVo database
        
        :returns: List Planes table data
        :rtype: list         
        """        
        return self.__plugin.gruposuelorodalp()


    def raleorodalesp(self):
        """Get data for table planes in MoSiVo database
        
        :returns: List Planes table data
        :rtype: list         
        """        
        return self.__plugin.raleorodalesp()

    
    def turnorodalesp(self):
        """Get data for table planes in MoSiVo database
        
        :returns: List Planes table data
        :rtype: list         
        """        
        return self.__plugin.turnorodalesp()
    
    def unloadPlugin(self):
        """Unload loaded plugin         
        """        
        self.pm.unloadPlugin( self.__loadPluginId )
        self.__loadPluginId = None
        self.__plugin = None
