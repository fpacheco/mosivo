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
    if auth.is_logged_in() and auth.has_membership('admins',auth.user.id):
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
    ( T('View'), URL('view','index')==URL, URL('view','index'),
        [
            ( T('Model data'), URL('modelconf','memberships')==URL(), URL('modelconf','memberships'),
                [
                    ( T('Raleo'), URL('modelconf','craleo')==URL(), URL('modelconf','craleo'), [] ),
                    ( T('Turno'), URL('modelconf','cturno')==URL(), URL('modelconf','cturno'), [] ),
                    ( T('Turno'), URL('modelconf','cturno')==URL(), URL('modelconf','cturno'), [] ),
                    ( T('Turno'), URL('modelconf','cturno')==URL(), URL('modelconf','cturno'), [] ),
                    ( T('Turno'), URL('modelconf','cturno')==URL(), URL('modelconf','cturno'), [] ),
                ]
            ),
            ( T('Data'), URL('modelconf','memberships')==URL(), URL('modelconf','memberships'),
                [
                    ( T('Plans'), URL('data','vplanes')==URL(), URL('data','vplanes'), [] ),
                    ( T('Declared stands'), URL('data','vrodald')==URL(), URL('data','vrodald'), [] ),
                ]
            ),
        ]
    ),
    ( T('Model Configuration'), URL('config','index')==URL, URL('config','index'),
        [
            ( T('Data updates'), URL('modelconf','configupdatefromrdb')==URL(), URL('modelconf','configupdatefromrdb'), [] ),
            ( T('Model execution'), URL('modelconf','modelupdate')==URL(), URL('modelconf','modelupdate'), [] ),
            LI(_class="divider"),
            ( T('Coefficients'), URL()==URL(), URL(),
                [
                    ( T('Área efectiva por especie y departamento'), URL('modelconf','mcaefectiva')==URL(), URL('modelconf','mcaefectiva'), [] ),
                    ( T('IMA por especie y departamento'), URL('modelconf','mcima')==URL(), URL('modelconf','mcima'), [] ),
                    ( T('Intervención (rodal)'), URL('modelconf','mcintervencionr')==URL(), URL('modelconf','mcintervencionr'), [] ),
                    ( T('Intervención (por departamento)'), URL('modelconf','mcintervenciona')==URL(), URL('modelconf','mcintervenciona'), [] ),
                    LI(_class="divider"),
                    ( T('Cosecha por especie y destino'), URL('modelconf','mccosecha')==URL(), URL('modelconf','mccosecha'), [] ),
                    ( T('Suelo por sección judicial'), URL('modelconf','mcgsuelo')==URL(), URL('modelconf','mcgsuelo'), [] ),
                    ( T('Biomasa por especie'), URL('modelconf','mcbcampoe')==URL(), URL('modelconf','mcbcampoe'), [] ),
                    ( T('Intervention type'), URL('modelconf','mtipointervencion')==URL(), URL('modelconf','mtipointervencion'), [] ),
                    LI(_class="divider"),
                    ( T('Biomasa en campo'), URL('modelconf','mcbcampo')==URL(), URL('modelconf','mcbcampo'), [] ),
                    ( T('Biomasa en la industria'), URL('modelconf','mcbindustria')==URL(), URL('modelconf','mcbindustria'), [] ),
                ]
            ),
            ( T('Others'), URL('modelconf','memberships')==URL(), URL('modelconf','memberships'),
                [
                    ( T('Destinations'), URL('modelconf','mdestino')==URL(), URL('modelconf','mdestino'), [] ),
                    ( T('Forest residues'), URL('modelconf','mtiporesiduoforestal')==URL(), URL('modelconf','mtiporesiduoforestal'), [] ),
                    ( T('Harvest type'), URL('modelconf','mcosecha')==URL(), URL('modelconf','mcosecha'), [] ),
                ]
            ),
            LI(_class="divider"),
            ( T('Verificar cumplimiento'), URL('modelconf','verifymodel')==URL(), URL('modelconf','verifymodel'), [] ),
        ]
    ),
    ( T('System administration'), URL('admin','index')==URL(), URL('admin','index'),
        [
            ( T('Users'), URL('sysadmin','users')==URL(), URL('sysadmin','users'), [] ),
            ( T('Memberships'), URL('sysadmin','memberships')==URL(), URL('sysadmin','memberships'), [] )

        ]
    ),
    ( T('Help'), URL('help','index')==URL(), URL('help','index'),
        [
            ( T('App manual'), URL('help','appmanual')==URL(), URL('help','appmanual'),[] ),
            ( T('System documentation'),URL('help','sysmanual')==URL(), URL('help','sysmanual'),[] ),
            LI(_class="divider"),
            ( T('About'),URL('about','index')==URL(), URL('about','index'),[]),
        ]
    ),
]

menuUser = [
    ( T('Home'), URL('default','index')==URL, URL('default','index'),[] ),
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
