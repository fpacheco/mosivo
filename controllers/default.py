# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

def index():
    return "MoSiVo"
    
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
                        DIV(INPUT(_id='cuencaCB', _type='checkbox'), _class='igsCB'), DIV(LABEL("Rectángulo:"), _class="igsLabel"),DIV(LABEL("Esquina superior izquierda:"), INPUT(_type='text', _id ="topLeft", _name ="topLeft", _autocomplete="off", requires=IS_FLOAT_IN_RANGE(None,None)), LABEL("Esquina inferior derecha:"),INPUT(_type='text', _id ="bottomRight", _name ="bottomRight", _autocomplete="off", requires=IS_FLOAT_IN_RANGE(None,None)),_class="igsNumbers")),
                    DIV(
                        DIV(INPUT(_id='cuencaCB', _type='checkbox'), _class='igsCB'), DIV(LABEL("Círculo:"), _class="igsLabel"),DIV(LABEL("Centro:"), INPUT(_type='text', _id ="centro", _name ="centro", _autocomplete="off", requires=IS_FLOAT_IN_RANGE(None,None)), LABEL("Radio:"),  INPUT(_type='text', _id ="radio", _name ="radio", _autocomplete="off", requires=IS_FLOAT_IN_RANGE(None,None)),_class="igsNumbers")),
                    DIV(
                        DIV(INPUT(_type = "submit", _value= "Guardar"),_class = "igsSave")
                    )
                ), _method = 'POST'
            )
    return dict(form=form)