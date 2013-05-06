"""
db.define_table('Asociaciones',
    Field('AsociacionesId', type='integer'),
    Field('AsociacionesDescripcion', type='string'),
    primarykey=['AsociacionesId'],
    migrate=False
)

db.define_table('Calificacion',
    Field('CalificacionId', type='integer'),
    Field('CalificacionDescripcion', type="string"),
    primarykey=['CalificacionId'],
    migrate=False
)

db.define_table('CalificacionBP',
    Field('CalificacionBPCarpeta', type='integer'),
    Field('CalificacionBPPadron', type='integer'),
    Field('CalificacionBPMatricula', type='string'),
    Field('CalificacionId', type='integer'),
    Field('CalifBPFechaHoraRegistroDig', type="datetime"),
    Field('CalifBPUsuario', type="string"),
    Field('CalifBPUsuarioUltimaModif', type="string"),
    Field('CalifBPFechaHoraUltimaModif', type="datetime"),
    primarykey=['CalificacionBPCarpeta','CalificacionBPPadron','CalificacionId'],
    migrate=False
)

db.define_table('CarpetaBN',
    Field('CarpetaBNId', type='integer'),
    Field('CarpetaBNFechaRegistro', type='datetime'),
    Field('CarpetaBNNombreEstabl', type='string'),
    #Field('CarpetaBNDepartamentoEstabl', db.Departamentos.DepartamentosId),
    Field('CarpetaBNDepartamentoEstabl', type='integer'),
    Field('CarpetaBNSeccionCatastralEstabl', type="integer"),
    Field('CarpetaBNSeccionJudicialEstabl', type="integer"),
    Field('CarpetaBNSeccionPolicialEstabl', type="integer"),
    Field('CarpetaBNParajeEstabl', type="string"),
    Field('CarpetaBNCIRepLegal', type="integer"),
    Field('CarpetaBNNombreRepLegal', type="string"),
    Field('CarpetaBNDireccionRepLegal', type="string"),
    #Field('CarpetaBNDepartamentoRepLegal', db.Departamentos.DepartamentosId),
    Field('CarpetaBNDepartamentoRepLegal', type="integer"),
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
    Field('CarpetaBNAreaArboladaTotal', type='double'),
    Field('CarpetaBNAreaArboladaBN', type='double'),
    Field('CarpetaBNAreaArboladaBP', type='double'),
    Field('CarpetaBNFechaHoraRegistroDig', type='datetime'),
    Field('CarpetaBNUsuario', type="string"),
    #Field('AsociacionesId', db.Asociaciones.AsociacionesId),
    Field('AsociacionesId', type="integer"),
    Field('CarpetaBNNroCarpeta', type="integer"),
    primarykey=['CarpetaBNId'],
    migrate=False
)

db.define_table('CarpetaBNPadron',
    #Field('CarpetaBNId', db.CarpetaBN.CarpetaBNId),
    Field('CarpetaBNId', type='integer'),
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

db.define_table('CarpetaBNPropietario',
    #Field('CarpetaBNId', db.CarpetaBN.CarpetaBNId),
    Field('CarpetaBNId', type='integer'),    
    Field('CarpetaBNPropietarioCI', type='integer'),
    Field('CarpetaBNPropietarioNombre', type='string'),
    Field('CarpetaBNPropietarioRazonSocial', type='string'),
    Field('CarpetaBNPropietarioRUT', type="string"),
    Field('CarpetaBNPropietarioDireccion', type="string"),
    #Field('CarpetaBNPropietarioDep', db.Departamentos.DepartamentosId),
    Field('CarpetaBNPropietarioDep', type='integer'),
    Field('CarpetaBNPropietarioCiudad', type="string"),
    Field('CarpetaBNPropietarioTelefono', type="string"),
    Field('CarpetaBNPropietarioCelular', type="string"),
    Field('CarpetaBNPropietarioFax', type="string"),
    Field('CarpetaBNPropietarioMail', type="string"),
    primarykey=['CarpetaBNId','CarpetaBNPropietarioCI'],
    migrate=False
)

db.define_table('CarpetaBP',
    Field('CarpetaBPId', type='integer'),
    Field('CarpetaBPFechaRegistro', type='datetime'),
    Field('CarpetaBPRazonSocial', type='string'),
    Field('CarpetaBPRUT', type="string"),
    Field('CarpetaBPDireccionProductor', type="string"),
    #Field('CarpetaBPDepartamentoProductor', db.Departamentos),
    Field('CarpetaBPDepartamentoProductor', type='integer'),    
    Field('CarpetaBPCuidadProductor', type="string"),
    Field('CarpetaBPTelefonoProductor', type="string"),
    Field('CarpetaBPCelularProductor', type="string"),
    Field('CarpetaBPFaxProductor', type="string"),
    Field('CarpetaBPMailProductor', type="string"),
    Field('CarpetaBPNombreEstabl', type="string"),
    #Field('CarpetaBPDepartamentoEstabl', db.Departamentos),
    Field('CarpetaBPDepartamentoEstabl', type='integer'),    
    Field('CarpetaBPSeccionCatastralEstabl', type="integer"),
    Field('CarpetaBPSeccionJudicialEstabl', type="integer"),
    Field('CarpetaBPSeccionPolicialEstabl', type="integer"),
    Field('CarpetaBPCIRepLegal', type="integer"),
    Field('CarpetaBPNombreRepLegal', type="string"),
    Field('CarpetaBPDireccionRepLegal', type="string"),
    #Field('CarpetaBPDepartamentoRepLegal', db.Departamentos),
    Field('CarpetaBPDepartamentoRepLegal', type="integer"),    
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
    Field('CarpetaBPFechaHoraRegistroDig', type='datetime'),
    Field('CarpetaBPUsuario', type="string"),
    Field('CarpetaBPFechaHoraUltimaModif', type='datetime'),
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
    Field('CarpetaBPNroCarpeta', type='double'),
    Field('Migrado', type="string"), #ver
    Field('CarpetaBPLongitudGrados', type='double'),
    Field('CarpetaBPLongitudMinutos', type='double'),
    Field('CarpetaBPLongitudSegundos', type='double'),
    Field('CarpetaBPLatitudGrados', type='double'),
    Field('CarpetaBPLatitudMinutos', type='double'),
    Field('CarpetaBPLatitudSegundos', type='double'),
    Field('CarpetaBPProyCortaFinalVolum', type="integer"), # Money??
    Field('CarpetaBPProyCortaFinalFecha', type="string"),
    Field('CarpetaBPExisCortaFinalVolum', type="decimal"),
    Field('CarpetaBPExisCortaFinalFecha', type="string"),
    primarykey=['CarpetaBPId'],
    migrate=False
)

 
db.define_table('CarpetaBPCarRaleo',
    #Field('CarpetaBPId', db.CarpetaBP.CarpetaBPId),
    Field('CarpetaBPId', type='integer'),    
    Field('CarpetaBPCarRaleoId', type='double'),
    Field('CarpetaBPCarRaleoPlantacionAnio', type='integer'),
    Field('CarpetaBPCarRaleoMetroPorHectarea', type='double'),
    Field('CarpetaBPCarRaleoAlturaEstimada', type="integer"),
    Field('CarpetaBPCarRaleoDensidad', type='double'),
    Field('CarpetaBPCarRaleoSuperficieRaleo', type='double'),
    Field('CarpetaBPCarRaleoRodalEdad', type="integer"),
    Field('CarpetaBPCarRaleoSupEfectivaAPodar', type='double'),
    #Field('EspecieGeneroCarRaleoCodEspecie', db.EspecieGenero),
    #Field('EspecieGeneroCarRaleoCodGenero', db.EspecieGenero),
    Field('EspecieGeneroCarRaleoCodEspecie', type="integer"),
    Field('EspecieGeneroCarRaleoCodGenero', type="integer"),
    Field('CarpetaBNPropietarioFax', type="string"),
    #Field('EspecieGeneroCarRaleoEspecieNombre', db.EspecieGeneroNombre),
    #Field('EspecieGeneroCarRaleoGeneroNombre', db.EspecieGeneroNombre),
    Field('EspecieGeneroCarRaleoEspecieNombre', type="integer"),
    Field('EspecieGeneroCarRaleoGeneroNombre', type="integer"),
    primarykey=['CarpetaBPId','CarpetaBPCarRaleoId'],
    migrate=False
)

db.define_table('CarpetaBPGrupoDeSueloPorPadron',
    #Field('CarpetaBPId', db.CarpetaBP.CarpetaBPId),
    Field('CarpetaBPId', type="integer"),
    Field('CarpetaBPGrupoDeSueloPorPadronNroPadron', type='double'),
    primarykey=['CarpetaBPId','CarpetaBPGrupoDeSueloPorPadronNroPadron'],
    migrate=False
)

db.define_table('CarpetaBPGrupoDeSueloPorPadronGrupoDeSue',
    #Field('CarpetaBPId', db.CarpetaBPGrupoDeSueloPorPadron.CarpetaBPId),
    #Field('CarpetaBPGrupoDeSueloPorPadronNroPadron', db.CarpetaBPGrupoDeSueloPorPadron.CarpetaBPGrupoDeSueloPorPadronNroPadron),
    Field('CarpetaBPId', type="integer"),
    Field('CarpetaBPGrupoDeSueloPorPadronNroPadron', type="integer"),
    Field('TipoSueloId', type='string'),
    Field('CarpetaBPGrupoDeSueloPorPadronGrupoDeSue', type='double'),
    primarykey=['CarpetaBPId','CarpetaBPGrupoDeSueloPorPadronNroPadron'],
    migrate=False
)


db.define_table('CarpetaBPObjForestacion',
    #Field('CarpetaBPId', db.CarpetaBP.CarpetaBPId),
    Field('CarpetaBPId', type='integer'),
    Field('CarpetaBPObjForestacionId', type='integer'),
    primarykey=['CarpetaBPId','CarpetaBPObjForestacionId'],
    migrate=False
)

db.define_table('CarpetaBPPadron',
    #Field('CarpetaBPId', db.CarpetaBP.CarpetaBPId),
    Field('CarpetaBPId', type='integer'),
    Field('CarpetaBPPadronId', type='double'),
    Field('CarpetaBPPadronSupBN', type='double'),
    Field('CarpetaBPPadronSupBP', type='double'),
    Field('EspecieGeneroPadronGeneroNombre', type='string'),
    Field('EspecieGeneroPadronEspecieNombre', type='string'),
    #Field('EspecieGeneroPadronCodGenero', db.EspecieGenero),
    #Field('EspecieGeneroPadronCodEspecie', db.EspecieGenero),
    Field('EspecieGeneroPadronCodGenero', type='integer'),
    Field('EspecieGeneroPadronCodEspecie', type='integer'),
    Field('CarpetaBPPadronPlantacionAnio', type='integer'),
    Field('CarpetaBPPadronDensidadPlantacion', type='double'),
    Field('CarpetaBPPadronSupEfectiva', type='double'),
    Field('CarpetaBPPadronSupTotal', type='double'),
    primarykey=['CarpetaBPId','CarpetaBPPadronId','EspecieGeneroPadronGeneroNombre','EspecieGeneroPadronEspecieNombre','CarpetaBPPadronPlantacionAnio'],
    migrate=False
)

db.define_table('CarpetaBPProgFor',
    #Field('CarpetaBPId', db.CarpetaBP.CarpetaBPId),
    Field('CarpetaBPId', type='integer'),
    Field('CarpetaBPProgForId', type='double'),
    Field('CarpetaBPProgForDensidadPlantacion', type='double'),
    Field('CarpetaBPProgForSupTotal', type='double'),
    Field('CarpetaBPProgForPadron', type='double'),
    Field('EspecieGeneroProgForEspecieNombre', type='string'),
    Field('EspecieGeneroProgForGeneroNombre', type='string'),
    #Field('EspecieGeneroProgForCodEspecie', db.EspecieGenero),
    #Field('EspecieGeneroProgForCodGenero', db.EspecieGenero),
    Field('EspecieGeneroProgForCodEspecie', type='integer'),
    Field('EspecieGeneroProgForCodGenero', type='integer'),
    Field('CarpetaBPProgForSupAfectada', type='double'),
    Field('CarpetaBPProgForSupEfectiva', type='double'),
    Field('CarpetaBPProgForPlantacionAnio', type='integer'),
    primarykey=['CarpetaBPId','CarpetaBPProgForId'],
    migrate=False
)

db.define_table('CarpetaBPTitular',
    #Field('CarpetaBPId', db.CarpetaBP.CarpetaBPId),
    Field('CarpetaBPId', type='integer'),
    Field('CarpetaBPTitularCI', type='integer'),
    Field('CarpetaBPTitularNombre', type='string'),
    Field('CarpetaBPTitularDir', type='string'),
    Field('CarpetaBPTitularTelefono', type='string'),
    Field('CarpetaBPTitularFax', type='string'),
    Field('CarpetaBPTitularCelular', type='string'),
    Field('CarpetaBPTitularMail', type='string'),
    Field('CarpetaBPTitularCiudad', type='string'),
    #Field('CarpetaBPTitularDep', db.Departamentos),
    Field('CarpetaBPTitularDep', type='integer'),
    Field('CarpetaBPTitularOtros', type='string'),
    Field('CarpetaBPTitularEsUsufructurario', type='string'), #ver
    Field('CarpetaBPTitularEsPromComprador', type='string'), #ver    
    Field('CarpetaBPTitularEsComodatario', type='string'), #ver
    Field('CarpetaBPTitularEsArrendatario', type='string'), #ver
    Field('CarpetaBPTitularEsPropietario', type='string'), #ver
    #Field('DGFTitularEnCalidadDeId', db.DGFTitularEnCalidadDe),
    Field('DGFTitularEnCalidadDeId', type='integer'),
    primarykey=['CarpetaBPId','CarpetaBPTitularCI'],
    migrate=False
)

db.define_table('Departamentos',
    Field('DepartamentosId', type='double'),
    Field('DepartamentosNombre', type='string'),
    primarykey=['DepartamentosId'],
    migrate=False
)

db.define_table('DGFTitularEnCalidadDe',
    Field('DGFTitularEnCalidadDeId', type='integer'),
    Field('DGFTitularEnCalidadDeDescripcion', type='string'),
    primarykey=['DGFTitularEnCalidadDeId'],
    migrate=False
)

db.define_table('Especie',
    Field('EspecieId', type='double'),
    Field('GeneroId', type='string'),
    Field('GeneroNombre', type='string'),
    Field('EspecieNombre', type='string'),
    primarykey=['EspecieId','GeneroId'],
    migrate=False
)

db.define_table('EspecieBP',
    Field('EspecieBPCarpeta', type='double'),
    Field('EspecieBPPadron', type='double'),
    Field('EspecieBPFechaHoraRegistroDig', type='datetime'),
    Field('EspecieBPUsuario', type='string'),
    Field('EspecieBPUsuarioUltimaModif', type='string'),
    Field('EspecieBPFechaHoraUltimaModif', type='datetime'),
    primarykey=['EspecieBPCarpeta','EspecieBPPadron'],
    migrate=False
)

db.define_table('EspecieGenero',
    Field('EspecieGeneroEspecie', type='double'),
    Field('EspecieGeneroGenero', type='string'),
    Field('EspecieGeneroEspecieNombre', type='string'),
    Field('EspecieGeneroGeneroNombre', type='string'),
    primarykey=['EspecieGeneroEspecie','EspecieGeneroGenero'],
    migrate=False
)

db.define_table('EspecieGeneroNombre',
    Field('EspecieGeneroNombreGenero', type='string'),
    Field('EspecieGeneroNombreEspecie', type='string'),
    primarykey=['EspecieGeneroNombreGenero','EspecieGeneroNombreEspecie'],
    migrate=False
)

db.define_table('Genero',
    Field('GeneroId', type='string'),
    Field('GeneroNombre', type='string'),
    primarykey=['GeneroId','GeneroNombre'],
    migrate=False
)

db.define_table('GrupoDeSuelos',
    Field('GrupoDeSuelosId', type='string'),
    Field('GrupoDeSuelosNombre', type='string'),
    primarykey=['GrupoDeSuelosId'],
    migrate=False
)

db.define_table('Operacion',
    #Field('OperacionId', db.Operacion.OperacionId),
    Field('OperacionId', type='integer'),
    Field('OperacionNombre', type='string'),
    primarykey=['OperacionId'],
    migrate=False
)

db.define_table('PlanDeManejoBN',
    Field('PlanDeManejoBNId', type='double'),
    Field('CarpetaBNId', type='string'),
    Field('OperacionId', type='integer'),
    Field('PlanDeManejoBNUsuario', type='string'),
    Field('PlanDeManejoBNFechaHoraRegistroDig', type='datetime'),
    primarykey=['PlanDeManejoBNId'],
    migrate=False
)

db.define_table('PlanDeManejoBNPadron',
    Field('PlanDeManejoBNId', type='double'),
    Field('FormPlanManejoBNCarpeta', type='integer'),
    #Field('FormPlanManejoBNCarpeta', db.CarpetaBN.CarpetaBNId),
    Field('FormPlanManejoBNPadron', type='double'),
    Field('PlanDeManejoBNPadronSupACortar', type='double'),
    Field('PlanDeManejoBNPadronToneladasEstimadas', type='integer'),
    Field('PlanDeManejoBNPadronPlazo', type='integer'),
    Field('PlanDeManejoBNPadronFundamentacion', type='string'),
    primarykey=['PlanDeManejoBNId','FormPlanManejoBNCarpeta','FormPlanManejoBNPadron'],
    migrate=False
)

db.define_table('TempCarpetaBN',
    #Field('TempCarpetaBNId', db.TempCarpetaBN.TempCarpetaBNId),
    Field('TempCarpetaBNId', type='integer'),
    Field('TempCarpetaBNFechaRegistro', type='datetime'),
    Field('TempCarpetaBNNombreEstabl', type='string'),
    Field('CarpetaBNDepartamentoEstabl', type='integer'),    
    #Field('CarpetaBNDepartamentoEstabl', db.Departamentos),
    Field('TempCarpetaBNSeccionCatastralEstabl', type='integer'),
    Field('TempCarpetaBNSeccionJudicialEstabl', type='integer'),
    Field('TempCarpetaBNSeccionPolicialEstabl', type='integer'),
    Field('TempCarpetaBNParajeEstabl', type='string'),
    Field('TempCarpetaBNCIRepLegal', type='integer'),
    Field('TempCarpetaBNNombreRepLegal', type='string'),
    Field('TempCarpetaBNDireccionRepLegal', type='string'),
    #Field('CarpetaBNDepartamentoRepLegal', db.Departamentos),
    Field('CarpetaBNDepartamentoRepLegal', type='integer'),    
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
    #Field('AsociacionesId', db.Asociaciones.AsociacionesId),
    Field('AsociacionesId', type='integer'),    
    Field('TempCarpetaBNTipoRebrote', type='integer'),
    Field('TempCarpetaBNEstadoSanitario', type='string'),
    Field('TempCarpetaBNInvEspExoticas', type='boolean'), #ver
    Field('TempCarpetaBNIncForestales', type='boolean'), #ver
    Field('TempCarpetaBNAccionesAntropicas', type='string'),
    Field('TempCarpetaBNAreaArboladaTotal', type='double'),
    Field('TempCarpetaBNAreaArboladaBN', type='double'),
    Field('TempCarpetaBNAreaArboladaBP', type='double'),
    Field('TempCarpetaBNFechaHoraRegistroDig', type='datetime'),
    Field('TempCarpetaBNFechaHoraRegistroDig', type='string'),
    Field('TempCarpetaBNFechaHoraRegistroDig', type='integer'),
    primarykey=['TempCarpetaBNId'],
    migrate=False
)

db.define_table('TempCarpetaBNPadron',
    Field('TempCarpetaBNId', type='string'),
    Field('TempCarpetaBNPadronId', type='double'),
    Field('TempCarpetaBNPadronSeccJudicial', type='integer'),
    Field('TempCarpetaBNPadronSupBN', type='double'),
    Field('TempCarpetaBNPadronSupBP', type='double'),
    Field('TempCarpetaBNPadronTotal', type='double'),
    Field('TempCarpetaBNPadronSupPadron', type='double'),
    Field('TempCarpetaBNPadronSeccPolicial', type='integer'),
    primarykey=['TempCarpetaBNId','TempCarpetaBNPadronId','TempCarpetaBNPadronSeccJudicial'],
    migrate=False
)

db.define_table('TempCarpetaBNPropietario',
    #Field('TempCarpetaBNId', db.CarpetaBN),
    Field('TempCarpetaBNId', type='integer'),    
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
    #Field('TempCarpetaBNPropietarioDep', db.Departamentos),
    Field('TempCarpetaBNPropietarioDep', type='integer'),    
    primarykey=['TempCarpetaBNId','TempCarpetaBNPropietarioCI'],
    migrate=False
)

db.define_table('TipoSuelo',
    #Field('TipoSueloId', db.TipoSuelo.TipoSueloId),
    Field('TipoSueloId', type='integer'),    
    Field('TipoSueloNombre', type='string'),
    primarykey=['TipoSueloId'],
    migrate=False
)

db.define_table('Usuario',
    Field('UsuarioNombre', type='string'),
    Field('UsuarioNombreApellido', type='string'),
    primarykey=['UsuarioNombre'],
    migrate=False
) 
"""