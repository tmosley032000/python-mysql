import mysql.connector

def connect_db(username,password,host,database):
  print "foo"
  dbh = mysql.connector.connect(user=username,password=password,host=host,database=database)
  return dbh


