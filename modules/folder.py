# -*- coding: utf-8 -*-
class Folder():

	def __init__(self, cursor, folder_id):
		"""
		Class that creates the Carpeta object and sets it's params
		"""
		self.cursor = cursor
		self.folder_id = folder_id

	def location(self):
		locSQL = """SELECT CarpetaBPLongitudGrados, CarpetaBPLongitudMinutos, CarpetaBPLongitudSegundos, 
				CarpetaBPLatitudGrados, CarpetaBPLatitudMinutos, CarpetaBPLatitudSegundos
				FROM CarpetaBP 
				WHERE CarpetaBPId = """ + str(self.folder_id) + ";"
		self.cursor.execute(locSQL)
		row = self.cursor.fetchone()
		if row != None:
			tempLon = float(row[1])/60 + float(row[2])/3600
			tempLat = float(row[4])/60 + float(row[5])/3600
			if float(row[0]) < 0:
				lon = float(row[0]) - tempLon
			else:
				lon = float(row[0]) + tempLon
			if float(row[3]) < 0:
				lat = float(row[3]) - tempLat
			else:
				lat = float(row[3]) + tempLat
			return (lon, lat)
		else:
			return None

	def registries(self):
		"""
		Method which returns the registries of the Folder
		"""
		registries = Registries(self.cursor, self.folder_id)
		return registries.data()

	def cuts(self):
		"""
		Method which returns the final cuts of the Folder
	    """
		cutsSQL = """SELECT CarpetaBPProyCortaFinalVolum, CarpetaBPProyCortaFinalFecha, CarpetaBPExisCortaFinalVolum, 
				CarpetaBPExisCortaFinalFecha
				FROM CarpetaBP 
				WHERE CarpetaBPId = """ + str(self.folder_id) + ";"
		self.cursor.execute(cutsSQL)
		row = self.cursor.fetchone()
		if row != None:
			return (row[0], row[1], row[2], row[3])
		else:
			return None

	def justiceSection(self):
		"""
		CarpetaBPSeccionCatastralEstabl,smallint
		CarpetaBPSeccionJudicialEstabl,smallint
		CarpetaBPSeccionPolicialEstabl,smallint
		"""
		justiceSection = """SELECT CarpetaBPSeccionJudicialEstabl
				FROM CarpetaBP 
				WHERE CarpetaBPId = """ + str(self.folder_id) + ";"
		self.cursor.execute(justiceSection)
		row = self.cursor.fetchone()
		if row != None:
			return row[0]
		else:
			return None

	def policeSection(self):
		"""
		CarpetaBPSeccionCatastralEstabl,smallint
		CarpetaBPSeccionJudicialEstabl,smallint
		CarpetaBPSeccionPolicialEstabl,smallint
		"""
		policeSection = """SELECT CarpetaBPSeccionPolicialEstabl
				FROM CarpetaBP 
				WHERE CarpetaBPId = """ + str(self.folder_id) + ";"
		self.cursor.execute(policeSection)
		row = self.cursor.fetchone()
		if row != None:
			return row[0]
		else:
			return None

	def cadastralSection(self):
		"""
		CarpetaBPSeccionCatastralEstabl,smallint
		CarpetaBPSeccionJudicialEstabl,smallint
		CarpetaBPSeccionPolicialEstabl,smallint
		"""
		cadastralSection = """SELECT CarpetaBPSeccionCatastralEstabl
				FROM CarpetaBP 
				WHERE CarpetaBPId = """ + str(self.folder_id) + ";"
		self.cursor.execute(cadastralSection)
		row = self.cursor.fetchone()
		if row != None:
			return row[0]
		else:
			return None