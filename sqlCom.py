#account information
    #account name: 'manager'@'localhost'
    #key: ''

import MySQLdb as mdb
import sys
import pprint
pp = pprint.PrettyPrinter(indent = 4)
con = None

class sqlCom():

    def excecute(self,sqlStatement):
        try:
            con  = mdb.connect('localhost', 'manager', '', 'managementDB')

            cur = con.cursor()

            cur.execute(sqlStatement)
            con.commit()

        except mdb.Error, e:
            print "Error %d: %s"%(e.args[0], e.args[1]) #TODO implement logging to save error message
            raise e

        finally:
            if con:
                con.close()

    def fetchinfo(self,sqlStatement):
        try:
            con  = mdb.connect('localhost', 'manager', '', 'managementDB')

            cur = con.cursor()

            cur.execute(sqlStatement)

            return cur.fetchall()
        except mdb.Error, e:
            print "Error %d: %s"%(e.args[0], e.args[1]) #TODO implement logging to save error message
            raise e

        finally:
            if con:
                con.close()

if __name__=="__main__":
    a = sqlCom()
    a.excecute("insert into test_subject(start_time,end_time,cumper) values('2015-06-27 20:18:35', '2015-06-27 20:18:38', 18);")