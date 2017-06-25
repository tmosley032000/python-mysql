import mysql.connector
from connect_db import *
from query_db import *
from db_config import *
from queries import *
from dml import *
import pdb
from random import randint

dbh = connect_db(db_configs())
query = all_records()


insert_vals = (randint(100,10000),"foobar")

insert_rec(dbh.cursor(),dbh,insert_vals)

result_cursor = make_query(dbh.cursor(),query) 

print result_cursor.column_names
foo =  result_cursor.fetchone()[1]
bar = result_cursor.fetchone()[0]
print bar
print foo.decode('ascii','ignore')



