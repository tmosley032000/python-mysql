import mysql.connector
from connect_db import *
from query_db import *
import pdb

username = 'tmosley'
password = 'tmosley'
host = 'localhost'
database = 'test'

dbh = connect_db(username,password,host,database)
query = "select * from tablename"

cur = dbh.cursor()

result_cursor = make_query(cur,query) 

print result_cursor.column_names
print result_cursor.fetchone()



