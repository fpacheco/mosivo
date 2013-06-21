# -*- coding: utf-8 -*-
class PluginManager(object):
    """Manager plugin class

    This class manage plugins 
    """

    def __init__(self):
        """Class initialization
        """
        self.__pluginsDir = None
        self.__loadedPlugins = []
        self.__pluginsMetadata = dict()           


    def __readPluginsMetadata(self):
        """Private method that read metadata for a plugin
        """        
        from os import listdir
        from os.path import isfile, isdir, join, basename 
        from ConfigParser import ConfigParser
      
        if len(self.__pluginsDir)>0:
            lpdir = listdir( self.__pluginsDir )
            lpdir.sort()
            for d in lpdir:
                adir = join(self.__pluginsDir,d)
                if isdir( adir ):
                    for f in listdir( adir ):
                        af = join( adir,f )
                        bfn = basename( af )
                        if isfile( af ) and bfn.endswith('mosivoplugin'):
                            dirname = d
                            plugid = f.split('.')[0]
                            print "PluginManager.__readPluginsMetadata:%s (%s)" % (plugid,dirname)                            
                            config = ConfigParser()
                            config.read( af )
                            name = config.get(plugid,'name')
                            version = config.get(plugid,'version')
                            category = config.get(plugid,'category')
                            description = config.get(plugid,'description')
                            author = config.get(plugid,'author')
                            email = config.get(plugid,'email')
                            webpage = config.get(plugid,'webpage')
                            minmosver = config.get(plugid,'minmosver')
                            ret = dict( 
                                name=name,
                                version=version,
                                category=category,
                                description=description,
                                author=author,
                                email=email,
                                minmosver=minmosver,
                                dirname=dirname                                     
                            )
                            self.__pluginsMetadata[plugid] = ret 



    def pluginsMetadata(self):
        """Plugins metadata for all plugin in plugins directory
        """
        return ( self.__pluginsMetadata )


    def setPluginsDir(self, pluginsdir):
        """Set plugins directory

        :param pluginsdir: String with the path of the plugins directory
        :type pluginsdir: str        
        """        
        from os.path import isdir
        if isdir( pluginsdir ):
            self.__pluginsDir = pluginsdir
            self.__readPluginsMetadata()

    
    def pluginsDir(self):
        """Get plugins directory

        :returns: The path of the plugins directories.
        :rtype: str 
        
        :Example:        
        
        >>> import template
        >>> a = MainClass()
        >>> a.function2(1,1,1)
        2
        
        .. note:: can be useful to emphasize important feature
        .. seealso:: :class:`MainClass2`
        .. warning:: arg2 must be non-zero.
        .. todo:: check that arg2 is non zero.        
        """        
        return self.__pluginsDir

    
    def pluginMetadata(self, plugid):
        """Get metadata for plugid plugin
        
        :param plugid: id string for the plugin
        :type plugid: str
                
        Returns:
            Metadata for this plugin.        
        """                
        if self.__pluginsMetadata.has_key(plugid):
            return ( self.__pluginsMetadata[plugid] )


    def loadPlugin(self, plugid):
        """Load a plugin by his id

        :param plugid: id string for the plugin
        :type plugid: str        
        """        
        from os.path import abspath, join 
        import sys
        
        # Add plugin directory to python path
        pluginsPath = abspath('.') + '/applications/mosivo/plugins'
        sys.path.append( pluginsPath )
        
        #Dynamic import Plugin class
        _mod = "%s.plugin" % plugid 
        _ip = __import__( _mod, fromlist=['Plugin'] )
        class_ = getattr(_ip, 'Plugin')
        _plugin = class_( join(self.__pluginsDir, plugid) )
        if not _plugin in self.__loadedPlugins:
            try:
                _plugin.load()
                self.__loadedPlugins.append( _plugin )
            except:
                print "Load error: Can't load plugin!" 
 
 
    def loadedPlugin(self,plugid):
        """Get a plugin from his id

        :param plugid: id string for the plugin
        :type plugid: str

        :returns: The plugin
        :rtype: IPlugin
        """        
        for p in self.__loadedPlugins:
            if p.id == plugid:
                return p
    
    
    def loadedPlugins(self):
        """Get a list of loaded plugins
        
        Returns:
            A list of loaded plugins        
        """
        return self.__loadedPlugins 


    def loadedPluginsKeys(self):
        """List of key of loaded plugins

        Returns:
            A list of keys of loaded plugins         
        """
        res = []
        for k in self.__loadedPlugins:
            res.append( k )
        return res
   
                
    def isLoaded(self,plugid):
        """List of key of loaded plugins
        
        :param plugid: id string for the plugin
        :type plugid: str

        :returns: True if plugin is loaded.
        :rtype: bool
        
        """
        for p in self.__loadedPlugins:
            if p.id == plugid:
                return (True)
        return (False)    

                
    def unloadAll(self):
        """Unload all loaded plugins
        """
        for p in self.__loadedPlugins:
            p.unload()
        self.__loadedPlugins = []


    def unloadPlugin(self, plugid):
        """Unload a plugin by his id
        
        :param plugid: id string for the plugin
        :type plugid: str
                  
        """        
        for p in self.__loadedPlugins:
            if p.id == plugid:
                p.unload()
                self.__loadedPlugins.remove( p )
                return