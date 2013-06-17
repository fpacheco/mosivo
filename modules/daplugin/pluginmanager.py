# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) database to local database (mosivo)
"""

class PluginManager(object):
    """Manager plugin class

    This class manage plugins 
    """

    def __init__(self):
        self.__pluginsDir = None
        self.__loadedPlugins = []
        self.__pluginsMetadata = dict()           


    def __readPluginsMetadata(self):
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
                            ret = dict( name=name,
                                version=version,
                                category=category,
                                description=description,
                                author=author,
                                email=email,
                                minmosver=minmosver,
                                dirname=dirname                                     
                            )
                            print ret 
                            self.__pluginsMetadata[plugid] = ret 



    def pluginsMetadata(self):
        """Plugins metadata for all plugin in plugins directory
        """
        return ( self.__pluginsMetadata )


    def setPluginsDir(self, pluginsdir):
        """Set plugins directory
        """        
        from os.path import isdir
        if isdir( pluginsdir ):
            self.__pluginsDir = pluginsdir
            self.__readPluginsMetadata()

    
    def pluginsDir(self):
        """Get plugins directory
        """        
        return self.__pluginsDir
    
    def pluginMetadata(self, plugid):
        """Get metadata for plugid plugin
        """                
        if self.__pluginsMetadata.has_key(plugid):
            return ( self.__pluginsMetadata[plugid] )

    def loadPlugin(self, plugid):
        """Load the plugin
        """        
        # _temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], -1)
        # eggs = _temp.eggs
        # saus = _temp.sausage
        # import importlib
        # foo = importlib.import_module('home.fpacheco.Descargas.web2py.applications.mosivo.plugins.dgfdata')
        from os.path import basename
        import sys
        print "PluginManager.loadPlugin.syspath: %s" % sys.path
        sys.path.append( '/home.net/fpacheco/Descargas/web2py.git/applications/mosivo/plugins/dgfdata' )
        
        """        
        pbp = basename( self.__pluginsDir )
        print "PluginManager.loadPlugin.ppath: %s" % self.__pluginsMetadata[plugid]
        ppath= "%s.%s.%s.%s.%s" % ( 'applications', 'mosivo', pbp, self.__pluginsMetadata[plugid]['dirname'], 'plugin')        
        print "PluginManager.loadPlugin.ppath: %s" % ppath        
        #_ip = __import__( ppath, globals(), locals(), ['plugin'], -1)
        _ip = __import__( ppath )
        """
        _ip = __import__( "plugin" )
        print _ip
        #module = __import__(module_name)
        #class_ = getattr(module, class_name)
        #instance = class_()
        class_ = getattr(_ip, 'Plugin')        
        _plugin = class_()
        # _ip.Plugin()
        if not _plugin in self.__loadedPlugins:
            _plugin.load()
            self.__loadedPlugins.append( _plugin )
 
    def loadedPlugins(self):
        return ( self.__loadedPlugins )    


    def loadedPluginsKeys(self):
        """List of key of loaded plugins 
        """
        res = []
        for k in self.__pluginsInfo:            
            res.append( k )
        return res
   
                
    def isLoaded(self,plugid):
        for p in self.__loadedPlugins:
            if p['id'] == plugid:
                return (True)
        return (False)    

                
    def unloadAll(self):
        """Unload all loaded plugins
        """
        for p in self.__loadedPlugins:
            p.unload()
        self.__loadedPlugins = []


    def unloadPlugin(self, plugid):
        for p in self.__loadedPlugins:
            if p['id'] == plugid:
                p.unload()
                self.__loadedPlugins.remove( p )
                return