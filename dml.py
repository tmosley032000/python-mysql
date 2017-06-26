def insert_rec(cur, dbh, query, insert_vals):
  cur.execute(query,insert_vals)
  dbh.commit()

def delete_rec(cur, dbh):
  cur.execute('DELETE FROM tablename where name = "foo"')
  dbh.commit()
