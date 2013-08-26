# -*- coding: utf-8 -*-
from gluon.sqlhtml import *
from gluon.html import *
from gluon import current
from importer import *
from exporter import *

"""
request = current.request
session = current.session
response = current.response
logged = session.auth and session.auth.user
"""

class DataManager(object):
    _actionURL=None
    _defaultOrder=None
    _fieldId=None
    _headers={}
    _idReadeable=False
    _searchable=True
    _tableName=None

    # Data export
    exportClasses = dict(
        tsv=( ExporterTSV, current.T('TSV') ),
        csv=( ExporterCSV, current.T('CSV') ),
        html=( ExporterHTML, current.T('HTML') ),
        pdf=( ExporterPDF, current.T('PDF') ),
        json=( ExporterJSON, current.T('JSON') ),
        xml=( ExporterXML, current.T('XML') )
    )
    # Data import
    importClasses = dict(
        tsv=( ImporterTSV, current.T('TSV') ),
        csv=( ImporterCSV, current.T('CSV') ),
        json=( ImporterJSON, current.T('JSON') ),
        xml=( ImporterXML, current.T('XML') )
    )


    def __init__(self, database, tablename, showmactions=True, showdactions=False):
        # database is required
        if database:
            self._db=database
            if tablename:
                # Just a table
                if tablename in self._db.tables:
                    try:
                        self._tableName=tablename
                        self._id='id'
                        self._fieldId=self._db[tablename][self._id]
                        self._query=( self._db[tablename][self._id]>0 )
                        self._fields=[ self._db[tablename][f] for f in self._db[tablename].fields ]
                        self._idReadeable=True
                        self._showMActions=showmactions
                        self._showDActions=showdactions
                        self._actionURL="/%s/plugin_dm/neddaction.load" % (current.request.application)
                        self._defaultOrder=self._fieldId
                        #self._headers=[ db[tablename][fn].label for fn in db[tablename].fields ]
                    except:
                        raise HTTP(200, current.T('Table %s dont have id field') % tablename)
                else:
                    raise HTTP(200, current.T('Database dont have table %s') % tablename)
            else:
                # May be a query!. Setup later!.
                pass
        else:
            raise HTTP(200, current.T('No database'))


    def url2(self,**b):
        b['args'] = current.request.args + b.get('args', [])
        localvars = current.request.get_vars.copy()
        localvars.update(b.get('vars', {}))
        b['vars'] = localvars
        b['hash_vars'] = False
        # b['user_signature'] = user_signature
        return URL(**b)
    
    def tableName(self,tablename):
        if tablename in self._db.tables:
            self._tableName=tableName
        else:
            pass

    def fieldId(self, id='id'):
        if self._tableName:
            self._id=id
            self._fieldId=self._db[self._tableName][id]
        else:
            pass

    def query(self, q):
        self._query=q


    def fields(self, fcols):
        # cols = [(tablename,fieldname),(tablename,fieldname), ... ]
        flist=[]
        for t in fcols:
            tablename=t[0]
            fieldname=t[1]
            if tablename in self._db.tables:
                if fieldname in self._db[tablename].fields:
                    flist.append( self._db[tablename][fieldname] )
                else:
                    print "Field (%s) is not in table (%s)" % (fieldname, tablename)
            else:
                print "The is no table (%s) in database" % tablename
        self._fields=flist


    def headers(self, head):
        #head=['label1', 'label2', ...]
        gridhead={}
        if len(head)==len(self._fields):
            cont=0
            for l in head:
                # str(field) da tablename.fieldname
                gridhead[ '%s' % self._fields[cont] ]=l
                cont=cont+1
        else:
            print "Fields and headers must have same size"
        self._headers=gridhead


    def idReadeable(self, val):
        # Grid hhas colum with ids
        if self._fieldId:
            self._idReadeable=val
            self._fieldId.readable=val
        else:
            pass

    def actionURL(self, url):
        #new, edit, delete and deleteall actions
        self.url=url


    def searchable(self, val):
        #Grid have serach box
        self._searchable=val


    def rowLinks(self,rid):
        #Custom links for every row
        """
        html=None
        if self._showMActions:
            html=SPAN(
                self.editButton(rid),
                self.deleteButton(rid)
            )
        if self._showDActions:
            if html:
                html=SPAN(html,detailsButton(rid))
            else:
                html=detailButton
        return html
        """
        return SPAN(
            SPAN(self.editButton(rid), self.deleteButton(rid)) if self._showMActions else '',
            self.detailButton(rid) if self._showDActions else ''
        )


    def newButton(self):
        return A(
            SPAN(
                I(_class='icon-plus-sign icon-white'),
                current.T('Add record')
            ),
            _class='btn btn-inverse btn-mini',
            _title=current.T('Add new record to this table'),
            _onclick="return newDialogShow('%s','%s');" % (self._actionURL, self._tableName),
        )


    def editButton(self, rid):
        return A(
            I(_class='icon-pencil icon-white'),
            _class='btn btn-inverse btn-mini',
            _title=current.T('Edit this record'),
            _onclick="return editDialogShow('%s','%s',%d);" % (self._actionURL, self._tableName, rid)
        )


    def deleteButton(self, rid):
        return A(
            I(_class='icon-remove icon-white'),
            _class='btn btn-warning btn-mini',
            _title=current.T('Delete this record'),
            _onclick="return deleteDialogShow('%s','%s', %d);" % (self._actionURL, self._tableName, rid)
        )


    def deleteAllButton(self):
        return A(
            SPAN(
                I(_class='icon-remove icon-white'),
                current.T('Delete all')
            ),
            _class='btn btn-warning btn-mini',
            _title=current.T('Delete all records in this table'),
            _onclick="return deleteAllDialogShow('%s','%s');" % (self._actionURL, self._tableName)
        )


    def detailsButton(self,rid):
        return A(
            I(_class='icon-th-large icon-white'),
            _class='btn btn-inverse btn-mini',
            _title=current.T('Edit details records'),
            _onclick="return detailsDialogEShow('%s', %d);" % (self._actionURL, rid),
            _onmouseover="return detailsDialogSShow('%s', %d);" % (self._actionURL, rid)
        )


    def exportButton(self):
        # mi=[1,2,3,4,5,6,7,8]
        export_links = []
        if not self._db(self._query).isempty():
            for k, v in sorted(self.exportClasses.items()):
                if not v:
                    continue
                label = v[1] if hasattr(v, "__getitem__") else k
                link = self.url2(vars=dict(
                    order=current.request.vars.order or '',
                    _export_type=k,
                    keywords=current.request.vars.keywords or '')
                )
                export_links.append(A(current.T(label), _href=link))
        else:
            export_menu = None
        
        return DIV(
            BUTTON(
                SPAN(
                    I(_class='icon-hand-right icon-white'),
                    current.T('Export')
                ),
                _class="btn btn-inverse btn-mini",
                _title=current.T('Export data to file'),
            ),
            BUTTON(
                SPAN(
                    _class="caret"
                ),
                **{
                    '_class':'btn btn-inverse btn-mini dropdown-toggle',
                    '_data-toggle':'dropdown'
                }
            ),
            UL(
                _class="dropdown-menu",
                *[LI(l) for l in export_links]
            ),
            _class="btn-group"
        )


    def importButton(self):
        mi=[1,2,3,4,5,6,7,8]
        return DIV(
            BUTTON(
                SPAN(
                    I(_class='icon-hand-left icon-white'),
                    current.T('Import')
                ),
                _class="btn btn-inverse btn-mini",
                _title=current.T('Import data from file'),
            ),
            BUTTON(
                SPAN(
                    _class="caret"
                ),
                **{
                    '_class':'btn btn-inverse btn-mini dropdown-toggle',
                    '_data-toggle':'dropdown'
                }
            ),
            UL(
                _class="dropdown-menu",
                *[LI(x) for x in mi]
            ),
            _class="btn-group"
        )


    def paginate(self,val):
        self.paginate=val


    def grid(self):
        return SQLFORM.grid(
            query=self._query,
            fields=self._fields,
            # headers=self._headers,
            # links=[ lambda row: self.rowLinks( row[self._tableName][self._id] ) ] if (self._showMActions or self._showDActions) else None,
            links=[ lambda row: self.rowLinks( row[self._id] ) ] if (self._showMActions or self._showDActions) else None,
            field_id=self._fieldId,
            orderby=self._defaultOrder,
            paginate=self.paginate,
            details=False,
            create=False,
            deletable=False,
            editable=False,
            showbuttontext=False,
            maxtextlength=64,
            exportclasses=None,
            ui='web2py',
            formstyle='table3cols',
            _class="web2py_grid",
        )


    def toolBar(self):
        return SPAN(
            self.newButton() if self._showMActions else '',
            self.exportButton(),
            self.importButton(),
            self.deleteAllButton() if self._showMActions else '',
        )
