# coding: utf8
"""
"""
# SELECT p.ncarpeta, mmt.rodalid, d.nombre, g.nombre, e.nombre, mmt.anioplant, mmt.areaafect, mmt.aintervencion, ti.nombre, mmt.ima, mmt.aefectiva, mmt.fextraccion, dn.nombre, mmt.fdestino, mmt.aniodisp, mmt.mcmcc FROM mmodelrtemp mmt, tipointervencion ti, plan p, rodald rd, seccionjudicial sj, departamento d, destino dn, especie e, genero g WHERE p.id=rd.plan AND rd.id=mmt.rodalid AND rd.especie=e.id AND g.id=e.genero AND p.sjudicial=sj.id AND sj.departamento=d.id AND ti.id=mmt.tintervencion AND dn.id=mmt.destino;

class MModel(object):


    def __init__(self, mDatabase, mUid):
        """Class initialization function

        :param mDatabase: local database (MoSiVo).
        :type mDatabase: DAL connection.
        :param mUid: Mosivo user id.
        :type mUis: Integer.
        """
        # mosivo app database
        self._db=mDatabase
        # mosivo app user id
        self._muid = mUid


    def checkCima(self):
        """Verifica si los datos del coeficiente de IMA estan correctos
        """
        q = self._db(
            (self._db['cima']['cby']==self._muid)
        )
        if q.isempty():
            return False
        else:
            q = self._db(
                (self._db['rodald']['cby']==self._muid)
            )
            if q.isempty():
                return False
            else:
                sql1 = "SELECT DISTINCT rd.especie, sj.departamento FROM rodald rd, plan p, seccionjudicial sj " \
                       "WHERE rd.plan=p.id AND sj.id=p.sjudicial AND p.cby=%i  ORDER BY sj.departamento" % (self._muid)
                sql2 = "SELECT DISTINCT c.especie,c.departamento FROM cima c, especie e WHERE c.cby=%i AND e.cby=%i AND e.exc=false" % (self._muid,self._muid)
                rows = self._db.executesql(
                    "(%s) EXCEPT (%s)" % (sql1,sql2)
                )
                if len(rows)==0:
                    return True
                else:
                    return False

    def checkCaefectiva(self):
        """Verifica si los datos del coeficiente de area efectiva estan correctos
        """
        q = self._db( self._db['caefectiva']['id']>0 )
        if q.isempty():
            return False
        else:
            q = self._db( self._db['rodald']['id']>0 )
            if q.isempty():
                return False
            else:
                rows = self._db.executesql("(SELECT DISTINCT rd.especie, sj.departamento FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento) EXCEPT (SELECT DISTINCT especie,departamento FROM caefectiva)")
                if len(rows)==0:
                    return True
                else:
                    return False


    def checkCintervencionr(self):
        """Verifica si los datos del coeficiente de area efectiva estan correctos
        """
        q = self._db( self._db['cintervencionr']['id']>0 )
        if q.isempty():
            return False
        else:
            qq = self._db( self._db['rodald']['id']>0 )
            if qq.isempty():
                return False
            else:
                sql1 = "(SELECT DISTINCT rd.especie, sj.departamento FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento)"
                sql2 = "( (SELECT DISTINCT especie,departamento FROM cintervencionr) UNION (SELECT DISTINCT especie,departamento FROM cintervenciona) )"
                rows = self._db.executesql(
                    "%s EXCEPT %s" % (sql1, sql2)
                )
                if len(rows)==0:
                    sql="SELECT count(tmp.b) FROM "\
                        "(SELECT cintervencionr,cast(sum(fdestino) as integer)*100=100 as b FROM cdintervencionr GROUP BY cintervencionr) AS tmp " \
                        "WHERE tmp.b=true"
                    r = self._db.executesql( sql )
                    if r[0][0]==q.count():
                        return True
                    else:
                        return False
                else:
                    return False


    def checkCintervenciona(self):
        """Verifica si los datos del coeficiente de area efectiva estan correctos
        """
        q = self._db( self._db['cintervenciona']['id']>0 )
        if q.isempty():
            return False
        else:
            q = self._db( self._db['rodald']['id']>0 )
            if q.isempty():
                return False
            else:
                sql1 = "(SELECT DISTINCT rd.especie, sj.departamento FROM rodald rd, plan p, seccionjudicial sj WHERE rd.plan=p.id AND sj.id=p.sjudicial ORDER BY sj.departamento)"
                sql2 = "( (SELECT DISTINCT especie,departamento FROM cintervenciona) UNION (SELECT DISTINCT especie,departamento FROM cintervenciona) )"
                rows = self._db.executesql(
                    "%s EXCEPT %s" % (sql1, sql2)
                )
                if len(rows)==0:
                    sql="SELECT count(tmp.b) FROM "\
                        "(SELECT cintervenciona,cast(sum(fdestino) as integer)*100=100 as b FROM cdintervenciona GROUP BY cintervenciona) AS tmp " \
                        "WHERE tmp.b=true"
                    r = self._db.executesql( sql )
                    if r[0][0]==q.count():
                        return True
                    else:
                        return False
                else:
                    return False


    def checkCbcampo(self):
        return False


    def checkCbindustria(self):
        return False


    def checkCgsuelo(self):
        return False


    def checkCcosecha(self):
        return False


    def checkCbcampoe(self):
        return False


    def checkAll(self):
        """Check all coeficientes
        """
        if self.checkCima() and self.checkCaefectiva() and \
                self.checkCintervencionr() and self.checkCintervenciona() and \
                self.checkCbindustria() and self.checkCbcampo() and \
                self.checkCgsuelo() and self.checkCcosecha() and \
                self.checkCbcampoe():
            print "checkAll: True"
            return True
        else:
            print "checkAll: False"
            return False


    def UbicacionRodalD(self):
        """Fill ubicacionrodald
        """
        q=self._db( self._db['plan']['id']>0 )
        if not q.isempty():
            self._db.commit()
            try:
                self._db.executesql("DELETE FROM ubicacionrodald")
                self._db.executesql("ALTER SEQUENCE ubicacionrodald_id_seq MINVALUE 0")
                self._db.executesql("SELECT setval('ubicacionrodald_id_seq', 0, true)")
                # SQL is short and fast
                sql = "SELECT rd.id, p.sjudicial, p.lon, p.lat FROM rodald rd, plan p " \
                    "WHERE rd.plan=p.id " \
                    "ORDER BY rd.id"
                sqlinsert ="INSERT INTO ubicacionrodald(rodal,sjudicial,lon,lat) (%s)" % sql
                self._db.executesql(sqlinsert)
                self._db.commit()
            except Exception as e:
                print "Error: %s!" % e
                self._db.rollback()
        else:
            pass


    def GrupoSueloRodalD(self):
        q=self._db( self._db['ubicacionrodald']['id']>0 )
        if not q.isempty():
            self._db.commit()
            try:
                self._db.executesql("DELETE FROM gruposuelorodald")
                self._db.executesql("ALTER SEQUENCE gruposuelorodald_id_seq MINVALUE 0;")
                self._db.executesql("SELECT setval('gruposuelorodald_id_seq', 0, true);")
                # SQL is short and fast
                sql = "SELECT urd.rodal, cgs.gsuelo, rd.areaafect " \
                    "FROM rodald rd, ubicacionrodald urd, cgsuelo cgs " \
                    "WHERE rd.id=urd.rodal AND urd.sjudicial=cgs.sjudicial " \
                    "ORDER BY rd.id"
                sqlinsert ="INSERT INTO gruposuelorodald(rodal,gsuelo,superficie) (%s)" % sql
                self._db.executesql(sqlinsert)
                self._db.commit()
            except Exception as e:
                print "Error: %s!" % e
                self._db.rollback()
        else:
            pass


    def IntervRodalD(self):
        q=self._db( self._db['rodald']['id']>0 )
        if not q.isempty():
            # Temporal table name
            temptable = 'mmodelrtemp'
            # Delete previous intance of temporal table
            # No es muy portable!!!!
            sqldrop = "DROP TABLE IF EXISTS %s" % temptable
            self._db.executesql(sqldrop)

            ## Create temporal table
            sql = "SELECT rd.id AS rodalid, rd.anioplant AS anioplant, rd.areaafect AS areaafect, cin.aintervencion AS aintervencion, " \
                "cin.tintervencion AS tintervencion, cim.ima AS ima, cae.aefectiva AS aefectiva, cin.fextraccion AS fextraccion, " \
                "cdi.destino AS destino, cdi.fdestino AS fdestino, " \
                "cast('-1' as double precision) AS aniodisp, " \
                "cast('-1' as double precision) AS mcmcc "
                #anio que quedara disponible
                #m3 de madera con corteza en campo
            sql += "INTO %s " % temptable
            sql += "FROM rodald rd, ubicacionrodald urd, seccionjudicial sj, "\
                "departamento d, cima cim, caefectiva cae, cintervencionr cin, cdintervencionr cdi "
            sql += "WHERE rd.id=urd.rodal AND urd.sjudicial=sj.id AND sj.departamento=d.id AND " \
                "d.id=cim.departamento AND d.id=cae.departamento AND d.id=cin.departamento AND " \
                "rd.especie=cim.especie AND rd.especie=cae.especie AND rd.especie=cin.especie AND " \
                "cin.id=cdi.cintervencionr "
            sql += "ORDER BY rd.id, cin.aintervencion"
            rows = self._db.executesql(sql)

            ## Update this table for raleos (1) y tala rasa (2)
            sql1 = "UPDATE %s " % temptable
            sql1 += "SET aniodisp=(anioplant+aintervencion), mcmcc=(areaafect*aefectiva)*(aintervencion*ima)*fextraccion*fdestino "
            sql1 += "WHERE tintervencion=1 OR tintervencion=2"
            res = self._db.executesql(sql1)

            ## Update this table for rebrotes (3)
            ids = self._db.executesql("SELECT DISTINCT rodalid FROM %s WHERE tintervencion=3" % temptable)
            for _id in ids:
                d=self._db.executesql(
                    "SELECT aintervencion FROM %s WHERE tintervencion=2 AND rodalid=%d" % (temptable,_id[0])
                )
                ahcant=d[0][0] #anios hasta el corte anterior
                rr=self._db.executesql(
                    "SELECT areaafect,aefectiva,aintervencion,ima,fextraccion,fdestino,rodalid " \
                    "FROM %s WHERE tintervencion=3 AND rodalid=%d ORDER BY aintervencion" % (temptable,_id[0])
                )
                for r in rr:
                    # (areaafect*aefectiva)*(aintervencion*ima)*fextraccion*fdestino
                    nanios=(r[2]-ahcant)
                    #mcmcc=(r[0]*r[1])*(nanios*r[3])*r[4]*r[5]
                    mcmcc=( float(r[0])*float(r[1]) )*( float(nanios)*float(r[3]) )*float(r[4])*float(r[5])
                    sql2 = "UPDATE %s " % temptable
                    sql2 += "SET aniodisp=(anioplant+aintervencion), mcmcc=%f " % mcmcc
                    sql2 += "WHERE tintervencion=3 AND rodalid=%d AND aintervencion=%f::numeric(5,3)" % (r[6],r[2])
                    res = self._db.executesql(sql2)
                    ahcant=r[2]

            ## Insert data in tables
            # prepare
            self._db.executesql("DELETE FROM destinointervrodald")
            self._db.executesql("ALTER SEQUENCE destinointervrodald_id_seq MINVALUE 0;")
            self._db.executesql("SELECT setval('destinointervrodald_id_seq', 0, true);")
            self._db.executesql("DELETE FROM intervrodald")
            self._db.executesql("ALTER SEQUENCE intervrodald_id_seq MINVALUE 0;")
            self._db.executesql("SELECT setval('intervrodald_id_seq', 0, true);")
            # intervrodald
            sql="SELECT DISTINCT rodalid, tintervencion, aniodisp FROM %s ORDER BY rodalid,aniodisp" % temptable
            sqlinsert="INSERT INTO intervrodald(rodal,tintervencion,adisp) (%s)" % sql
            self._db.executesql(sqlinsert)
            # destinointervrodald
            """
            sql="SELECT DISTINCT id, rodal, adisp FROM intervrodald ORDER BY rodal,adisp"
            rows = self._db.executesql(sql)
            self._db.commit()
            try:
                for r in rows:
                    sql="SELECT %d AS irodal, destino, mcmcc FROM %s WHERE rodalid=%d AND aniodisp=%d" % (r[0],temptable,r[1],r[2])
                    sqlinsert="INSERT INTO destinointervrodald(irodal,destino,mcmcc) (%s)" % sql
                    self._db.executesql(sqlinsert)
                self._db.commit()
            except Exception as e:
                print "Error: %s" % e
                self._db.rollback()
            """
            self._db.commit()
            try:
                sql="SELECT i.id AS irodal, destino, mcmcc FROM %s t, intervrodald i WHERE i.rodal=t.rodalid AND i.adisp=t.aniodisp ORDER BY i.id,i.adisp" % (temptable)
                sqlinsert="INSERT INTO destinointervrodald(irodal,destino,mcmcc) (%s)" % sql
                self._db.executesql(sqlinsert)
                self._db.commit()
            except Exception as e:
                print "Error: %s" % e
                self._db.rollback()
        else:
            pass

    def run(self):
        #if checkAll:
        if self.checkCima() and self.checkCaefectiva() and \
                self.checkCintervencionr():
            self.UbicacionRodalD()
            self.GrupoSueloRodalD()
            self.IntervRodalD()
            # TODO: Agregar en una tabla fecha de simulacion, hasta, autor
            return True
        else:
            return False


