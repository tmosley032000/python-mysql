def (connect_postgres():
  conn = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='root'")
  return conn
  
