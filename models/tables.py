"""
Columns
Asociaciones
	AsociacionesId,smallint identity
	AsociacionesDescripcion,char
"""

db2.define_table('Asociaciones',
    Field('AsociacionesId', type='integer'),
    Field('AsociacionesDescripcion', type="string"),
    primarykey=['AsociacionesId'],
    migrate=False
)


"""
Calificacion
	CalificacionId,char
	CalificacionDescripcion,char
"""
db2.define_table('Calificacion',
    Field('CalificacionId', type='integer'),
    Field('CalificacionDescripcion', type="string"),
    primarykey=['CalificacionId'],
    migrate=False
)
 
""" 
CalificacionBP
	CalificacionBPCarpeta,decimal
	CalificacionBPPadron,decimal
	CalificacionBPMatricula,char
	CalificacionId,char
	CalifBPFechaHoraRegistroDig,datetime
	CalifBPUsuario,char
	CalifBPUsuarioUltimaModif,char
	CalifBPFechaHoraUltimaModif,datetime
"""
db2.define_table('CalificacionBP',
    Field('CalificacionBPCarpeta', type='integer'),
    Field('CalificacionBPPadron', type='integer'),
    Field('CalificacionBPMatricula', type='string'),
    Field('CalificacionId', db2.Calificacion.CalificacionId),
    Field('CalifBPFechaHoraRegistroDig', type="datetime"),
    Field('CalifBPUsuario', type="string"),
    Field('CalifBPUsuarioUltimaModif', type="string"),
    Field('CalifBPFechaHoraUltimaModif', type="datetime"),
    primarykey=['CalificacionBPCarpeta','CalificacionBPPadron','CalificacionId'],
    migrate=False
)

 
"""
CarpetaBN
	CarpetaBNId,char
	CarpetaBNFechaRegistro,datetime
	CarpetaBNNombreEstabl,char
	CarpetaBNDepartamentoEstabl,char
	CarpetaBNSeccionCatastralEstabl,smallint
	CarpetaBNSeccionJudicialEstabl,smallint
	CarpetaBNSeccionPolicialEstabl,smallint
	CarpetaBNParajeEstabl,char
	CarpetaBNCIRepLegal,int
	CarpetaBNNombreRepLegal,char
	CarpetaBNDireccionRepLegal,char
	CarpetaBNDepartamentoRepLegal,char
	CarpetaBNTelefonoRepLegal,char
	CarpetaBNCelularRepLegal,char
	CarpetaBNFaxRepLegal,char
	CarpetaBNMailRepLegal,char
	CarpetaBNCITecnico,int
	CarpetaBNNombreTecnico,char
	CarpetaBNDireccionTecnico,char
	CarpetaBNTelefonoTecnico,char
	CarpetaBNCelularTecnico,char
	CarpetaBNFaxTecnico,char
	CarpetaBNMailTecnico,char
	CarpetaBNTipoProfesional,bit
	CarpetaBNTipoRebrote,smallint
	CarpetaBNEstadoSanitario,varchar
	CarpetaBNInvEspExoticas,bit
	CarpetaBNIncForestales,bit
	CarpetaBNAccionesAntropicas,varchar
	CarpetaBNAreaArboladaTotal,decimal
	CarpetaBNAreaArboladaBN,decimal
	CarpetaBNAreaArboladaBP,decimal
	CarpetaBNFechaHoraRegistroDig,datetime
	CarpetaBNUsuario,char
	AsociacionesId,smallint
	CarpetaBNNroCarpeta,int
""" 

db2.define_table('CarpetaBN',
    Field('CarpetaBNId', type='integer'),
    Field('CarpetaBNFechaRegistro', type='datetime'),
    Field('CarpetaBNNombreEstabl', type='string'),
    Field('CarpetaBNDepartamentoEstabl', db2.Departamentos.DepartamentosId),
    Field('CarpetaBNSeccionCatastralEstabl', type="integer"),
    Field('CarpetaBNSeccionJudicialEstabl', type="integer"),
    Field('CarpetaBNSeccionPolicialEstabl', type="integer"),
    Field('CarpetaBNParajeEstabl', type="string"),
    Field('CarpetaBNCIRepLegal', type="integer"),
    Field('CarpetaBNNombreRepLegal', type="string"),
    Field('CarpetaBNDireccionRepLegal', type="string"),
    Field('CarpetaBNDepartamentoRepLegal', db2.Departamentos.DepartamentosId),
    Field('CarpetaBNTelefonoRepLegal', type="string"),
    Field('CarpetaBNCelularRepLegal', type="string"),
    Field('CarpetaBNFaxRepLegal', type="string"),
    Field('CarpetaBNMailRepLegal', type="string"),
    Field('CarpetaBNCITecnico', type="string"),
    Field('CarpetaBNNombreTecnico', type="string"),
    Field('CarpetaBNDireccionTecnico', type="string"),
    Field('CarpetaBNTelefonoTecnico', type="string"),
    Field('CarpetaBNCelularTecnico', type="string"),
    Field('CarpetaBNFaxTecnico', type="string"),
    Field('CarpetaBNMailTecnico', type="string"),
    Field('CarpetaBNTipoProfesional', type="boolean"), # ver
    Field('CarpetaBNTipoRebrote', type="integer"),
    Field('CarpetaBNEstadoSanitario', type="string"),
    Field('CarpetaBNInvEspExoticas', type="boolean"),
    Field('CarpetaBNIncForestales', type="boolean"),
    Field('CarpetaBNAreaArboladaTotal', type="decimal"),
    Field('CarpetaBNAreaArboladaBN', type="decimal"),
    Field('CarpetaBNAreaArboladaBP', type="decimal"),
    Field('CarpetaBNFechaHoraRegistroDig', type="datetime"),
    Field('CarpetaBNUsuario', type="string"),
    Field('AsociacionesId', db2.Asociaciones.AsociacionesId),
    Field('CarpetaBNNroCarpeta', type="integer"),
    primarykey=['CarpetaBNId'],
    migrate=False
)
 
""" 
CarpetaBNPadron
	CarpetaBNId,char
	CarpetaBNPadronId,decimal
	CarpetaBNPadronSeccJudicial,smallint
	CarpetaBNPadronSeccPolicial,smallint
	CarpetaBNPadronSupBN,decimal
	CarpetaBNPadronSupBP,decimal
	CarpetaBNPadronTotal,decimal
	CarpetaBNPadronSupPadron,decimal
"""
db2.define_table('CarpetaBNPadron',
    Field('CarpetaBNId', db2.CarpetaBN.CarpetaBNId),
    Field('CarpetaBNPadronId', type='decimal'),
    Field('CarpetaBNPadronSeccJudicial', type='integer'),
    Field('CarpetaBNPadronSeccPolicial', type='integer'),
    Field('CarpetaBNPadronSupBN', type="decimal"),
    Field('CarpetaBNPadronSupBP', type="decimal"),
    Field('CarpetaBNPadronTotal', type="decimal"),
    Field('CarpetaBNPadronSupPadron', type="decimal"),
    primarykey=['CarpetaBNId','CarpetaBNPadronId','CarpetaBNPadronSeccJudicial'],
    migrate=False
)

""" 
 
CarpetaBNPropietario
	CarpetaBNId,char
	CarpetaBNPropietarioCI,int
	CarpetaBNPropietarioNombre,char
	CarpetaBNPropietarioRazonSocial,char
	CarpetaBNPropietarioRUT,char
	CarpetaBNPropietarioDireccion,char
	CarpetaBNPropietarioDep,char
	CarpetaBNPropietarioCiudad,char
	CarpetaBNPropietarioTelefono,char
	CarpetaBNPropietarioCelular,char
	CarpetaBNPropietarioFax,char
	CarpetaBNPropietarioMail,char
"""

db2.define_table('CarpetaBNPropietario',
    Field('CarpetaBNId', db2.CarpetaBN.CarpetaBNId),
    Field('CarpetaBNPropietarioCI', type='integer'),
    Field('CarpetaBNPropietarioNombre', type='string'),
    Field('CarpetaBNPropietarioRazonSocial', type='string'),
    Field('CarpetaBNPropietarioRUT', type="string"),
    Field('CarpetaBNPropietarioDireccion', type="string"),
    Field('CarpetaBNPropietarioDep', db2.Departamentos.DepartamentosId),
    Field('CarpetaBNPropietarioCiudad', type="string"),
    Field('CarpetaBNPropietarioTelefono', type="string"),
    Field('CarpetaBNPropietarioCelular', type="string"),
    Field('CarpetaBNPropietarioFax', type="string"),
    Field('CarpetaBNPropietarioMail', type="string"),
    primarykey=['CarpetaBNId','CarpetaBNPropietarioCI'],
    migrate=False
)

"""
 
CarpetaBP
	CarpetaBPId,decimal
	CarpetaBPFechaRegistro,datetime
	CarpetaBPRazonSocial,char
	CarpetaBPRUT,char
	CarpetaBPDireccionProductor,char
	CarpetaBPDepartamentoProductor,char
	CarpetaBPCuidadProductor,char
	CarpetaBPTelefonoProductor,char
	CarpetaBPCelularProductor,char
	CarpetaBPFaxProductor,char
	CarpetaBPMailProductor,char
	CarpetaBPNombreEstabl,char
	CarpetaBPDepartamentoEstabl,char
	CarpetaBPSeccionCatastralEstabl,smallint
	CarpetaBPSeccionJudicialEstabl,smallint
	CarpetaBPSeccionPolicialEstabl,smallint
	CarpetaBPCIRepLegal,int
	CarpetaBPNombreRepLegal,char
	CarpetaBPDireccionRepLegal,char
	CarpetaBPDepartamentoRepLegal,char
	CarpetaBPTelefonoRepLegal,char
	CarpetaBPCelularRepLegal,char
	CarpetaBPFaxRepLegal,char
	CarpetaBPMailRepLegal,char
	CarpetaBPCITecnico,int
	CarpetaBPTipoProf,bit
	CarpetaBPNombreTecnico,char
	CarpetaBPDireccionTecnico,char
	CarpetaBPTelefonoTecnico,char
	CarpetaBPCelularTecnico,char
	CarpetaBPFaxTecnico,char
	CarpetaBPMailTecnico,char
	CarpetaBPCIAutorizado,int
	CarpetaBPNombAutorizado,char
	CarpetaBPTelefAutorizado,char
	CarpetaBPCelAutorizado,char
	CarpetaBPFaxAutorizado,char
	CarpetaBPMailAutorizado,char
	CarpetaBPFechaHoraRegistroDig,datetime
	CarpetaBPUsuario,char
	CarpetaBPFechaHoraUltimaModif,datetime
	CarpetaBPUsuarioUltimaModif,char
	CarpetaBPDepartamentoTecnico,smallint
	CarpetaBPCiudadTecnico,char
	CarpetaBPCiudadRepLegal,char
	CarpetaBPProcedencia,varchar
	CarpetaBPEspeciesElegidas,varchar
	CarpetaBPCarpetaBNNumero,int
	CarpetaBPLaboreoSuelo,varchar
	CarpetaBPControlMalezas,varchar
	CarpetaBPControEnemigos,varchar
	CarpetaBPTareasCulturales,varchar
	CarpetaBPFertilizacion,varchar
	CarpetaBPSistemaPlantacion,varchar
	CarpetaBPForestacionObjetivo,varchar
	CarpetaBPIncendiosOtrosElementos,varchar
	CarpetaBPIncendiosProteccion,varchar
	CarpetaBPPlagasProteccion,varchar
	CarpetaBPUltimoNroProgFor,smallint
	CarpetaBPUltimoNroCarRaleo,smallint
	CarpetaBPCarpetaBN,char
	CarpetaBPTelefonoEstabl,char
	CarpetaBPUltimoTipoSuelo,smallint
	CarpetaBPDireccionEstabl,char
	CarpetaBPNroCarpeta,decimal
	Migrado,bit
	CarpetaBPLongitudGrados,decimal
	CarpetaBPLongitudMinutos,decimal
	CarpetaBPLongitudSegundos,decimal
	CarpetaBPLatitudGrados,decimal
	CarpetaBPLatitudMinutos,decimal
	CarpetaBPLatitudSegundos,decimal
	CarpetaBPProyCortaFinalVolum,money
	CarpetaBPProyCortaFinalFecha,char
	CarpetaBPExisCortaFinalVolum,money
	CarpetaBPExisCortaFinalFecha,char
"""

db2.define_table('CarpetaBP',
    Field('CarpetaBPId', type='integer'),
    Field('CarpetaBPFechaRegistro', type='datetime'),
    Field('CarpetaBPRazonSocial', type='string'),
    Field('CarpetaBPRUT', type="string"),
    Field('CarpetaBPDireccionProductor', type="string"),
    Field('CarpetaBPDepartamentoProductor', db2.Departamentos.DepartamentosId),
    Field('CarpetaBPCuidadProductor', type="string"),
    Field('CarpetaBPTelefonoProductor', type="string"),
    Field('CarpetaBPCelularProductor', type="string"),
    Field('CarpetaBPFaxProductor', type="string"),
    Field('CarpetaBPMailProductor', type="string"),
    Field('CarpetaBPNombreEstabl', type="string"),
    Field('CarpetaBPDepartamentoEstabl', db2.Departamentos.DepartamentosId),
    Field('CarpetaBPSeccionCatastralEstabl', type="integer"),
    Field('CarpetaBPSeccionJudicialEstabl', type="integer"),
    Field('CarpetaBPSeccionPolicialEstabl', type="integer"),
    Field('CarpetaBPCIRepLegal', type="integer"),
    Field('CarpetaBPNombreRepLegal', type="string"),
    Field('CarpetaBPDireccionRepLegal', type="string"),
    Field('CarpetaBPDepartamentoRepLegal', db2.Departamentos.DepartamentosId),
    Field('CarpetaBPTelefonoRepLegal', type="string"),
    Field('CarpetaBPCelularRepLegal', type="string"),
    Field('CarpetaBPFaxRepLegal', type="string"),
    Field('CarpetaBPMailRepLegal', type="string"),
    Field('CarpetaBPCITecnico', type="integer"),
    Field('CarpetaBPTipoProf', type="boolean"), # ver
    Field('CarpetaBPNombreTecnico', type="string"),
    Field('CarpetaBPDireccionTecnico', type="string"),
    Field('CarpetaBPTelefonoTecnico', type="string"),
    Field('CarpetaBPCelularTecnico', type="string"),
    Field('CarpetaBPFaxTecnico', type="string"),
    Field('CarpetaBPMailTecnico', type="string"),
    Field('CarpetaBPCIAutorizado', type="integer"),
    Field('CarpetaBPNombAutorizado', type="string"),
    Field('CarpetaBPTelefAutorizado', type="string"),
    Field('CarpetaBPCelAutorizado', type="string"),
    Field('CarpetaBPFaxAutorizado', type="string"),
    Field('CarpetaBPMailAutorizado', type="string"),
    Field('CarpetaBPFechaHoraRegistroDig', type="datetime"),
    Field('CarpetaBPUsuario', type="string"),
    Field('CarpetaBPFechaHoraUltimaModif', type="datetime"),
    Field('CarpetaBPUsuarioUltimaModif', type="string"),
    Field('CarpetaBPDepartamentoTecnico', type="integer"),
    Field('CarpetaBPCiudadTecnico', type="string"),
    Field('CarpetaBPCiudadRepLegal', type="string"),
    Field('CarpetaBPProcedencia', type="string"),
    Field('CarpetaBPEspeciesElegidas', type="string"),
    Field('CarpetaBPCarpetaBNNumero', type="integer"),
    Field('CarpetaBPLaboreoSuelo', type="string"),
    Field('CarpetaBPControlMalezas', type="string"),
    Field('CarpetaBPControEnemigos', type="string"),
    Field('CarpetaBPTareasCulturales', type="string"),
    Field('CarpetaBPFertilizacion', type="string"),
    Field('CarpetaBPSistemaPlantacion', type="string"),
    Field('CarpetaBPForestacionObjetivo', type="string"),
    Field('CarpetaBPIncendiosOtrosElementos', type="string"),
    Field('CarpetaBPIncendiosProteccion', type="string"),
    Field('CarpetaBPPlagasProteccion', type="string"),
    Field('CarpetaBPUltimoNroProgFor', type="integer"),
    Field('CarpetaBPUltimoNroCarRaleo', type="integer"),
    Field('CarpetaBPCarpetaBN', type="string"),
    Field('CarpetaBPTelefonoEstabl', type="string"),
    Field('CarpetaBPUltimoTipoSuelo', type="integer"),
    Field('CarpetaBPDireccionEstabl', type="string"),
    Field('CarpetaBPNroCarpeta', type="decimal"),
    Field('Migrado', type="boolean"), #ver
    Field('CarpetaBPLongitudGrados', type="decimal"),
    Field('CarpetaBPLongitudMinutos', type="decimal"),
    Field('CarpetaBPLongitudSegundos', type="decimal"),
    Field('CarpetaBPLatitudGrados', type="decimal"),
    Field('CarpetaBPLatitudMinutos', type="decimal"),
    Field('CarpetaBPLatitudSegundos', type="decimal"),
    Field('CarpetaBPProyCortaFinalVolum', type="decimal"), # Money??
    Field('CarpetaBPProyCortaFinalFecha', type="string"),
    Field('CarpetaBPExisCortaFinalVolum', type="decimal"),
    Field('CarpetaBPExisCortaFinalFecha', type="string"),
    primarykey=['CarpetaBPId'],
    migrate=False
)

 
"""
CarpetaBPCarRaleo
	CarpetaBPId,decimal
	CarpetaBPCarRaleoId,decimal
	CarpetaBPCarRaleoPlantacionAnio,smallint
	CarpetaBPCarRaleoMetroPorHectarea,decimal
	CarpetaBPCarRaleoAlturaEstimada,smallint
	CarpetaBPCarRaleoDensidad,decimal
	CarpetaBPCarRaleoSuperficieRaleo,decimal
	CarpetaBPCarRaleoRodalEdad,smallint
	CarpetaBPCarRaleoSupEfectivaAPodar,decimal
	EspecieGeneroCarRaleoCodEspecie,decimal
	EspecieGeneroCarRaleoCodGenero,char
	EspecieGeneroCarRaleoEspecieNombre,char
	EspecieGeneroCarRaleoGeneroNombre,char
""" 

db2.define_table('CarpetaBPCarRaleo',
    Field('CarpetaBPId', db2.CarpetaBP.CarpetaBPId),
    Field('CarpetaBPCarRaleoId', type='decimal'),
    Field('CarpetaBPCarRaleoPlantacionAnio', type='integer'),
    Field('CarpetaBPCarRaleoMetroPorHectarea', type='decimal'),
    Field('CarpetaBPCarRaleoAlturaEstimada', type="integer"),
    Field('CarpetaBPCarRaleoDensidad', type="decimal"),
    Field('CarpetaBPCarRaleoSuperficieRaleo', type="decimal"),
    Field('CarpetaBPCarRaleoRodalEdad', type="integer"),
    Field('CarpetaBPCarRaleoSupEfectivaAPodar', type="decimal"),
    Field('EspecieGeneroCarRaleoCodEspecie', db2.EspecieGenero.EspecieGeneroEspecie),
    Field('EspecieGeneroCarRaleoCodGenero', db2.EspecieGenero.EspecieGeneroGenero),
    Field('CarpetaBNPropietarioFax', type="string"),
    Field('EspecieGeneroCarRaleoEspecieNombre', db2.EspecieGeneroNombre.EspecieGeneroNombreEspecie),
    Field('EspecieGeneroCarRaleoGeneroNombre', db2.EspecieGeneroNombre.EspecieGeneroNombreGenero),
    primarykey=['CarpetaBPId','CarpetaBPCarRaleoId'],
    migrate=False
)

"""
CarpetaBPGrupoDeSueloPorPadron
	CarpetaBPId,decimal
	CarpetaBPGrupoDeSueloPorPadronNroPadron,decimal
"""

db2.define_table('CarpetaBPGrupoDeSueloPorPadron',
    Field('CarpetaBPId', db2.CarpetaBP.CarpetaBPId),
    Field('CarpetaBPGrupoDeSueloPorPadronNroPadron', type='decimal'),
    primarykey=['CarpetaBPId','CarpetaBPGrupoDeSueloPorPadronNroPadron'],
    migrate=False
)

"""
CarpetaBPGrupoDeSueloPorPadronGrupoDeSue
	CarpetaBPId,decimal
	CarpetaBPGrupoDeSueloPorPadronNroPadron,decimal
	TipoSueloId,char
	CarpetaBPGrupoDeSueloPorPadronGrupoDeSue,decimal
"""

db2.define_table('CarpetaBPGrupoDeSueloPorPadronGrupoDeSue',
    Field('CarpetaBPId', db2.CarpetaBPGrupoDeSueloPorPadron.CarpetaBPId),
    Field('CarpetaBPGrupoDeSueloPorPadronNroPadron', db2.CarpetaBPGrupoDeSueloPorPadron.CarpetaBPGrupoDeSueloPorPadronNroPadron),
    Field('TipoSueloId', type='string'),
    Field('CarpetaBPGrupoDeSueloPorPadronGrupoDeSue', type='decimal'),
    primarykey=['CarpetaBPId','CarpetaBPGrupoDeSueloPorPadronNroPadron'],
    migrate=False
)

"""
CarpetaBPObjForestacion
	CarpetaBPId,decimal
	CarpetaBPObjForestacionId,smallint
"""

db2.define_table('CarpetaBPObjForestacion',
    Field('CarpetaBPId', db2.CarpetaBP.CarpetaBPId),
    Field('CarpetaBPObjForestacionId', type='integer'),
    primarykey=['CarpetaBPId','CarpetaBPObjForestacionId'],
    migrate=False
)

""" 
CarpetaBPPadron
	CarpetaBPId,decimal
	CarpetaBPPadronId,decimal
	CarpetaBPPadronSupBN,decimal
	CarpetaBPPadronSupBP,decimal
	EspecieGeneroPadronGeneroNombre,char
	EspecieGeneroPadronEspecieNombre,char
	EspecieGeneroPadronCodGenero,char
	EspecieGeneroPadronCodEspecie,decimal
	CarpetaBPPadronPlantacionAnio,smallint
	CarpetaBPPadronDensidadPlantacion,decimal
	CarpetaBPPadronSupEfectiva,decimal
	CarpetaBPPadronSupTotal,decimal
"""

db2.define_table('CarpetaBPPadron',
    Field('CarpetaBPId', db2.CarpetaBP.CarpetaBPId),
    Field('CarpetaBPPadronId', type='decimal'),
    Field('CarpetaBPPadronSupBN', type='decimal'),
    Field('CarpetaBPPadronSupBP', type='decimal'),
    Field('EspecieGeneroPadronGeneroNombre', db2.EspecieGeneroNombre.EspecieGeneroNombreGenero),
    Field('EspecieGeneroPadronEspecieNombre', db2.EspecieGeneroNombre.EspecieGeneroNombreEspecie),
    Field('EspecieGeneroPadronCodGenero', db2.EspecieGenero.EspecieGeneroGenero),
    Field('EspecieGeneroPadronCodEspecie', db2.EspecieGenero.EspecieGeneroEspecie),
    Field('CarpetaBPPadronPlantacionAnio', type='integer'),
    Field('CarpetaBPPadronDensidadPlantacion', type='decimal'),
    Field('CarpetaBPPadronSupEfectiva', type='decimal'),
    Field('CarpetaBPPadronSupTotal', type='decimal'),
    primarykey=['CarpetaBPId','CarpetaBPPadronId','EspecieGeneroPadronGeneroNombre','EspecieGeneroPadronEspecieNombre','CarpetaBPPadronPlantacionAnio'],
    migrate=False
)

"""
CarpetaBPProgFor
	CarpetaBPId,decimal
	CarpetaBPProgForId,decimal
	CarpetaBPProgForDensidadPlantacion,decimal
	CarpetaBPProgForSupTotal,decimal
	CarpetaBPProgForPadron,decimal
	EspecieGeneroProgForEspecieNombre,char
	EspecieGeneroProgForGeneroNombre,char
	EspecieGeneroProgForCodEspecie,decimal
	EspecieGeneroProgForCodGenero,char
	CarpetaBPProgForSupAfectada,decimal
	CarpetaBPProgForSupEfectiva,decimal
	CarpetaBPProgForPlantacionAnio,smallint
"""

db2.define_table('CarpetaBPProgFor',
    Field('CarpetaBPId', db2.CarpetaBP.CarpetaBPId),
    Field('CarpetaBPProgForId', type='decimal'),
    Field('CarpetaBPProgForDensidadPlantacion', type='decimal'),
    Field('CarpetaBPProgForSupTotal', type='decimal'),
    Field('CarpetaBPProgForPadron', type='decimal'),
    Field('EspecieGeneroProgForEspecieNombre', db2.EspecieGeneroNombre.EspecieGeneroNombreEspecie),
    Field('EspecieGeneroProgForGeneroNombre', db2.EspecieGeneroNombre.EspecieGeneroNombreGenero),
    Field('EspecieGeneroProgForCodEspecie', db2.EspecieGenero.EspecieGeneroEspecie),
    Field('EspecieGeneroProgForCodGenero', db2.EspecieGenero.EspecieGeneroGenero),
    Field('CarpetaBPProgForSupAfectada', type='decimal'),
    Field('CarpetaBPProgForSupEfectiva', type='decimal'),
    Field('CarpetaBPProgForPlantacionAnio', type='integer'),
    primarykey=['CarpetaBPId','CarpetaBPProgForId'],
    migrate=False
)

"""
CarpetaBPTitular
	CarpetaBPId,decimal
	CarpetaBPTitularCI,int
	CarpetaBPTitularNombre,char
	CarpetaBPTitularDir,char
	CarpetaBPTitularTelefono,char
	CarpetaBPTitularFax,char
	CarpetaBPTitularCelular,char
	CarpetaBPTitularMail,char
	CarpetaBPTitularCiudad,char
	CarpetaBPTitularDep,char
	CarpetaBPTitularOtros,char
	CarpetaBPTitularEsUsufructurario,bit
	CarpetaBPTitularEsPromComprador,bit
	CarpetaBPTitularEsComodatario,bit
	CarpetaBPTitularEsArrendatario,bit
	CarpetaBPTitularEsPropietario,bit
	DGFTitularEnCalidadDeId,smallint
"""

db2.define_table('CarpetaBPTitular',
    Field('CarpetaBPId', db2.CarpetaBP.CarpetaBPId),
    Field('CarpetaBPTitularCI', type='integer'),
    Field('CarpetaBPTitularNombre', type='string'),
    Field('CarpetaBPTitularDir', type='string'),
    Field('CarpetaBPTitularTelefono', type='string'),
    Field('CarpetaBPTitularFax', type='string'),
    Field('CarpetaBPTitularCelular', type='string'),
    Field('CarpetaBPTitularMail', type='string'),
    Field('CarpetaBPTitularCiudad', type='string'),
    Field('CarpetaBPTitularDep', db2.Departamentos.DepartamentosId),
    Field('CarpetaBPTitularOtros', type='string'),
    Field('CarpetaBPTitularEsUsufructurario', type='boolean'), #ver
    Field('CarpetaBPTitularEsPromComprador', type='boolean'), #ver    
    Field('CarpetaBPTitularEsComodatario', type='boolean'), #ver
    Field('CarpetaBPTitularEsArrendatario', type='boolean'), #ver
    Field('CarpetaBPTitularEsPropietario', type='boolean'), #ver
    Field('DGFTitularEnCalidadDeId', db2.DGFTitularEnCalidadDe.DGFTitularEnCalidadDeId),
    primarykey=['CarpetaBPId','CarpetaBPTitularCI'],
    migrate=False
)

"""
Departamentos
	DepartamentosId,char
	DepartamentosNombre,char
"""

db2.define_table('Departamentos',
    Field('DepartamentosId', type='decimal'),
    Field('DepartamentosNombre', type='string'),
    primarykey=['DepartamentosId'],
    migrate=False
)

"""
DGFTitularEnCalidadDe
	DGFTitularEnCalidadDeId,smallint
	DGFTitularEnCalidadDeDescripcion,char
"""

db2.define_table('DGFTitularEnCalidadDe',
    Field('DGFTitularEnCalidadDeId', type='integer'),
    Field('DGFTitularEnCalidadDeDescripcion', type='string'),
    primarykey=['DGFTitularEnCalidadDeId'],
    migrate=False
)

"""
Especie
	EspecieId,decimal
	GeneroId,char
	GeneroNombre,char
	EspecieNombre,char
"""

db2.define_table('Especie',
    Field('EspecieId', type='decimal'),
    Field('GeneroId', db2.Genero.GeneroId),
    Field('GeneroNombre', db2.Genero.GeneroNombre),
    Field('EspecieNombre', type='string'),
    primarykey=['EspecieId','GeneroId'],
    migrate=False
)

"""
EspecieBP
	EspecieBPCarpeta,decimal
	EspecieBPPadron,decimal
	EspecieBPFechaHoraRegistroDig,datetime
	EspecieBPUsuario,char
	EspecieBPUsuarioUltimaModif,char
	EspecieBPFechaHoraUltimaModif,datetime
"""

db2.define_table('EspecieBP',
    Field('EspecieBPCarpeta', type='decimal'),
    Field('EspecieBPPadron', type='decimal'),
    Field('EspecieBPFechaHoraRegistroDig', type='datetime'),
    Field('EspecieBPUsuario', type='string'),
    Field('EspecieBPUsuarioUltimaModif', type='string'),
    Field('EspecieBPFechaHoraUltimaModif', type='datetime'),
    primarykey=['EspecieBPCarpeta','EspecieBPPadron'],
    migrate=False
)

"""
EspecieGenero
	EspecieGeneroEspecie,decimal
	EspecieGeneroGenero,char
	EspecieGeneroEspecieNombre,char
	EspecieGeneroGeneroNombre,char
"""

db2.define_table('EspecieGenero',
    Field('EspecieGeneroEspecie', type='decimal'),
    Field('EspecieGeneroGenero', type='string'),
    Field('EspecieGeneroEspecieNombre', type='string'),
    Field('EspecieGeneroGeneroNombre', type='string'),
    primarykey=['EspecieGeneroEspecie','EspecieGeneroGenero'],
    migrate=False
)

 
""" 
EspecieGeneroNombre
	EspecieGeneroNombreGenero,char
	EspecieGeneroNombreEspecie,char
""" 

db2.define_table('EspecieGeneroNombre',
    Field('EspecieGeneroNombreGenero', type='string'),
    Field('EspecieGeneroNombreEspecie', type='string'),
    primarykey=['EspecieGeneroNombreGenero','EspecieGeneroNombreEspecie'],
    migrate=False
)

"""
Genero
	GeneroId,char
	GeneroNombre,char
"""

db2.define_table('Genero',
    Field('GeneroId', type='string'),
    Field('GeneroNombre', type='string'),
    primarykey=['GeneroId','GeneroNombre'],
    migrate=False
)

"""
GrupoDeSuelos
	GrupoDeSuelosId,char
	GrupoDeSuelosNombre,char
"""

db2.define_table('GrupoDeSuelos',
    Field('GrupoDeSuelosId', type='string'),
    Field('GrupoDeSuelosNombre', type='string'),
    primarykey=['GrupoDeSuelosId'],
    migrate=False
)

"""
Operacion
	OperacionId,smallint
	OperacionNombre,char
"""

db2.define_table('Operacion',
    Field('OperacionId', db2.Operacion.OperacionId),
    Field('OperacionNombre', type='string'),
    primarykey=['OperacionId'],
    migrate=False
)

"""
PlanDeManejoBN
	PlanDeManejoBNId,decimal
	CarpetaBNId,char
	OperacionId,smallint
	PlanDeManejoBNUsuario,char
	PlanDeManejoBNFechaHoraRegistroDig,datetime
"""

db2.define_table('PlanDeManejoBN',
    Field('PlanDeManejoBNId', db2.PlanDeManejoBN.PlanDeManejoBNId),
    Field('CarpetaBNId', type='string'),
    Field('OperacionId', type='integer'),
    Field('PlanDeManejoBNUsuario', type='string'),
    Field('PlanDeManejoBNFechaHoraRegistroDig', type='datetime'),
    primarykey=['PlanDeManejoBNId'],
    migrate=False
)
 
"""
PlanDeManejoBNPadron
	PlanDeManejoBNId,decimal
	FormPlanManejoBNCarpeta,char
	FormPlanManejoBNPadron,decimal
	PlanDeManejoBNPadronSupACortar,decimal
	PlanDeManejoBNPadronToneladasEstimadas,smallint
	PlanDeManejoBNPadronPlazo,smallint
	PlanDeManejoBNPadronFundamentacion,varchar
"""


db2.define_table('PlanDeManejoBNPadron',
    Field('PlanDeManejoBNId', type='decimal'),
    Field('FormPlanManejoBNCarpeta', db2.CarpetaBN.CarpetaBNId),
    Field('FormPlanManejoBNPadron', type='decimal'),
    Field('PlanDeManejoBNPadronSupACortar', type='decimal'),
    Field('PlanDeManejoBNPadronToneladasEstimadas', type='integer'),
    Field('PlanDeManejoBNPadronPlazo', type='integer'),
    Field('PlanDeManejoBNPadronFundamentacion', type='string'),
    primarykey=['PlanDeManejoBNId','FormPlanManejoBNCarpeta','FormPlanManejoBNPadron'],
    migrate=False
)

"""
TempCarpetaBN
	TempCarpetaBNId,char
	TempCarpetaBNFechaRegistro,datetime
	TempCarpetaBNNombreEstabl,char
	CarpetaBNDepartamentoEstabl,char
	TempCarpetaBNSeccionCatastralEstabl,smallint
	TempCarpetaBNSeccionJudicialEstabl,smallint
	TempCarpetaBNSeccionPolicialEstabl,smallint
	TempCarpetaBNParajeEstabl,char
	TempCarpetaBNCIRepLegal,int
	TempCarpetaBNNombreRepLegal,char
	TempCarpetaBNDireccionRepLegal,char
	CarpetaBNDepartamentoRepLegal,char
	TempCarpetaBNTelefonoRepLegal,char
	TempCarpetaBNCelularRepLegal,char
	TempCarpetaBNFaxRepLegal,char
	TempCarpetaBNMailRepLegal,char
	TempCarpetaBNCITecnico,int
	TempCarpetaBNTipoProfesional,bit
	TempCarpetaBNNombreTecnico,char
	TempCarpetaBNDireccionTecnico,char
	TempCarpetaBNTelefonoTecnico,char
	TempCarpetaBNCelularTecnico,char
	TempCarpetaBNFaxTecnico,char
	TempCarpetaBNMailTecnico,char
	AsociacionesId,smallint
	TempCarpetaBNTipoRebrote,smallint
	TempCarpetaBNEstadoSanitario,varchar
	TempCarpetaBNInvEspExoticas,bit
	TempCarpetaBNIncForestales,bit
	TempCarpetaBNAccionesAntropicas,varchar
	TempCarpetaBNAreaArboladaTotal,decimal
	TempCarpetaBNAreaArboladaBN,decimal
	TempCarpetaBNAreaArboladaBP,decimal
	TempCarpetaBNFechaHoraRegistroDig,datetime
	TempCarpetaBNUsuario,char
	TempCarpetaBNNroCarpeta,int
"""

db2.define_table('TempCarpetaBN',
    Field('TempCarpetaBNId', db2.TempCarpetaBN.TempCarpetaBNId),
    Field('TempCarpetaBNFechaRegistro', type='datetime'),
    Field('TempCarpetaBNNombreEstabl', type='string'),
    Field('CarpetaBNDepartamentoEstabl', db2.Departamentos.DepartamentosId),
    Field('TempCarpetaBNSeccionCatastralEstabl', type='integer'),
    Field('TempCarpetaBNSeccionJudicialEstabl', type='integer'),
    Field('TempCarpetaBNSeccionPolicialEstabl', type='integer'),
    Field('TempCarpetaBNParajeEstabl', type='string'),
    Field('TempCarpetaBNCIRepLegal', type='integer'),
    Field('TempCarpetaBNNombreRepLegal', type='string'),
    Field('TempCarpetaBNDireccionRepLegal', type='string'),
    Field('CarpetaBNDepartamentoRepLegal', db2.Departamentos.DepartamentosId),
    Field('TempCarpetaBNTelefonoRepLegal', type='string'),
    Field('TempCarpetaBNCelularRepLegal', type='string'),
    Field('TempCarpetaBNFaxRepLegal', type='string'),
    Field('TempCarpetaBNMailRepLegal', type='string'),
    Field('TempCarpetaBNCITecnico', type='integer'),
    Field('TempCarpetaBNTipoProfesional', type='boolean'), #ver
    Field('TempCarpetaBNNombreTecnico', type='string'),
    Field('TempCarpetaBNDireccionTecnico', type='string'),
    Field('TempCarpetaBNTelefonoTecnico', type='string'),
    Field('TempCarpetaBNCelularTecnico', type='string'),
    Field('TempCarpetaBNFaxTecnico', type='string'),
    Field('TempCarpetaBNMailTecnico', type='string'),
    Field('AsociacionesId', db2.Asociaciones.AsociacionesId),
    Field('TempCarpetaBNTipoRebrote', type='integer'),
    Field('TempCarpetaBNEstadoSanitario', type='string'),
    Field('TempCarpetaBNInvEspExoticas', type='boolean'), #ver
    Field('TempCarpetaBNIncForestales', type='boolean'), #ver
    Field('TempCarpetaBNAccionesAntropicas', type='string'),
    Field('TempCarpetaBNAreaArboladaTotal', type='decimal'),
    Field('TempCarpetaBNAreaArboladaBN', type='decimal'),
    Field('TempCarpetaBNAreaArboladaBP', type='decimal'),
    Field('TempCarpetaBNFechaHoraRegistroDig', type='datetime'),
    Field('TempCarpetaBNFechaHoraRegistroDig', type='string'),
    Field('TempCarpetaBNFechaHoraRegistroDig', type='integer'),
    primarykey=['TempCarpetaBNId'],
    migrate=False
)

""" 
TempCarpetaBNPadron
	TempCarpetaBNId,char
	TempCarpetaBNPadronId,decimal
	TempCarpetaBNPadronSeccJudicial,smallint
	TempCarpetaBNPadronSupBN,decimal
	TempCarpetaBNPadronSupBP,decimal
	TempCarpetaBNPadronTotal,decimal
	TempCarpetaBNPadronSupPadron,decimal
	TempCarpetaBNPadronSeccPolicial,smallint
"""

db2.define_table('TempCarpetaBNPadron',
    Field('TempCarpetaBNId', db2.TempCarpetaBN.TempCarpetaBNId),
    Field('TempCarpetaBNPadronId', type='decimal'),
    Field('TempCarpetaBNPadronSeccJudicial', type='integer'),
    Field('TempCarpetaBNPadronSupBN', type='decimal'),
    Field('TempCarpetaBNPadronSupBP', type='decimal'),
    Field('TempCarpetaBNPadronTotal', type='decimal'),
    Field('TempCarpetaBNPadronSupPadron', type='decimal'),
    Field('TempCarpetaBNPadronSeccPolicial', type='integer'),
    primarykey=['PlanDeManejoBNId','TempCarpetaBNPadronId','TempCarpetaBNPadronSeccJudicial'],
    migrate=False
)

"""
TempCarpetaBNPropietario
	TempCarpetaBNId,char
	TempCarpetaBNPropietarioCI,int
	TempCarpetaBNPropietarioNombre,char
	TempCarpetaBNPropietarioRazonSocial,char
	TempCarpetaBNPropietarioRUT,char
	TempCarpetaBNPropietarioDireccion,char
	TempCarpetaBNPropietarioCuidad,char
	TempCarpetaBNPropietarioTelefono,char
	TempCarpetaBNPropietarioCelular,char
	TempCarpetaBNPropietarioFax,char
	TempCarpetaBNPropietarioMail,char
	TempCarpetaBNPropietarioDep,char
"""

db2.define_table('TempCarpetaBNPropietario',
    Field('TempCarpetaBNId', db2.CarpetaBN),
    Field('TempCarpetaBNPropietarioCI', type='integer'),
    Field('TempCarpetaBNPropietarioNombre', type='string'),
    Field('TempCarpetaBNPropietarioRazonSocial', type='string'),
    Field('TempCarpetaBNPropietarioRUT', type="string"),
    Field('TempCarpetaBNPropietarioDireccion', type="string"),
    Field('TempCarpetaBNPropietarioCuidad', type="string"),
    Field('TempCarpetaBNPropietarioTelefono', type="string"),
    Field('TempCarpetaBNPropietarioCelular', type="string"),
    Field('TempCarpetaBNPropietarioFax', type="string"),
    Field('TempCarpetaBNPropietarioMail', type="string"),
    Field('TempCarpetaBNPropietarioDep', db2.Departamentos.DepartamentosId),
    primarykey=['CarpetaBNId','CarpetaBNPropietarioCI'],
    migrate=False
)


"""
TipoSuelo
	TipoSueloId,char
	TipoSueloNombre,char
"""

db2.define_table('TipoSuelo',
    Field('TipoSueloId', db2.TipoSuelo.TipoSueloId),
    Field('TipoSueloNombre', type='string'),
    primarykey=['TipoSueloId'],
    migrate=False
)

"""
Usuario
	UsuarioNombre,char
	UsuarioNombreApellido,char
""" 

db2.define_table('Usuario',
    Field('UsuarioNombre', type='string'),
    Field('UsuarioNombreApellido', type='string'),
    primarykey=['UsuarioNombre'],
    migrate=False
) 
 
""" 
PK
Asociaciones
	AsociacionesId
Calificacion
	CalificacionId
CalificacionBP
	CalificacionBPCarpeta
	CalificacionBPPadron
	CalificacionId
CarpetaBN
	CarpetaBNId
CarpetaBNPadron
	CarpetaBNId
	CarpetaBNPadronId
	CarpetaBNPadronSeccJudicial
CarpetaBNPropietario
	CarpetaBNId
	CarpetaBNPropietarioCI
CarpetaBP
	CarpetaBPId
CarpetaBPCarRaleo
	CarpetaBPId
	CarpetaBPCarRaleoId
CarpetaBPGrupoDeSueloPorPadron
	CarpetaBPId
	CarpetaBPGrupoDeSueloPorPadronNroPadron
CarpetaBPGrupoDeSueloPorPadronGrupoDeSue
	CarpetaBPId
	CarpetaBPGrupoDeSueloPorPadronNroPadron
	TipoSueloId
CarpetaBPObjForestacion
	CarpetaBPId
	CarpetaBPObjForestacionId
CarpetaBPPadron
	CarpetaBPId
	CarpetaBPPadronId
	EspecieGeneroPadronGeneroNombre
	EspecieGeneroPadronEspecieNombre
	CarpetaBPPadronPlantacionAnio
CarpetaBPProgFor
	CarpetaBPId
	CarpetaBPProgForId
CarpetaBPTitular
	CarpetaBPId
	CarpetaBPTitularCI
Departamentos
	DepartamentosId
DGFTitularEnCalidadDe
	DGFTitularEnCalidadDeId
Especie
	EspecieId
	GeneroId
EspecieBP
	EspecieBPCarpeta
	EspecieBPPadron
EspecieGenero
	EspecieGeneroEspecie
	EspecieGeneroGenero
EspecieGeneroNombre
	EspecieGeneroNombreGenero
	EspecieGeneroNombreEspecie
Genero
	GeneroId
	GeneroNombre
GrupoDeSuelos
	GrupoDeSuelosId
Operacion
	OperacionId
PlanDeManejoBN
	PlanDeManejoBNId
PlanDeManejoBNPadron
	PlanDeManejoBNId
	FormPlanManejoBNCarpeta
	FormPlanManejoBNPadron
TempCarpetaBN
	TempCarpetaBNId
TempCarpetaBNPadron
	TempCarpetaBNId
	TempCarpetaBNPadronId
	TempCarpetaBNPadronSeccJudicial
TempCarpetaBNPropietario
	TempCarpetaBNId
	TempCarpetaBNPropietarioCI
TipoSuelo
	TipoSueloId
Usuario
	UsuarioNombre
FK
Asociaciones
	AsociacionesId,CarpetaBN,AsociacionesId
	AsociacionesId,TempCarpetaBN,AsociacionesId
Calificacion
	CalificacionId,CalificacionBP,CalificacionId
CalificacionBP
CarpetaBN
	CarpetaBNId,CarpetaBNPadron,CarpetaBNId
	CarpetaBNId,CarpetaBNPropietario,CarpetaBNId
	CarpetaBNId,PlanDeManejoBNPadron,FormPlanManejoBNCarpeta
CarpetaBNPadron
CarpetaBNPropietario
CarpetaBP
	CarpetaBPId,CarpetaBPCarRaleo,CarpetaBPId
	CarpetaBPId,CarpetaBPGrupoDeSueloPorPadron,CarpetaBPId
	CarpetaBPId,CarpetaBPObjForestacion,CarpetaBPId
	CarpetaBPId,CarpetaBPPadron,CarpetaBPId
	CarpetaBPId,CarpetaBPProgFor,CarpetaBPId
	CarpetaBPId,CarpetaBPTitular,CarpetaBPId
CarpetaBPCarRaleo
CarpetaBPGrupoDeSueloPorPadron
	CarpetaBPId,CarpetaBPGrupoDeSueloPorPadronGrupoDeSue,CarpetaBPId
	CarpetaBPGrupoDeSueloPorPadronNroPadron,CarpetaBPGrupoDeSueloPorPadronGrupoDeSue,CarpetaBPGrupoDeSueloPorPadronNroPadron
CarpetaBPGrupoDeSueloPorPadronGrupoDeSue
CarpetaBPObjForestacion
CarpetaBPPadron
CarpetaBPProgFor
CarpetaBPTitular
Departamentos
	DepartamentosId,CarpetaBN,CarpetaBNDepartamentoEstabl
	DepartamentosId,CarpetaBN,CarpetaBNDepartamentoRepLegal
	DepartamentosId,CarpetaBNPropietario,CarpetaBNPropietarioDep
	DepartamentosId,CarpetaBP,CarpetaBPDepartamentoEstabl
	DepartamentosId,CarpetaBP,CarpetaBPDepartamentoProductor
	DepartamentosId,CarpetaBP,CarpetaBPDepartamentoRepLegal
	DepartamentosId,CarpetaBPTitular,CarpetaBPTitularDep
	DepartamentosId,TempCarpetaBN,CarpetaBNDepartamentoEstabl
	DepartamentosId,TempCarpetaBN,CarpetaBNDepartamentoRepLegal
	DepartamentosId,TempCarpetaBNPropietario,TempCarpetaBNPropietarioDep
DGFTitularEnCalidadDe
	DGFTitularEnCalidadDeId,CarpetaBPTitular,DGFTitularEnCalidadDeId
Especie
EspecieBP
EspecieGenero
	EspecieGeneroEspecie,CarpetaBPCarRaleo,EspecieGeneroCarRaleoCodEspecie
	EspecieGeneroGenero,CarpetaBPCarRaleo,EspecieGeneroCarRaleoCodGenero
	EspecieGeneroEspecie,CarpetaBPPadron,EspecieGeneroPadronCodEspecie
	EspecieGeneroGenero,CarpetaBPPadron,EspecieGeneroPadronCodGenero
	EspecieGeneroEspecie,CarpetaBPProgFor,EspecieGeneroProgForCodEspecie
	EspecieGeneroGenero,CarpetaBPProgFor,EspecieGeneroProgForCodGenero
EspecieGeneroNombre
	EspecieGeneroNombreGenero,CarpetaBPCarRaleo,EspecieGeneroCarRaleoGeneroNombre
	EspecieGeneroNombreEspecie,CarpetaBPCarRaleo,EspecieGeneroCarRaleoEspecieNombre
	EspecieGeneroNombreGenero,CarpetaBPPadron,EspecieGeneroPadronGeneroNombre
	EspecieGeneroNombreEspecie,CarpetaBPPadron,EspecieGeneroPadronEspecieNombre
	EspecieGeneroNombreGenero,CarpetaBPProgFor,EspecieGeneroProgForGeneroNombre
	EspecieGeneroNombreEspecie,CarpetaBPProgFor,EspecieGeneroProgForEspecieNombre
Genero
	GeneroId,Especie,GeneroId
	GeneroNombre,Especie,GeneroNombre
GrupoDeSuelos
Operacion
	OperacionId,PlanDeManejoBN,OperacionId
PlanDeManejoBN
	PlanDeManejoBNId,PlanDeManejoBNPadron,PlanDeManejoBNId
PlanDeManejoBNPadron
TempCarpetaBN
	TempCarpetaBNId,TempCarpetaBNPadron,TempCarpetaBNId
	TempCarpetaBNId,TempCarpetaBNPropietario,TempCarpetaBNId
TempCarpetaBNPadron
TempCarpetaBNPropietario
TipoSuelo
	TipoSueloId,CarpetaBPGrupoDeSueloPorPadronGrupoDeSue,TipoSueloId
Usuario
"""