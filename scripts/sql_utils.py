#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
fi = re.compile( "INSERT INTO TipoOpcionSanidad(Pino|Eucalyptus)\(tipo,ido,opcion\) VALUES\(\d+\,\D" )
se = re.compile( "INSERT INTO TipoOpcionSanidad(Pino|Eucalyptus)\(tipo,ido,opcion\) VALUES\(\d+,\d+,'No se define'\);" )

"""
try:
    f = open("sqltypes.sql", "r")
    try:
        lines = f.readlines()
        sm=str()
        for l in lines:
            l = l[:-1]
            suc = fi.match(l)
            if suc:
                if sm == suc.group():
                    i+=1
                else:
                    sm = suc.group()
                    i=1
                nl = l.replace(sm,"%s%d,'" % (sm[:-1],i) )
                print nl
            else:
                print l
    finally:
        f.close()
except IOError:
    print "Error"
"""

try:
    f = open("sqltypes.sql", "r")
    try:
        lines = f.readlines()
        sm=str()
        for l in lines:
            l = l[:-1]
            suc = se.match(l)
            if suc:
                pass
            else:
                print l
    finally:
        f.close()
except IOError:
    print "Error"
