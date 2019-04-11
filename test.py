import mysql.connector
from connect_db import *
from query_db import *
from db_config import *
from queries import *
from dml import *
from dml_statements import *
from get_random import *
from create_table import *
import json
import pdb
#from connect_db_postgres import *
from random import randint


#
# Assumptions: 
# 1. you have installed mysql.connector
# 2. you have a running Mysql DB that can be accessed
# 3. you have changed the db_config.py *OR* db_conig.json file to point to your DB
# 4. you have changed/added your table name to the db_config.py or db_config.json file pointing to your table *Use only one, it's your choice
#

# 
#for using json (db_config.json) file for connection:
#  "db_config":
#              {"user":"tmosley","password":"tmosley","host":"localhost","database":"twith open('db_config.json') as data_file:    
with open('db_config.json') as data_file:
    data = json.load(data_file)

# for using dict (db_config.py) for connection:
# db_configs is a dict found in db_config.py ** change to connect to your DB **
# db_config = {'user':'tmosley',
#               'password':'tmosley',
#               'host':'localhost',
#               'database':'test'
#               }
#  return db_config

# connect with json(db_config.json):
dbh = connect_db(data['db_config'])
# just a comment
# --OR--
# connect with dictionary(db_config.py):
# *** Uncomment out next line to use ***
#dbh = connect_db(db_configs())

db_cursor = dbh.cursor()

# Create your own table:
#create_table_sample() contains:
table_script = "CREATE TABLE IF NOT EXISTS example ( \
           id_num INT NOT NULL auto_increment,  \
           id_name VARCHAR(40) NOT NULL, \
           data VARCHAR(40) ,  \
           PRIMARY KEY (id_num) \
           )"

db_cursor.execute(create_table_sample())

#
# modules used in the next calls:
# insert_sql = dml_statements.insert_sql()
# dbh = connect_db.connect_db()
# insert_sql = dml_statements.insert_sql()
# return_random = get_random.return_random()
# insert_rec = dml.insert_rec()

# table_names is a tablename config found in table_name dict of db_config.py or db_config.json ** Use only one, its your choce 
# dict - table_names = {'tablename':'tablename',
#                 'foobar':'foobar'
#                }
#         return table_names 
# json -   "table_names":
#             {"tablename":"tablename"}
#
#
# example using dict if you want to use json uncomment out the next line:
#insert_sql = insert_sql(data['table_names']['tablename'])
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
