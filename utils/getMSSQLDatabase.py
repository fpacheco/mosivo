# -*- coding: utf-8 -*-
#!/usr/bin/python
import os, sys
import pyodbc

# Conectar
conn = pyodbc.connect( "DNS=DGF_DATABASE;UID=fpacheco;PWD=fpacheco" )
# Lista de tablas 
cur = conn.cursor()
cur.tables()
tables = cur.fetchall()
for t in tables:
    print "dbro.define_table (u'%s'," % t.table_name
    # Lista de columnas
    cur.columns(table=t.table_name)
    cols = cur.fetchall()
    for row in cols:
        print "Field(u'%s','%s')" % (row.column_name,row.type_name)
    print ")"
    print ""
cur.close ()
