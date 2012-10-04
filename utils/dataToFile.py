#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os, sys
import pyodbc
import codecs

# El encoding
# miEnc = 'utf-8'
miEnc = 'latin-1'

# Conectar
conn = pyodbc.connect( "DSN=DGF_DATABASE;UID=fpacheco;PWD=fpacheco" )
# Lista de tablas 
cur = conn.cursor()
cur.tables()
tables = cur.fetchall()
for t in tables:
    #if (t.table_name!='dtproperties') and (t.table_name!='Enfermedades') and (t.table_name!='Monitoreos') and (t.table_name!='Otros'):
    if (t.table_name!='dtproperties') and (t.table_name!='MAPINFO_MAPCATALOG'):
        filename = u"%s.txt" % t.table_name
        miFile=codecs.open(filename,'wb+',encoding=miEnc)
        print u"Open %s" % filename
        sql = u'SELECT * FROM %s' % t.table_name
        cur.execute( sql )
        rows = cur.fetchall()    
        for row in rows:
            #for f in row[0:-1]:
            #    s = "%s|" % f
                # print s
                #miFile.write( unicode(s).encode(miEnc) )
            #    miFile.write( s )
            #s = "%s" % rows[-1]
            #miFile.write( unicode(s).encode(miEnc) )
            s = "%s" % row
            miFile.write( s )    
            miFile.write("\n")
        miFile.close()
        print u"%s closed" % filename
