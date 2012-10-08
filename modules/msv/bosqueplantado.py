# -*- coding: utf-8 -*-
"""
"""

class BosquePlantado():
    """ """
    def __init__(self,con,BPrIds):
        """docstring for __init__"""
        self.con = con
        self.cur = self.con.cursor()
        self.BPrIds = BPrIds
        self.setBasicData()

    def setBasicData(self):
        """docstring for se"""
        sExpr = []
        for id in self.ids:
            sExpr.append( "Codigo_Plan_Pro=%d" % id)
        ors = " OR ".join( sExpr )
        sql = "SELECT * FROM Planes WHERE %s ORDER BY Año_Dec ASC" % ors
        self.cur.execute( sql )
        rows = self.cur.fetchall()
        data = []
        for row in rows:
            rowData = {}
            ## rowData['id'] = row[0] ## id de ese proyecto de bosque
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
            rowData['raleo'] = self.setRaleo() # Datos de los raleos
            rowData['poda'] = self.setPoda() # Datos de las podas
            data.append(rowData)

        self.data = data

    def setFechaCorte(self):
        """docstring for setFechaCorte"""
        return 0

    def setRaleo(self):
        """docstring for setRaleo"""
        return []

    def setPoda(self):
        """docstring for setPoda"""
        return []

