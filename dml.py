def new_insert_rec():
  new_rec = ("insert into tablename (id, name) VALUES (null, 'next_row')")
  return new_rec

def execute_dml(cur, dbh, rec):
  cur.execute(rec)
  dbh.commit()
