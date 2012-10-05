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
            self.proyId = proyId
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
        data = []
        self.cursor.execute('SELECT * FROM Planes_Pro WHERE Codigo_Cp=?',self.proyId)
        rows = self.cursor.fetchall()
        for row in rows:
            raleo = []
            self.id = row[0]
            self.fechaPlantac = row[3] ## Solo el año
            self.codGenero = row[4]
            self.codEspecie = row[5]
            self.epoca = row[6]
            self.area = row[7] ## En hectareas
            self.densidad = row[8] ## En arboles por hectare
            self.distArbol = row[9]
            self.distFila = row[10]
            self.distSilvo = row[11]
            self.calificacion = row[12]
            self.objetivo = row[20]
            self.fechaCorte = 0
            self.raleo = raleo

