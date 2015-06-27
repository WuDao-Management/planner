#account information
    #account name: 'manager'@'localhost'
    #key: ''

import MySQLdb as mdb
import sys
import pprint 
pp = pprint.PrettyPrinter(indent = 4)
con = None



try:
    con  = mdb.connect('localhost', 'manager', '', 'managementDB')

    cur = con.cursor()

    
    cur.execute("""CREATE TABLE IF NOT EXISTS Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))""")  
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")  
    con.commit()
except mdb.Error, e:
    print "Error %d: %s"%(e.args[0], e.args[1]) #TODO implement logging to save error message
    raise e

finally:
    if con:
        con.close()

