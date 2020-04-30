# Block is responsible for connection and operating SQL database

# Import library for managing SQl DB
import mysql.connector


# Create singlton class for creating permanent connection to DB
class DbInstance(object):
    # Create local variable for creating instances of class
    __instance = None
    # Create local variable for connecting to DB
    __db_connection = None

    # Create constant with name of DB
    DB_NAME = 'BooksDB'

    # Create static method which can be called outside the class that will return the instance of connection
    @staticmethod
    def instance():
        # Create connection if it does not exist
        if not DbInstance.__instance:
            DbInstance.__instance = DbInstance()
        return DbInstance.__instance

    # Create constructor for instances with requisites of DB for connection
    def __init__(self):
        self.__db_connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="CostaRica2017"
        )

    # Function creates connection to DB
    def set_db(self):
        cursor = self.__db_connection.cursor()

        try:
            cursor.execute("USE {};".format(self.DB_NAME))
        except mysql.connector.Error as err:
            print("Failed to set db: {}".format(err))

    # Function gets access to commands for managing DB
    def get_cursor(self):
        if self.__db_connection:
            return self.__db_connection.cursor()
        return None

    # Function commits changes made to DB
    def commit(self):
        if self.__db_connection:
            self.__db_connection.commit()


# Function creates a new DB with two tables: writer and book
def create_db(writer, book):
    # Create an instance of DbInstance class to work with DB
    instance = DbInstance()
    # Get access to commands for managing DB
    cursor = instance.get_cursor()

    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(instance.DB_NAME))
        instance.set_db()
        # create tables here
        cursor.execute(writer)
        cursor.execute(book)
    except mysql.connector.Error as err:
        print("Failed to create db: {}".format(err))


# Functions executes queries to get data from the DB
def get_data(query):
    instance = DbInstance()
    cursor = instance.get_cursor()

    try:
        instance.set_db()
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = [x[0] for x in cursor.description]

        data = []
        for result in rows:
            row = {}
            idx = 0
            for header in headers:
                row[header] = result[idx]
                idx += 1
            data.append(row)
        return data
    except mysql.connector.Error as err:
        print("Failed to fetch data: {}".format(err))


# # Function allows to save changes made in the DB
def execute_command(query):
    instance = DbInstance()
    cursor = instance.get_cursor()

    try:
        instance.set_db()
        cursor.execute(query)
        instance.commit()
    except mysql.connector.Error as err:
        print("Failed to insert/update data: {}".format(err))
