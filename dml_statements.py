import pdb
from db_config import *

def insert_sql(table_name):
  insert = "INSERT INTO %s(id,name)"%(table_name) + "VALUES(%s,%s)"
  #insert = insert_statement +  "VALUES(%s,%s)"
  return insert

def delete_rec(column_name, qualifer):
  return "delete from ? where ? = ?"
