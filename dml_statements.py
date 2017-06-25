def insert_rec():
  return ("insert into tablename (id, name) VALUES (null, %s)")%("foo")

def delete_rec(column_name, qualifer):
  return "delete from ? where ? = ?"
