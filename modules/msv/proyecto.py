# -*- coding: utf-8 -*-
"""
"""
from bosqueplantado import BosquePlantado as BPl
from bosqueproyectado import BosqueProyectado as BPr

class Proyecto():
    """ setCoord de la base de datos
    coord desde la clase
    """
    """
    def __init__(self,con,id):
        self.con = con
        self.cur = con.cursor()
        if self.__checkId(id):
            self.id = id
            self.setBasicData()
            ## El orden es importante
            self.setBProyectado()
    """
    def __init__(self, id):
        self.id = id
        self.setBPlantado()


    def __checkId(self,id):
        """Verifica si existe un proyecto con ese id"""
        self.cursor.execute('SELECT Nro_Carpeta FROM Carpetas_P WHERE Nro_Carpeta=?',id)
        rows = self.cursor.fetchall()
        if len(rows)==1:
            return True
        return False

    def setBasicData(self):
        """Obtiene los datos básicos desde la BD para este proyecto"""
        fields=[
            'Longitud',
            'Latitud',
            'Cod_Dpto',
            'Cod_SJ',
            'Baja'
            ]
        sql = "SELECT %s FROM Carpetas_P WHERE Nro_Carpeta=%d" % ( ",".join(fields),self.id )
        self.cur.execute( sql )
        rows = self.cur.fetchall()
        if len(rows)==1:
            for row in rows:
                self.lon = row[0][0]
                self.lat = row[0][1]
                self.codDepto = row[0][2]
                self.codSecJud = row[0][3]
                self.baja = row[0][4]

        self.codPadron = self.setCodPadron()

    def setCodPadron(self):
        """Obtiene el codigo del padron para este proyecto"""
        self.cursor.execute('SELECT Codigo_Pad FROM Registro WHERE Codigo_Cp_Pr=?',self.id)
        rows = self.cursor.fetchall()
        if len(rows)==1:
            return rows[0][0]
        return None

    def setBPlantado(self):
        """Obtiene los datos de bosque plantado para este proyecto"""
        self.bPlantado = BPl(self.con,self.bProyectado.BPlIds)

    def setBProyectado(self):
        """Obtiene los datos de bosque proyectado para este proyecto"""
        self.bProyectado = BPr(self.con,self.id)
        
    def getBPlantado(self):
        if not self.bPlantado:
            self.setBPlantado()
        return self.bPlantado
        
    def getBProyectado(self):
        if not self.bProyectado:
            self.setBProyectado()
        return self.bProyectado

