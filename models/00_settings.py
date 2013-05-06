# -*- coding: utf-8 -*-
from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = u'Modelo de simulación de volumen'
settings.subtitle = 'powered by web2py'
settings.author = 'InGeSur srl'
settings.author_email = 'contacto@ingesur.com.uy'
settings.keywords = ''
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'c966722c-a947-44b7-9212-7a2c00b38de6'
settings.email_server = 'logging'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = ['jqgrid']
# Modificar la base de datos

# Mode de desarrollo
DEVELOP_MODE = True
# Versionado de cada una de las tablas de la base de datos
VERSIONING_DB = False
# Si esto en InGeSur emulo con postgresql via ODBC
IN_DGF = False

# Datos de acceso al servidor MSSQL vía ODBC (pyodbc/FreeTDS)
MSSQL_USER = 'fpacheco'
MSSQL_PASS = 'fpacheco'
MSSQL_SERVER = '192.168.20.7'
MSSQL_DATABASE = 'DGF'
# Nombre de una seccion en odbcinst.ini [SQL Server]
ODBC_DRIVER = '{SQL Server}'
# Nombre del DSN en odbc.ini
ODBC_DSN = 'DGF_DATABASE'
# Texto de conexion
CON_STR = "DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s" % (
    ODBC_DRIVER,
    MSSQL_SERVER,
    MSSQL_DATABASE,
    MSSQL_USER,
    MSSQL_PASS,
)
# Texto alternativo de conexión (con DSN en odbc.ini)
CON_STR2 = "DSN=%s;UID=%s;PWD=%s" % (
    ODBC_DSN,
    MSSQL_USER,
    MSSQL_PASS,
)
