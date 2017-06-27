def create_table_sample():
    table_script = "CREATE TABLE IF NOT EXISTS example ( \
           id_num INT NOT NULL auto_increment,  \
           id_name VARCHAR(40) NOT NULL, \
           data VARCHAR(40) ,  \
           PRIMARY KEY (id_num) \
           )"
    return table_script
