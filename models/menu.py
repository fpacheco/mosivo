"""
response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
]
"""

# For develop only
if DEVELOP_MODE:
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
            ( M_USER,'Environmental problems','queries','eviron',[] )
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
    ( T('Models'), URL('models','index')==URL(), URL('models','index'),
        [            
            ( T('Wood'), URL('models','wood')==URL(), URL('models','wood'),[] ),
            ( T('Biomass'),URL('models','biomass')==URL(), URL('models','biomass'),[] ),
        ]
    ),
    ( T('User'),URL('user','index')==URL(), URL('user','index'),
        [
            ( T('Profile'), URL('user','profile')==URL(), URL('user','profile'),[] ),
            ( T('Change password'), URL('user','change_password')==URL(), URL('user','change_password'),[] ),
        ]
    ),
    ( T('Administration'), URL('admin','index')==URL(), URL('admin','index'),
        [
            ( T('Users'), URL('admin','users')==URL(), URL('admin','users'), [] ),
            ( T('Groups'), URL('admin','groups')==URL(), URL('admin','groups'), [] ),
            ( T('Memberships'), URL('admin','memberships')==URL(), URL('admin','memberships'), [] ),
            ( T('Statistics'), URL('admin','stats')==URL(), URL('amin','stats'),[] ),
            
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
    ( T('Models'), URL('models','index')==URL(), URL('models','index'),
        [            
            ( T('Wood'), URL('models','wood')==URL(), URL('models','wood'),[] ),
            ( T('Biomass'),URL('models','biomass')==URL(), URL('models','biomass'),[] ),
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
