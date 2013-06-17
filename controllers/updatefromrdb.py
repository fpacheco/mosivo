# -*- coding: utf-8 -*-
if 0:
    import static
    
    
### @auth.requires_membership('admin')
def index():
    """Default
    """
    from remotedata import RemoteData
    print "request.folder: %s" % request.folder
    rd = RemoteData( request.folder + "plugins" )
    print "Plugins: %s" % rd.pluginsMetadata()
    rd.loadPlugin('dgfdata')
    rd.planes()
    return dict()


### @auth.requires_membership('admin')
def update():
    """Update remote data to local database
    """
    print dict()

