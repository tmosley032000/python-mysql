def insert_rec(cur, dbh, insert_vals):
  query = "INSERT INTO tablename(id,name)" "VALUES(%s,%s)" 
  cur.execute(query,insert_vals)
  dbh.commit()

def delete_rec(cur, dbh):
  cur.execute('DELETE FROM tablename where name = "foo"')
  dbh.commit()
