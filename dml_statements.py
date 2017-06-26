def insert_sql():
  insert = "INSERT INTO tablename(id,name)" "VALUES(%s,%s)"
  return insert

def delete_rec(column_name, qualifer):
  return "delete from ? where ? = ?"
