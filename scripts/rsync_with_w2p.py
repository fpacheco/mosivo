#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este archivo sincroniza la fuente de la aplicación con el
de la raiz de web2py. Se ejecuta desde el propio directorio,
es decir: app/scrips/este_script.py

Mi árbol:
 src: workspace/app_source
 web2py: workspace/web2py_tree
"""

import os
import re
import sys
import time
import commands

APPNAME="mosivo"
HOME = os.path.expanduser("~")
APP_PATH=os.path.join( HOME, "workspace", APPNAME )
WEB2PY_PATH=os.path.join( HOME, "workspace", "web2py" )
WEB2PY_APP_PATH=os.path.join( WEB2PY_PATH, "applications" )

# Carpetas que NO queremos copiar..
EXCLUDE_SYNC_SUB_DIRS = [
    '.git',
    'databases',
    'backup',
    'export',
    'kml',
    'scripts',
    'tests',
    'uploads',
    'xml',
]

excl = ""
for d in EXCLUDE_SYNC_SUB_DIRS:
    excl += "--exclude %s " % d

print '\nrsync with web2py:\n'
## No delete: --delete
rsyncCommand = "rsync -a --delete --progress --stats -l -z -v -r -p %s %s %s" % (excl, APP_PATH, WEB2PY_APP_PATH)
[status,output]=commands.getstatusoutput(rsyncCommand)
print "%s" % rsyncCommand
