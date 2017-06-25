import mysql.connector
from connect_db import *
from query_db import *
from db_config import *
import pdb

username = 'tmosley'
password = 'tmosley'
host = 'localhost'
database = 'test'

conf = return_db_config()

dbh = connect_db(conf['username'],conf['password'],conf['host'],conf['database'])
query = "select * from tablename"

cur = dbh.cursor()

result_cursor = make_query(cur,query) 

print result_cursor.column_names
foo =  result_cursor.fetchone()[1]
bar = result_cursor.fetchone()[0]
print bar
print foo.decode('ascii','ignore')



