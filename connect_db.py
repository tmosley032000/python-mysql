import mysql.connector
import pdb

def connect_db(conf):
  #desc
  ''' 
  conf is **kwargs - a reference to db_config.db_config dict i.e.
  --using dictionary --
  db_config = 
             {
              'user':'tmosley',
              'password':'tmosley',
              'host':'localhost',
              'database':'test'
             }
  --using json --
  "db_config": 
              {"user":"tmosley","password":"tmosley","host":"localhost","database":"test"}
  '''


  
    #foo
  return mysql.connector.connect(**conf)
