# -*- coding: utf-8 -*-
from gluon.sqlhtml import *
from gluon.html import *
from gluon import current

class ExporterPDF(ExportClass):
    label = 'PDF'
    file_ext = "pdf"
    content_type = "text/pdf"

    def __init__(self, rows):
        ExportClass.__init__(self, rows)

    def export(self):
        if self.rows:
            return self.rows.as_xml()
        else:
            return '<rows></rows>'


class ImportClass(object):
    label = None
    file_ext = None
    content_type = None

    def __init__(self, rows):
        self.rows=rows


    def importData(self):
        raise NotImplementedError


class ImporterTSV(ImportClass):
    label = 'TSV'
    file_ext = "tsv"
    content_type = "text/tsv"

    def __init__(self, rows):
        ImportClass.__init__(self, rows)

    def importData(self):
        pass


class ImporterCSV(ImportClass):
    label = 'CSV'
    file_ext = "csv"
    content_type = "text/csv"

    def __init__(self, rows):
        ImportClass.__init__(self, rows)

    def importData(self):
        pass


class ImporterJSON(ImportClass):
    label = 'JSON'
    file_ext = "json"
    content_type = "text/json"

    def __init__(self, rows):
        ImportClass.__init__(self, rows)

    def importData(self):
        pass


class ImporterXML(ImportClass):
    label = 'XML'
    file_ext = "xml"
    content_type = "text/xml"

    def __init__(self, rows):
        ImportClass.__init__(self, rows)

    def importData(self):
        pass


class DataManager(object):

    exportClasses = dict(
        tsv=( ExporterTSV, current.T('TSV') ),
        csv=( ExporterCSV, current.T('CSV') ),
        html=( ExporterHTML, current.T('HTML') ),
        pdf=( ExporterPDF, current.T('PDF') ),
        json=( ExporterJSON, current.T('JSON') ),
        xml=( ExporterXML, current.T('XML') )
    )

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
                try:
                    self._tableName=tablename
                    self._id='id'
                    self._fieldId=self._db[tablename][self._id]
                    self._query=( self._db[tablename][self._id]>0 )
                    self._fields=[ self._db[tablename][f] for f in self._db[tablename].fields ]
                    self._idReadeable=True
                    self._showMActions=showmactions
                    self._showDActions=showdactions
                    self._actionURL="elActionURL"
                except:
                    raise HTTP(200, current.T('Table dont have id field'))
            else:
                # May be a query!. Setup later.
                pass
        else:
            raise HTTP(200, current.T('Not database'))


    def fieldId(self, tableName, id='id'):
        self._tableName=tableName
        self._id=id
        self._fieldId=self._db[tablename][id]


    def query(self, q):
        self._query=q


    def fields(self, clos):
        self._cols=cols


    def headers(self, head):
        self._headers=head


    def idReadeable(self, val):
        self._idReadeable=val


    def actionURL(self, url):
        self.url=url


    def searchable(self, val):
        self._searchable=val


    def rowLinks(self,rid):
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


    def newButton(self):
        return A(
            SPAN(
                I(_class='icon-plus-sign icon-white'),
                current.T('Add record')
            ),
            _class='btn btn-inverse btn-mini',
            _title=current.T('Add new record to this table'),
            _onclick="return newDialogShow('%s');" % self._actionURL,
        )


    def editButton(self, rid):
        return A(
            I(_class='icon-pencil icon-white'),
            _class='btn btn-inverse btn-mini',
            _title=current.T('Edit this record'),
            _onclick="return editDialogShow('%s',%d);" % (self._actionURL, rid)
        )


    def deleteButton(self, rid):
        return A(
            I(_class='icon-remove icon-white'),
            _class='btn btn-warning btn-mini',
            _title=current.T('Delete this record'),
            _onclick="return deleteDialogShow('%s',%d);" % (self._actionURL, rid)
        )


    def deleteAllButton(self):
        return A(
            SPAN(
                I(_class='icon-remove icon-white'),
                current.T('Delete all')
            ),
            _class='btn btn-warning btn-mini',
            _title=current.T('Delete all records in this table'),
            _onclick="return deleteAllDialogShow('%s');" % (self._actionURL)
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
        mi=[1,2,3,4,5,6,7,8]
        return DIV(
            BUTTON(
                SPAN(
                    I(_class='icon-hand-right icon-white'),
                    current.T('Export')
                ),
                _class="btn btn-inverse btn-small",
                _title=current.T('Export data to file'),
            ),
            BUTTON(
                SPAN(
                    _class="caret"
                ),
                **{
                    '_class':'btn btn-inverse btn-small dropdown-toggle',
                    '_data-toggle':'dropdown'
                }
            ),
            UL(
                _class="dropdown-menu",
                *[LI(x) for x in mi]
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
                _class="btn btn-inverse btn-small",
                _title=current.T('Import data from file'),
            ),
            BUTTON(
                SPAN(
                    _class="caret"
                ),
                **{
                    '_class':'btn btn-inverse btn-small dropdown-toggle',
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
            headers=self._headers,
            links=[ lambda row: self.links( row[self._tableName][self._id] ) ],
            field_id=self._fieldId,
            orderby=self.defaultOrder,
            paginate=self.paginate,
            details=False,
            create=False,
            deletable=False,
            editable=False,
            showbuttontext=False,
            maxtextlength=64,
            exportclasses=self.exportClasses,
            ui='web2py',
            formstyle='table3cols',
            _class="web2py_grid",
        )


    def toolBar(self):
        return SPAN(
            self.newButton() if self._showMActions else None,
            self.exportButton(),
            self.importButton(),
            self.deleteAllButton() if self._showMActions else None,
        )
