# -*- coding: utf-8 -*-
"""
"""

class BosqueProyectado():
    """ """
    def __init__(self,con,proyId):
        """docstring for __init__"""
        self.con = con
        self.cursor = self.con.cursor()
        if self.__checkProyId(proyId):
            self.proyId = proyId ## Nro_Carpeta de la tabla Carpetas_P
            self.setBasicData()

    def __checkProyId(self,id):
        """Verifica si existe un registro con ese id en la tabla Planes_Pro"""
        self.cursor.execute('SELECT Codigo_Cp FROM Planes_Pro WHERE Codigo_Cp=?',id)
        rows = self.cursor.fetchall()
        if len(rows)>0:
            return True
        return False

    def setBasicData(self):
        """docstring for se"""
        # from datetime import date
        #self.cursor.execute( u'SELECT * FROM Planes_Pro WHERE Codigo_Cp=? AND Año_Pro>=?', (self.proyId,date.today().year) )
        self.cursor.execute( u'SELECT * FROM Planes_Pro WHERE Codigo_Cp=? ORDER BY Año_Pro ASC', self.proyId )
        rows = self.cursor.fetchall()
        ids = []
        data = []
        for row in rows:
            rowData = {}
            rowData['id'] = row[0] ## id de ese proyecto de bosque
            ids.append( row[0] )
            rowData['fechaPlant'] = row[3] ## Solo el año
            rowData['codGenero'] = row[4] ## Codigo del genero
            rowData['codEspecie'] = row[5] ## Codigo de la especie
            # rowData['epoca'] = row[6] ## Epoca???
            rowData['area']= row[7] ## Area proyectada de bosque (en hectareas!) 
            rowData['densidad'] = row[8] ## Número de arboles en una hectare
            rowData['distArbol']= row[9] ## Distancia entre arbole (E1)
            rowData['distFila'] = row[10]  ## Distancia entre filas (E2)
            rowData['distAreas'] = row[11] ## Distancia entre areas paltadas, para silvopastoreo (E3)
            rowData['calificacion'] = row[12]
            rowData['objProd'] = row[20] ## Objetivo productivo del bosque
            rowData['fechaCorte'] = self.setFechaCorte() # Turno o fecha que se va a cortar el bosque
            rowData['raleo'] = self.setRaleo() # Datoos de los raleos
            rowData['poda'] = self.setPoda() # Datos de las podas
            data.append(rowData)

        self.BPlIds = ids ## Los ids de bosques proyectados para la carpera id
        self.data = data ## Los datos de cada uno de los ids

    def setFechaCorte(self):
        """docstring for setFechaCorte"""
        return 0

    def setRaleo(self):
        """docstring for setRaleo"""
        return []

    def setPoda(self):
        """docstring for setPoda"""
        return []


