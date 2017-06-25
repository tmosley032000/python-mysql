def insert_rec():
  return ("insert into tablename (id, name) VALUES (null, 'next_row')")

def delete_rec(column_name, qualifer):
  return "delete from ? where ? = ?"
