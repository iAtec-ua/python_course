# Constructor for writers SQL table

TABLE_NAME = 'writers'
TABLE = (
    "CREATE TABLE IF NOT EXISTS writers ("
    "  id int(11) NOT NULL AUTO_INCREMENT,"
    "  name varchar(60) NOT NULL,"
    "  PRIMARY KEY (id)"
    ") ENGINE=InnoDB")
