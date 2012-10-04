#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os, sys
import pyodbc

# Conectar
conn = pyodbc.connect( "DSN=DGF_DATABASE;UID=fpacheco;PWD=fpacheco" )

# Lista de tablas 
cur = conn.cursor()
cur.tables()
tables = cur.fetchall()
for t in tables:
    print "dbro.define_table(u'%s'," % t.table_name
    # Lista de columnas
    cur.columns(table=t.table_name)
    cols = cur.fetchall()
    for row in cols:
        print "    Field(u'%s',u'%s')," % (row.column_name,row.type_name)
    print ")"
    print ""
cur.close ()


## Primary keys
cur = conn.cursor()
cur.tables()
tables = cur.fetchall()
for t in tables:
    # Lista de columnas
    cur.primaryKeys(table=t.table_name)
    cols = cur.fetchall()
    print "Tabla: %s" % t.table_name
    for row in cols:
        print "    primaryKey: u'%s'," % (row.column_name)
    print ")"
    print ""
cur.close ()

## Foreign keys
cur = conn.cursor()
cur.tables()
tables = cur.fetchall()
for t in tables:
    # Lista de columnas
    cur.foreignKeys(table=t.table_name)
    cols = cur.fetchall()
    #print "Tabla: %s" % t.table_name
    for row in cols:
        print "%s" % row
cur.close ()


