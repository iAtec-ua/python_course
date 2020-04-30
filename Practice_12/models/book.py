# Constructor for books SQL table

TABLE_NAME = 'books'
TABLE = (
    "CREATE TABLE IF NOT EXISTS books ("
    "  id int(11) NOT NULL AUTO_INCREMENT,"
    "  name varchar(100) NOT NULL,"
    "  description varchar(255) NOT NULL,"
    "  writerId int(11) NOT NULL,"
    "  PRIMARY KEY (id)"
    ") ENGINE=InnoDB")
