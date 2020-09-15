import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"core\Level 2\Challenge 2\Data.db"

    sql_create_employee_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        employee_id integer PRIMARY KEY,
                                        first_name text NOT NULL,
                                        last_name text NOT NULL,
                                        age integer NOT NULL,
                                        salary integer NOT NULL
                                        
                                    ); """

    

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_employee_table)
        print("DATABASE CREATED")

        # create tasks table
       
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
try:
    sqliteConnection = sqlite3.connect('core\Level 2\Challenge 2\Data.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO projects
                          (employee_id, first_name, last_name, age, salary) 
                           VALUES 
                          (1,'Evenly','Grace','26',280),
                          (2,'Ovilia','Harper','28',320),
                          (3,'Robert','Hall','36',310),
                          (4,'Doug','Judy','32',280),
                          (5,'Leo','Grace','233',280),"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")