# -*- coding: utf-8 -*-
u"""En este módulo se establece el menu de la aplicación

    :TODO: recorrer menu por arbol
"""

# For develop only
# if DEVELOP_MODE:
from gluon import *

# El menu es una lista de tuplas. Cada tupla:
# (Nombre, Actual, url, [ ... sub-menu ... ])
# el submenus es:
# (Nombre, Actual, url, [ ... sub-sub-menus ... ])

M_PUBLIC = 0
M_USER = 100
M_ADMIN = 200

class MenuNode():
    u"""Estructura basica de nodo del menu de la aplicación"""
    def __init__(self,mALevel,mName,mContro,mFunc,mArgs):
        u"""Inicialización de  la clase

        :param mALevel: Nivel de acceso al menu
        :mAlevel type: int
        :param mName: Nombre del menu
        :mName type: str
        :param mContro: Controlador del enlace
        :mContro type:str
        :param mFunc: Funcion del controlador
        :type mContro:str
        :param mArgs: Argumentos del controlador
        :type mArgs:str
        """
        self.malevel = mALevel
        self.mname = mName
        self.mcontro = mContro
        self.mfunc = mFunc
        self.margs = mArgs

    def aLevel(self):
        """Devuelve el nievel de acceso del menu"""
        return self.malevel

    def mNode(self):
        """ """
        return T(self.mname),URL(self.mcontro,self.mfunc)==URL(),URL(self.mcontro,self.mfunc,args=self.margs)

class Menu():
    """ """
    def __init__(self,menuList):
        pass

response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description

# Las tres funciones siguientes estan mal
def menuItem(name,contro,fun):
    """ Temporal"""
    return T(name),URL(contro,fun)==URL(),URL(contro,fun)

def createMenuItems(menuType,menuList,parent=0):
    u"""Esta función es un utilitario que genera un nuevo item en el menu"""
    print "----createMenuList: %d,%s" % (menuType,menuList)
    for m in menuList:
        if ( m[0]<=menuType ):
            if ( len(m[4])==0 ):
                return (
                            T( m[1] ),
                            URL( m[2],m[3] )==URL(),
                            URL( m[2],m[3] ),
                            []
                        )
            else:
                if ( m[0]<=menuType ) and ( len(m[4])>0 ):
                    return (
                        T( m[1] ),
                        URL( m[2],m[3] )==URL(),
                        URL( m[2],m[3] ),
                        [ createMenuItems(menuType, m[4]), ]
                    )


def createMenu(menuList):
    u"""Crea el menú de la aplicación en base a estrucutra de listas"""
    mType = -1
    #    if auth.is_logged_in() and auth.has_membership('administrator',auth.user.id):
    #        mType=2
    #    elif auth.is_logged_in():
    #        mType=1
    #    else:
    #        mType=0
    #    return createMenuItems(mType,menuList)
    if auth.is_logged_in() and auth.has_membership('admin',auth.user.id):
        return menuAdmin
    elif auth.is_logged_in():
        return menuUser
    else:
        return menuPublic

# Menu format: ( type,name,controller,function,[submenus] ) 
menu = [
    ( M_PUBLIC,'Home','default','index',
        [
        ]
    ),
    ( M_USER,'Queries','queries','index',
        [
            ( M_USER,'Water','queries','water',[] ),
            ( M_USER,'Soil','queries','soil',[] ),
            ( M_USER,'Vegetation','queries','vegetation',[] ),
            ( M_USER,'Fauna','queries','fauna',[] ),
            ( M_USER,'Non-wood','queries','nonwood',[] ),
            ( M_USER,'Environmental problems','queries','eviron',[] ),
        ]
    ),
    ( M_ADMIN,'Load Data','data','loadData',
        [
        ]
    ),
    ( M_USER,'User','user','index',
        [
            ( 1,'User data','user','data',[] )
        ]
    ),
    ( M_ADMIN,'Administration','admin','index',
        [
            ( M_ADMIN,'Users','admin','users',[] ),
            ( M_ADMIN,'Statistics','admin','stats',[] ),
        ]
    ),
    ( M_PUBLIC,'About','about','index',
        [
        ]
    ),
    ( M_PUBLIC,'Help','help','index',
        [
            ( M_PUBLIC,'Basic help','help','appbasic',[] ),
            ( M_USER,'App manual','help','appmanual',[] ),
            ( M_USER,'System documentation','help','sysmanual',[] ),
        ]
    ),
]

menuAdmin = [
    ( T('Home'), URL('default','index')==URL, URL('default','index'),[] ),
    ( T('Queries'), URL('queries','index')==URL(), URL(),
        [    
            ( T('Native forest'),URL('queries','nforest')==URL(), URL('queries','nforest'),[] ),
            ( T('Planted forest'),URL('queries','pforest')==URL(), URL('queries','pforest'),[] ),  
            ( T('Forest'),URL('queries','affor')==URL(), URL('queries','affor'),[] ),  
            ( T('Non-wood products'), URL('queries','nonwood')==URL, URL('queries','nonwood'),[] ),    
            ( T('Soil'),URL('queries','soil')==URL(), URL('queries','soil'),[] ),
            ( T('Fauna'), URL('queries','fauna')==URL(), URL('queries','fauna'),[] ),
            ( T('Flora'), URL('queries','flora')==URL(), URL('queries','flora'),[] ),
            ( T('Vegetation cover'), URL('queries','vegetation')==URL(), URL('queries','vegetation'), [] ),
            ( T('Water'), URL('queries','water')==URL(), URL('queries','water'),[] ),           
            ( T('Forest Overview'), URL('queries','foverview')==URL(), URL('queries','foverview'),[] ),    
            ( T('Relief'),URL('queries','relief')==URL(), URL('queries','relief'),[] ),        
            ( T('Environmental problems'),URL('queries','eviron')==URL(), URL('queries','environ'),[] ),
            ( T('Eucalyptus Sanitation'),URL('queries','esanitation')==URL(), URL('queries','esanitation'),[] ),
            ( T('Pinus Sanitation'),URL('queries','psanitation')==URL(), URL('queries','psanitation'),[] ),
            ( T('Invasive species'),URL('queries','especies_invasoras')==URL(), URL('queries','especies_invasoras'),[] ),
            ( T('General'),URL('queries','general')==URL(), URL('queries','general'),[] ),
        ]
    ),
    ( T('Data'), URL('admin','index')==URL(), URL('admin','index'),
        [
            ( T('Generate Latest Data'), URL('data','generateData')==URL, URL('data','generateData'),[] ),
            ( T('Load Data'), URL('data','loadData')==URL, URL('data','loadData'),[] ),
            ( T('Add and Edit Types'), URL('data','editTypes')==URL, URL('data','editTypes'),[] ),
            ( T('Send Data'), URL('data','sendData')==URL, URL('data','sendData'),[] ),
            ( T('Review Pending Samples'), URL('review','reviewIndex')==URL, URL('review','reviewIndex'),[] )          
        ]
    ),
    ( T('User'),URL('user','index')==URL(), URL('user','index'),
        [
            ( T('Profile'), URL('user','profile')==URL(), URL('user','profile'),[] ),
            ( T('Change password'), URL('user','change_password')==URL(), URL('user','change_password'),[] ),
        ]
    ),
    ( T('Media'),URL('default','index')==URL(), URL('default','index'),
        [
            ( T('Photos'), URL('data','photos')==URL(), URL('data','photos'),[] ),
            ( T('Tracks'), URL('data','tracks')==URL(), URL('data','tracks'),[] ),
        ]
    ),
    ( T('Maps'),URL('maps','index')==URL(), URL('maps','index'),
        [
        ]
    ),
    ( T('Administration'), URL('admin','index')==URL(), URL('admin','index'),
        [
            ( T('Samples\'s Follow Up'), URL('data','followup')==URL, URL('data','followup'),[] ),
            ( T('Users'), URL('admin','users')==URL(), URL('admin','users'), [] ),
            ( T('Memberships'), URL('admin','memberships')==URL(), URL('admin','memberships'), [] )
            
        ]
    ),
    ( T('About'),URL('about','index')==URL(), URL('about','index'),
        [
        ]
    ),
    ( T('Help'), URL('help','index')==URL(), URL('help','index'),
        [
            ( T('Basic help'), URL('help','appbasic')==URL(), URL('help','appbasic'),[] ),
            ( T('App manual'), URL('help','appmanual')==URL(), URL('help','appmanual'),[] ),
            ( T('System documentation'),URL('help','sysmanual')==URL(), URL('help','sysmanual'),[] ),
        ]
    ),
]

menuUser = [
    ( T('Home'), URL('default','index')==URL, URL('default','index'),[] ),
    ( T('Queries'), URL('queries','index')==URL(), URL('queries','index'),
        [            
            ( T('Native forest'),URL('queries','nforest')==URL(), URL('queries','nforest'),[] ),
            ( T('Planted forest'),URL('queries','pforest')==URL(), URL('queries','pforest'),[] ),  
            ( T('Forest'),URL('queries','affor')==URL(), URL('queries','affor'),[] ),  
            ( T('Non-wood products'), URL('queries','nonwood')==URL, URL('queries','nonwood'),[] ),    
            ( T('Soil'),URL('queries','soil')==URL(), URL('queries','soil'),[] ),
            ( T('Fauna'), URL('queries','fauna')==URL(), URL('queries','fauna'),[] ),
            ( T('Flora'), URL('queries','flora')==URL(), URL('queries','flora'),[] ),
            ( T('Vegetation cover'), URL('queries','vegetation')==URL(), URL('queries','vegetation'), [] ),
            ( T('Water'), URL('queries','water')==URL(), URL('queries','water'),[] ),           
            ( T('Forest Overview'), URL('queries','foverview')==URL(), URL('queries','foverview'),[] ),    
            ( T('Relief'),URL('queries','relief')==URL(), URL('queries','relief'),[] ),        
            ( T('Environmental problems'),URL('queries','eviron')==URL(), URL('queries','environ'),[] ),
            ( T('Eucalyptus Sanitation'),URL('queries','esanitation')==URL(), URL('queries','esanitation'),[] ),
            ( T('Pinus Sanitation'),URL('queries','psanitation')==URL(), URL('queries','psanitation'),[] ),
            ( T('Invasive species'),URL('queries','especies_invasoras')==URL(), URL('queries','especies_invasoras'),[] ),
            ( T('General'),URL('queries','general')==URL(), URL('queries','general'),[] ),
            
        ]
    ),
    ( T('Maps'),URL('maps','index')==URL(), URL('maps','index'),
        [
        ]
    ),
    ( T('User'),URL('user','index')==URL(), URL('user','index'),
        [

            ( T('Profile'), URL('user','profile')==URL(), URL('user','profile'),[] ),
            ( T('Change password'), URL('user','change_password')==URL(), URL('user','change_password'),[] ),
        ]
    ),
    
    ( T('About'),URL('about','index')==URL(), URL('about','index'),
        [
        ]
    ),
    ( T('Help'), URL('help','index')==URL(), URL('help','index'),
        [
            ( T('Basic help'), URL('help','appbasic')==URL(), URL('help','appbasic'),[] ),
            ( T('App manual'), URL('help','appmanual')==URL(), URL('help','appmanual'),[] ),
            ( T('System documentation'),URL('help','sysmanual')==URL(), URL('help','sysmanual'),[] ),
        ]
    ),
]

menuPublic = [
    ( T('Home'), URL('default','index')==URL, URL('default','index'),[] ),
    ( T('About'),URL('about','index')==URL(), URL('about','index'),
        [
        ]
    ),
    ( T('Help'), URL('help','index')==URL(), URL('help','index'),
        [
            ( T('Basic help'), URL('help','appbasic')==URL(), URL('help','appbasic'),[] ),
        ]
    ),
]

response.menu = createMenu(menu)
