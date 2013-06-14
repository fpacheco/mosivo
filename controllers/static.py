import gluon
from gluon.contrib.gql import GQLDB
from gluon.html import A
from gluon.html import B
from gluon.html import BEAUTIFY
from gluon.html import BODY
from gluon.html import BR
from gluon.html import CENTER
from gluon.validators import CLEANUP 
from gluon.html import CODE
from gluon.validators import CRYPT
from gluon.html import DIV
from gluon.html import FORM
from gluon.html import I
from gluon.html import IFRAME
from gluon.html import IMG
from gluon.html import INPUT
from gluon.validators import IS_ALPHANUMERIC
from gluon.validators import IS_DATE
from gluon.validators import IS_DATETIME
from gluon.validators import IS_DATETIME_IN_RANGE
from gluon.validators import IS_DATE_IN_RANGE
from gluon.validators import IS_DECIMAL_IN_RANGE
from gluon.validators import IS_EMAIL
from gluon.validators import IS_EMPTY_OR
from gluon.validators import IS_EQUAL_TO
from gluon.validators import IS_EXPR
from gluon.validators import IS_FLOAT_IN_RANGE
from gluon.validators import IS_IMAGE
from gluon.validators import IS_INT_IN_RANGE
from gluon.validators import IS_IN_DB
from gluon.validators import IS_IN_SET
from gluon.validators import IS_IPV4
from gluon.validators import IS_LENGTH
from gluon.validators import IS_LIST_OF
from gluon.validators import IS_LOWER
from gluon.validators import IS_MATCH
from gluon.validators import IS_NOT_EMPTY
from gluon.validators import IS_NOT_IN_DB
from gluon.validators import IS_NULL_OR
from gluon.validators import IS_SLUG
from gluon.validators import IS_STRONG 
from gluon.validators import IS_TIME
from gluon.validators import IS_UPLOAD_FILENAME
from gluon.validators import IS_UPPER
from gluon.validators import IS_URL
from gluon.html import LABEL
from gluon.html import LEGEND
from gluon.html import LI
from gluon.html import LINK
from gluon.html import MARKMIN
from gluon.html import MENU
from gluon.html import META
from gluon.html import OBJECT
from gluon.html import OL
from gluon.html import ON
from gluon.html import OPTGROUP
from gluon.html import OPTION
from gluon.html import P
from gluon.html import PRE
from gluon.html import SCRIPT
from gluon.html import SELECT
from gluon.html import SPAN
from gluon.html import TABLE
from gluon.html import TAG
from gluon.html import TBODY
from gluon.html import TD
from gluon.html import TEXTAREA
from gluon.html import TFOOT
from gluon.html import TH 
from gluon.html import THEAD
from gluon.html import TITLE
from gluon.html import TR
from gluon.html import TT
from gluon.html import UL
from gluon.html import URL
from gluon.html import XHTML
from gluon.html import XML
from gluon.html import embed64
from gluon.html import xmlescape
from gluon.sql import SQLDB
from gluon.sqlhtml import SQLFORM
from gluon.sql import SQLField
from gluon.sqlhtml import SQLTABLE
from gluon.html import STYLE
from gluon.http import redirect
import gluon.languages.translator as T
from gluon.tools import Auth
from gluon.tools import Service
global auth; auth = gluon.tools.Auth()
global cache; cache = gluon.cache.Cache()
global crud; crud = gluon.tools.Crud()
global db; db = gluon.sql.DAL()
import gluon.compileapp.local_import_aux as local_import
global request; request = gluon.globals.Request()
global response; response = gluon.globals.Response()
global service; service = gluon.tools.Service()
global session; session = gluon.globals.Session()
global DAL; DAL = gluon.dal()
global HTTP; HTTP = gluon.http()
global LOAD; LOAD = gluon.compileapp.LoadFactory()
global LOAD; LOAD = gluon.compileapp.LoadFactory()