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

#
# Assumptions: 
# 1. you have a running Mysql DB that can be accessed
# 2. you have changed the db_config.py file to point to your DB
# 3. you have changed/added your table name to the db_config.py file pointing to your table
# 

# db_configs is a dict found in db_config.py ** change to connect to your DB **
#db_config = {'user':'tmosley',
#               'password':'tmosley',
#               'host':'localhost',
#               'database':'test'
#               }
#  return db_config

dbh = connect_db(db_configs())
db_cursor = dbh.cursor()

#
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
#

insert_sql = insert_sql(table_names()['tablename'])
insert_rec(db_cursor,dbh,insert_sql,(return_random(),"foobar"))


with open("datafile.txt", "r") as open_file:
  for line in open_file:
    insert_rec(db_cursor,dbh,insert_sql,(return_random(),line))


#query all records queries.all_records()
result_cursor = execute_query(db_cursor,all_records()) 

# The following is just there to query the db and verify the contents, pretty much throw away code ;)
#some code to verify db contents
print result_cursor.column_names

all_recs = result_cursor.fetchall()
 
 #
 # all_recs is an array of arrays: [[]] <- array of arrays i.e
 # [(1194, u'test4\n'), (1996, u'foobar'), (2577, u'test1\n'), 
 #  (4858, u'test5\n'), (5316, u'test2\n'), (9766, u'test3\n')]
 #

i = 0
for rec in all_recs:
 
  #
  # iterate over all records
  # rec is one of the elements of all_arrays [], also an array [],but now at the data i.e 
  # (1194, u'test4\n') ** the first record, just an example, see above 
  #

  print "record #->", i,  "id ->",rec[0] ,"name->",rec[1].decode('ascii', 'ignore').strip()
    
    #
    # index is the record index, id is the column id(rec[0]), name is the column name(rec[1])
    # mysql> desc tablename;
    # +-------+----------------------+------+-----+---------+----------------+
    # | Field | Type                 | Null | Key | Default | Extra          |
    # +-------+----------------------+------+-----+---------+----------------+
    # | id    | smallint(5) unsigned | NO   | PRI | NULL    | auto_increment |
    # | name  | varchar(20)          | NO   |     | NULL    |                |
    # +-------+----------------------+------+-----+---------+----------------+
    #
  i = i + 1
