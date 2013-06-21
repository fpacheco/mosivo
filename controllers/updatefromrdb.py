# -*- coding: utf-8 -*-
if 0:
    import static
    
    
### @auth.requires_membership('admin')
def index():
    """Default
    """
    from daplugin.remotedata import RemoteData
    rd = RemoteData( request.folder + "plugins" )
    rd.loadPlugin('dgfdata')        
    rd.planes()    
    return dict()


### @auth.requires_membership('admin')
def update():
    """Update remote data to local database
    """
    print dict()

