# -*- coding: utf-8 -*-
"""This module update relevant data from remote database (DGF) database to local database (mosivo)
"""

class PluginManager(object):

    def __init__(self):
        self.__pluginsDir = str()
        self.__pluginsInfo = {}

    def __readPluginsInfo(self):
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
                            config = ConfigParser()
                            config.read( af )
                            name = config.get(plugid,'name')
                            version = config.get(plugid,'version')
                            category = config.get(plugid,'category')
                            description = config.get(plugid,'description')
                            author = config.get(plugid,'author')
                            email = config.get(plugid,'email')
                            webpage = config.get(plugid,'webpage')
                            self.__pluginsInfo[plugid] = {
                                'name': name,                                
                                'version': version,
                                'category': category,
                                'dirname': dirname, 
                                'description': description,
                                'author': author,
                                'email': email,
                                'webpage': webpage,
                                'plugin': None                                                
                            }


    def pluginsInfo(self):
        return self.__pluginsInfo


    def setPluginsDir(self, plugPath):
        from os.path import isdir
        if isdir( plugPath ):            
            self.__pluginsDir = plugPath
            self.__readPluginsInfo()

    
    def pluginsDir(self):
        return self.__pluginsDir
    
    def pluginInfo(self, plugid):        
        if self.__pluginsInfo.has_key(plugid):
            return self.__pluginsInfo[plugid]

    def loadPlugin(self, plugid):
        if self.__pluginsInfo.has_key(plugid):
            #_temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], -1)
            #eggs = _temp.eggs
            #saus = _temp.sausage
            #import importlib
            #foo = importlib.import_module('home.fpacheco.Descargas.web2py.applications.mosivo.plugins.dgfdata')
            from os.path import basename
            pbp = basename( self.__pluginsDir )             
            ppath = "%s.%s" % (pbp,self.__pluginsInfo[plugid].dirname)
            
            print "PluginManager.loadPlugin.ppath: %s" % ppath
            
            plug = __import__(ppath)
            self.__pluginsInfo[plugid]['plugin'] = plug.Plugin()
            self.__pluginsInfo[plugid]['plugin'].load()
 
    def plugin(self,plugid):
        if self.__pluginsInfo.has_key(plugid) and self.isLoaded(plugid):
            return self.__pluginsInfo[plugid]['plugin']
                
    def isLoaded(self,plugid):
        if self.__pluginsInfo.has_key(plugid):
            return ( self.__pluginsInfo[plugid]['plugin'] == None )
        
    def loadedPlugins(self):
        """List of key of loaded __pluginsInfo 
        """
        res = []
        for p in self.__pluginsInfo:
            if self.isLoaded(p):
                res.append(p)
        return res

    def unloadAll(self):
        """Unload all loaded plugins
        """
        kk = self.loadedPlugins()
        """
        if len(kk)>0:
            for k in kk:
                self.unloadPlugin(k)        
        """
        for k in kk:
            self.unloadPlugin(k)        

        
    def unloadPlugin(self, plugid):
        if self.__pluginsInfo.has_key(plugid) and self.isLoaded(plugid):
            self.__pluginsInfo[plugid]['plugin'].unload()
            self.__pluginsInfo[plugid]['plugin'] = None