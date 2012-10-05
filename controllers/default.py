# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

def index():
    form = SQLFORM(db.Planes_Pro)
    if form.accepts(request, session):
        request.flash = "saved!"
    elif form.errors:
        request.flash = "errors"
    else:
        pass
    return dict(form=form)
    
def mosivo():
    opts = []
    form = FORM(DIV(
                    DIV(
                        DIV(LABEL("Rango años:"), _class="igsLabelRango"),DIV(INPUT(_type='text', _id ="rango1", _name ="rango1", _autocomplete="off", requires=IS_INT_IN_RANGE(1950,2500)), "-", INPUT(_type='text', _id ="rango2", _name ="rango2", _autocomplete="off", requires=IS_INT_IN_RANGE(1950,2500)),_class="igsRangoAnios")),
                    DIV(
                        DIV(INPUT(_id='padronCB', _type='checkbox'), _class='igsCB'), DIV(LABEL("Padrón:"), _class="igsLabel"), DIV(SELECT(opts, _name='padron', _id='padron', _disabled="disabled"),_class="igsSelects")),
                    DIV(
                        DIV(INPUT(_id='seccionJCB', _type='checkbox'), _class='igsCB'), DIV(LABEL("Sección Judicial:"), _class="igsLabel"), DIV(SELECT(opts, _name='seccionJudicial', _id='seccionJudicial', _disabled="disabled"),_class="igsSelects")),
                    DIV(
                        DIV(INPUT(_id='deptoCB', _type='checkbox'), _class='igsCB'), DIV(LABEL("Departamento:"), _class="igsLabel"), DIV(SELECT(opts, _name='departamento', _id='departamento', _disabled="disabled"),_class="igsSelects")),
                    DIV(
                        DIV(INPUT(_id='regionCB', _type='checkbox'), _class='igsCB'), DIV(LABEL("Región:"), _class="igsLabel"), DIV(SELECT(opts, _name='region', _id='region', _disabled="disabled"),_class="igsSelects")),
                    DIV(
                        DIV(INPUT(_id='cuencaCB', _type='checkbox'), _class='igsCB'), DIV(LABEL("Cuenca:"), _class="igsLabel"), DIV(SELECT(opts, _name='cuenca', _id='cuenca', _disabled="disabled"),_class="igsSelects")),
                    DIV(
                        DIV(DIV(INPUT(_id='rectCB', _name='rectCB', _type='checkbox'), _class='igsOtherCB'), DIV(LABEL("Rectángulo:"), _class="igsLabel")),
                        DIV(LABEL("Esquina superior izquierda:"), _class='igsTabbedLabel'), 
                        DIV(LABEL("Latitud:"), INPUT(_type='text', _id ="topLeftLat", _name ="topLeftLat", _autocomplete="off", requires=IS_FLOAT_IN_RANGE(None,None), _disabled="disabled"), LABEL("Longitud:"), INPUT(_type='text', _id ="topLeftLong", _name ="topLeftLong", _autocomplete="off", requires=IS_FLOAT_IN_RANGE(None,None), _disabled="disabled"),_class="igsNumbers"), 
                        DIV(LABEL("Esquina inferior derecha:"), _class='igsTabbedLabel'),
                        DIV(LABEL("Latitud:"), INPUT(_type='text', _id ="bottomRightLat", _name ="bottomRightLat", _autocomplete="off", requires=IS_FLOAT_IN_RANGE(None,None), _disabled="disabled"), LABEL("Longitud:"), INPUT(_type='text', _id ="bottomRightLong", _name ="bottomRightLong", _autocomplete="off", requires=IS_FLOAT_IN_RANGE(None,None), _disabled="disabled"),_class="igsNumbers")
                    ),
                    DIV(
                        DIV(DIV(INPUT(_id='circCB',  _name='rectCB', _type='checkbox'), _class='igsOtherCB'), DIV(LABEL("Círculo:"), _class="igsLabel")),
                        DIV(LABEL("Centro:"), _class='igsTabbedLabel'), 
                        DIV(LABEL("Latitud:"), INPUT(_type='text', _id ="centroLat", _name ="centroLat", _autocomplete="off", requires=IS_FLOAT_IN_RANGE(None,None), _disabled="disabled"), LABEL("Longitud:"), INPUT(_type='text', _id ="centroLong", _name ="centroLong", _autocomplete="off", requires=IS_FLOAT_IN_RANGE(None,None), _disabled="disabled"),_class="igsNumbers"), 
                        DIV(DIV(LABEL("Radio:"), _class="igsTabbedLabelRadio"), DIV(INPUT(_type='text', _id ="radio", _name ="radio", _autocomplete="off", requires=IS_FLOAT_IN_RANGE(None,None), _disabled="disabled"), _class='igsNumbersRadio'), _style="clear: both;"),
                    ),
                    DIV(
                        DIV(INPUT(_type = "submit", _value= "Guardar"),_class = "igsSave")
                    )
                ), _method = 'POST'
            )
    #from gluon.debug import dbg
    #dbg.set_trace() # stop here!
    return dict(form=form)