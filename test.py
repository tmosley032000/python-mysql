import mysql.connector
from connect_db import *
from query_db import *
from db_config import *
from queries import *
from dml import *
from dml_statements import *
from get_random import *
import pdb
from random import randint

# db_configs is a dict found in db_config.py:
#db_config = {'user':'tmosley',
#               'password':'tmosley',
#               'host':'localhost',
#               'database':'test'
#               }
#  return db_config

dbh = connect_db(db_configs())

# modules used in the next calls:
# insert_sql = dml_statements.insert_sql()
# dbh = connect_db.connect_db()
# insert_sql = dml_statements.insert_sql()
# return_random = get_random.return_random()
# insert_rec = dml.insert_rec()

# table_names is a tablename config found in table_name dict of db_config.py
# table_names = {'tablename':'tablename',
#                 'foobar':'foobar'
#                }
# return table_names 
insert_sql = insert_sql(table_names()['tablename'])
insert_rec(dbh.cursor(),dbh,insert_sql,(return_random(),"foobar"))

#query all records queries.all_records()
result_cursor = execute_query(dbh.cursor(),all_records()) 

print result_cursor.column_names
foo =  result_cursor.fetchone()[1]
bar = result_cursor.fetchone()[0]
print bar
print foo.decode('ascii','ignore')



