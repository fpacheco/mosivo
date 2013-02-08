# -*- coding: utf-8 -*-

class Registries():
	"""
	Class which holds the registries of the Folder
	"""
	def __init__(self, cursor, folder_id):
		self.cursor = cursor
		self.folder_id = folder_id

	def data(self):
		"""
		Method which returns the data of the registries of the Folder
	    """
		registriesDataSQL = """SELECT cbp.CarpetaBPId, cbpp.EspecieGeneroPadronGeneroNombre, cbpp.EspecieGeneroPadronEspecieNombre,
				cbpp.CarpetaBPPadronPlantacionAnio, cbpp.CarpetaBPPadronDensidadPlantacion,
				cbpp.CarpetaBPPadronSupEfectiva, ts.TipoSueloNombre
				FROM CarpetaBP cbp, CarpetaBPPadron cbpp, CarpetaBPGrupoDeSueloPorPadronGrupoDeSue cbpgs, TipoSuelo ts
				WHERE cbp.CarpetaBPId = cbpgs.CarpetaBPId AND cbpgs.TipoSueloId = ts.TipoSueloId AND 
				cbp.CarpetaBPId = cbpp.CarpetaBPId AND cbp.CarpetaBPId = """ + str(self.folder_id) + ";"
		self.cursor.execute(registriesDataSQL)
		rows = self.cursor.fetchall()
		ret = {}
		for row in rows:
			data = {}
			data['gender'] = row[1]
			data['species'] = row[2]
			data['year'] = row[3]
			data['density'] = row[4]
			data['efectiveArea'] = row[5]
			data['soliType'] = row[6]
			ret[row[0]].append(data)
		return ret
		