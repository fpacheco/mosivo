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
            (self._db['cima']['especie']==self._db['especie']['id']) &
            (self._db['especie']['genero']==self._db['genero']['id']) &
            (self._db['genero']['cby']==self._muid)
        )
        if q.isempty():
            return False
        else:
            q = self._db(
                (self._db['rodald']['plan']==self._db['plan']['id']) &
                (self._db['plan']['cby']==self._muid)
            )
            if q.isempty():
                return False
            else:
                # RFPV - ¿Y si todas las sj hacen que un depto no sea valido?
                sql1 = "SELECT DISTINCT rd.especie, sj.departamento FROM rodald rd, plan p, seccionjudicial sj " \
                    "WHERE rd.plan=p.id AND sj.id=p.sjudicial AND p.cby=%i AND sj.cby=%i ORDER BY sj.departamento" % (self._muid,self._muid)
                sql2 = "SELECT DISTINCT c.especie,c.departamento FROM cima c, especie e, genero g " \
                    "WHERE c.especie=e.id AND e.genero=g.id AND g.cby=%i AND e.exc='F'" % (self._muid)
                sql = "(%s) EXCEPT (%s)" % (sql1,sql2)
                print "MModel.checkCima.sql: %s" % sql
                rows = self._db.executesql( sql )
                if len(rows)==0:
                    return True
                else:
                    return False

    def checkCaefectiva(self):
        """Verifica si los datos del coeficiente de area efectiva estan correctos
        """
        q = self._db(
            (self._db['caefectiva']['especie']==self._db['especie']['id']) &
            (self._db['especie']['genero']==self._db['genero']['id']) &
            (self._db['genero']['cby']==self._muid)
        )
        if q.isempty():
            return False
        else:
            q = self._db(
                (self._db['rodald']['plan']==self._db['plan']['id']) &
                (self._db['plan']['cby']==self._muid)
            )
            if q.isempty():
                return False
            else:
                # RFPV - ¿Y si todas las sj hacen que un depto no sea valido?
                sql1 = "SELECT DISTINCT rd.especie, sj.departamento FROM rodald rd, plan p, seccionjudicial sj " \
                    "WHERE rd.plan=p.id AND sj.id=p.sjudicial AND p.cby=%i AND sj.cby=%i ORDER BY sj.departamento" % (self._muid,self._muid)
                sql2 = "SELECT DISTINCT c.especie,c.departamento FROM caefectiva c, especie e, genero g " \
                    "WHERE c.especie=e.id AND e.genero=g.id AND g.cby=%i AND e.exc='F'" % (self._muid)
                sql = "(%s) EXCEPT (%s)" % (sql1,sql2)
                print "MModel.checkCaefectiva.sql: %s" % sql
                rows = self._db.executesql( sql )
                if len(rows)==0:
                    return True
                else:
                    return False


    def checkCintervencionr(self):
        """Verifica si los datos del coeficiente de area efectiva estan correctos
        """
        q = self._db(
            (self._db['cintervencionr']['especie']==self._db['especie']['id']) &
            (self._db['especie']['genero']==self._db['genero']['id']) &
            (self._db['genero']['cby']==self._muid)
        )
        if q.isempty():
            return False
        else:
            qq = self._db(
                (self._db['rodald']['plan']==self._db['plan']['id']) &
                (self._db['plan']['cby']==self._muid)
            )
            if qq.isempty():
                return False
            else:
                sql1 = "SELECT DISTINCT rd.especie, sj.departamento FROM rodald rd, plan p, seccionjudicial sj " \
                    "WHERE rd.plan=p.id AND sj.id=p.sjudicial AND p.cby=%i AND sj.cby=%i ORDER BY sj.departamento" % (self._muid,self._muid)
                sql2 = "SELECT DISTINCT c.especie,c.departamento " \
                    "FROM cintervencionr c, especie e, genero g " \
                    "WHERE c.especie=e.id AND e.genero=g.id AND g.cby=%i AND e.exc='F' " % (self._muid)
                sql3 = "SELECT DISTINCT c.especie,c.departamento " \
                    "FROM cintervenciona c, especie e, genero g " \
                    "WHERE c.especie=e.id AND e.genero=g.id AND g.cby=%i AND e.exc='F' " % (self._muid)
                sql = "(%s) EXCEPT ( (%s) UNION (%s) )" % (sql1, sql2, sql3)
                print "MModel.checkCintervencionr.sql: %s" % sql
                rows = self._db.executesql( sql )
                if len(rows)==0:
                    sql="SELECT count(tmp.b) FROM "\
                        "(SELECT cdi.cintervencionr,cast(sum(cdi.fdestino) as integer)*100=100 as b " \
                        "FROM cdintervencionr cdi,cintervencionr ci, genero g, especie e  " \
                        "WHERE cdi.cintervencionr=ci.id AND ci.especie=e.id AND e.genero=g.id AND g.cby=%i AND e.exc='F' " \
                        "GROUP BY cdi.cintervencionr) AS tmp " \
                        "WHERE tmp.b=true" % (self._muid)
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
        """Verifica si los datos del coeficiente de suelo estan correctos
        """
        # cguselo(sjudiaicl,gruposuelo)
        q = self._db(
            (self._db['cgsuelo']['sjudicial']==self._db['seccionjudicial']['id']) &
            (self._db['seccionjudicial']['cby']==self._muid) &
            (self._db['seccionjudicial']['exc']==False)
        )
        if q.isempty():
            return False
        else:
            q = self._db(
                (self._db['ubicacionrodald']['rodal']==self._db['rodald']['id']) &
                (self._db['rodald']['plan']==self._db['plan']['id']) &
                (self._db['plan']['cby']==self._muid)
            )
            if q.isempty():
                return False
            else:
                sql1 = "SELECT DISTINCT urd.sjudicial FROM ubicacionrodald urd, rodald rd, plan p, seccionjudicial sj " \
                    "WHERE rd.plan=p.id AND urd.rodal=rd.id AND sj.id=urd.sjudicial AND p.cby=%i AND sj.cby=%i AND sj.exc='F' " \
                    "ORDER BY urd.sjudicial" % (self._muid,self._muid)
                sql2 = "SELECT DISTINCT c.sjudicial FROM cgsuelo c, seccionjudicial sj " \
                    "WHERE c.sjudicial=sj.id AND sj.cby=%i AND sj.exc='F'" % (self._muid)
                sql = "(%s) EXCEPT (%s)" % (sql1,sql2)
                print "MModel.checkCgsuelo.sql: %s" % sql
                rows = self._db.executesql( sql )
                if len(rows)==0:
                    return True
                else:
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


    def grupoSueloRodalD(self):
        """Fill grupo suelo rodald
        """
        q=self._db(
            (self._db['ubicacionrodald']['rodal']==self._db['rodald']['id']) &
            (self._db['rodald']['plan']==self._db['plan']['id']) &
            (self._db['plan']['cby']==self._muid)
        )
        if not q.isempty():
            self._db.commit()
            try:
                # Delete old data
                sql1 = "DELETE FROM gruposuelorodald WHERE rodal IN "
                sql2 = "SELECT r.id FROM rodald r, plan p " \
                    "WHERE r.plan=p.id AND p.cby=%i" % (self._muid)
                sql = "%s (%s)" % (sql1,sql2)
                print "MModel.grupoSueloRodalD.sql: %s" % sql
                self._db.executesql(sql)

                # SQL is short and fast
                sql1 ="INSERT INTO gruposuelorodald(rodal,gsuelo,superficie)"
                sql2 = "SELECT urd.rodal, cgs.gsuelo, rd.areaafect " \
                    "FROM plan p, rodald rd, ubicacionrodald urd, cgsuelo cgs " \
                    "WHERE rd.plan=p.id AND p.cby=%i AND rd.id=urd.rodal AND urd.sjudicial=cgs.sjudicial " \
                    "ORDER BY rd.id" % (self._muid, )
                sql = "%s (%s)" % (sql1,sql2)
                print "MModel.grupoSueloRodalD.sql: %s" % sql
                self._db.executesql(sql)
                self._db.commit()
            except Exception as e:
                print "Error: %s!" % e
                self._db.rollback()
        else:
            pass


    def intervRodalD(self):
        """Run model
        """
        q=self._db( self._db['rodald']['id']>0 )
        if not q.isempty():
            # Temporal table name
            temptable = 'mmodelrtemp_%i' % self._muid
            # Delete previous intance of temporal table
            # No es muy portable!!!!
            sqldrop = "DROP TABLE IF EXISTS %s" % temptable
            self._db.executesql(sqldrop)

            ## Create temporal table
            sql = "SELECT rd.id AS rodalid, rd.anioplant AS anioplant, rd.areaafect AS areaafect, cin.aintervencion AS aintervencion, " \
                "cin.stintervencion AS stintervencion, cim.ima AS ima, cae.aefectiva AS aefectiva, cin.fextraccion AS fextraccion, " \
                "cdi.destino AS destino, cdi.fdestino AS fdestino, " \
                "cast('-1' as double precision) AS aniodisp, " \
                "cast('-1' as double precision) AS mcmcc, " \
                "%i AS cby " % self._muid
                #anio que quedara disponible
                #m3 de madera con corteza en campo
                #uid
            sql += "INTO %s " % temptable
            sql += "FROM plan p, rodald rd, ubicacionrodald urd, seccionjudicial sj, "\
                "departamento d, cima cim, caefectiva cae, cintervencionr cin, cdintervencionr cdi "
            sql += "WHERE rd.plan=p.id AND p.cby=%i AND rd.id=urd.rodal AND urd.sjudicial=sj.id AND sj.departamento=d.id AND " \
                "d.id=cim.departamento AND d.id=cae.departamento AND d.id=cin.departamento AND " \
                "rd.especie=cim.especie AND rd.especie=cae.especie AND rd.especie=cin.especie AND " \
                "cin.id=cdi.cintervencionr " % (self._muid)
            sql += "ORDER BY rd.id, cin.aintervencion"
            print "MModel.intervRodalD.sql: %s" % sql
            rows = self._db.executesql(sql)

            ## Update this table for raleos (1,2,3,4,) y tala rasa (5)
            sql1 = "UPDATE %s " % temptable
            sql1 += "SET aniodisp=(anioplant+aintervencion), mcmcc=(areaafect*aefectiva)*(aintervencion*ima)*fextraccion*fdestino "
            # Raleo o Tala rasa
            sql1 += "WHERE stintervencion IN (1,2,3,4,5)"
            print "MModel.intervRodalD.sql: %s" % sql
            res = self._db.executesql(sql1)
            self._db.commit()

            ## Update this table for rebrotes (6)
            ids = self._db.executesql("SELECT DISTINCT rodalid FROM %s WHERE stintervencion=6" % temptable)
            for _id in ids:
                d=self._db.executesql(
                    "SELECT aintervencion FROM %s WHERE stintervencion=5 AND rodalid=%d" % (temptable,_id[0])
                )
                ahcant=d[0][0] #anios hasta el corte anterior
                rr=self._db.executesql(
                    "SELECT areaafect,aefectiva,aintervencion,ima,fextraccion,fdestino,rodalid " \
                    "FROM %s WHERE stintervencion=6 AND rodalid=%d ORDER BY aintervencion" % (temptable,_id[0])
                )
                for r in rr:
                    # (areaafect*aefectiva)*(aintervencion*ima)*fextraccion*fdestino
                    nanios=(r[2]-ahcant)
                    #mcmcc=(r[0]*r[1])*(nanios*r[3])*r[4]*r[5]
                    mcmcc=( float(r[0])*float(r[1]) )*( float(nanios)*float(r[3]) )*float(r[4])*float(r[5])
                    sql2 = "UPDATE %s " % temptable
                    sql2 += "SET aniodisp=(anioplant+aintervencion), mcmcc=%f " % mcmcc
                    sql2 += "WHERE stintervencion=6 AND rodalid=%d AND aintervencion=%f::numeric(5,3)" % (r[6],r[2])
                    res = self._db.executesql(sql2)
                    ahcant=r[2]

            ## Insert data in tables
            # Explicit delete, cascade is slow
            # Delete user records from destinointervrodald
            sql1 = "DELETE FROM destinointervrodald WHERE irodal"
            sql2 = "SELECT ir.id " \
                "FROM intervrodald ir, rodald rd, plan p " \
                "WHERE ir.rodal=rd.id AND rd.plan=p.id AND p.cby=%i" % (self._muid)
            sql ="%s IN (%s)" % (sql1,sql2)
            print "MModel.intervRodalD.sql: %s" % sql
            self._db.executesql(sql)
            # Delete user records from intervrodald
            sql1 = "DELETE FROM intervrodald WHERE rodal"
            sql2 = "SELECT rd.id " \
                "FROM rodald rd, plan p " \
                "WHERE rd.plan=p.id AND p.cby=%i" % (self._muid)
            sql ="%s IN (%s)" % (sql1,sql2)
            print "MModel.intervRodalD.sql: %s" % sql
            self._db.executesql(sql)

            # intervrodald
            sql1 = "INSERT INTO intervrodald(rodal,stintervencion,adisp)"
            sql2 = "SELECT DISTINCT rodalid, stintervencion, aniodisp FROM %s ORDER BY rodalid,aniodisp" % temptable
            sql ="%s (%s)" % (sql1,sql2)
            print "MModel.intervRodalD.sql: %s" % sql
            self._db.executesql(sql)

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
        if self.checkCima() and self.checkCaefectiva() and self.checkCintervencionr():
            # self.UbicacionRodalD()
            self.grupoSueloRodalD()
            self.intervRodalD()
            # TODO: Agregar en una tabla fecha de simulacion, hasta, autor
            return True
        else:
            return False


