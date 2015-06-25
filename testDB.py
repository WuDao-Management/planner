#account information
    #account name: 'manager'@'localhost'
    #key: ''

import MySQLdb as mdb
import sys
import pprint 
pp = pprint.PrettyPrinter(indent = 4)
con = None

try:
    con  = mdb.connect('localhost', 'manager', '', 'personal')

    cur = con.cursor()

    cur.execute('select * from money')

    data = cur.fetchone()

    print type(data[1])
    # pp.pprint(data)

except mdb.Error, e:
    print "Error %d: %s"%(e.args[0], e.args[1])

finally:
    if con:
        con.close()
