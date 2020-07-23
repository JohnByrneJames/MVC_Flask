# To use this database connector you need to first import this class, it will return your connection in the form of a
# cursor. This can be used to work in other classes, as long as you pass them in as arguments of the classes
# initialisation method.
import pyodbc


class DatabaseConnector:
    # Essential attributes needed by database connector to make a connection {Server, Database, Username, Password}
    # Connection_string formulated using credentials and then a cursor that is used to make the retrieval of data from
    # the database.
    __server = None  # Server connection
    __database = None  # Database connection
    __cursor = None  # cursor to access database
    __connection_string = None  # Store connection string for integrity and future storage
    retry_count = 0  # retry count

    def __init__(self, server, database):
        self.__server = server
        self.__database = database
        self.retry_count = 0  # This is used to count the attempts to connect to the database

    def establish_connection(self):  # establishing connection
        # Create, store and connect to the database using this connection string
        # connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" \
        #                     + self.__server + ";DATABASE=" + self.__database + \
        #                     ";UID=" + self.__username + ";PWD=" + self.__password

        connection_string = "Driver={SQL SERVER};Server=" + self.__server + ";Database=" \
                            + self.__database + ";Trusted_connection=yes"

        self.__connection_string = connection_string

        try:
            with pyodbc.connect(self.__connection_string, timeout=5) as connection:  # Connection to database
                # Success and connection has been made
                print("Connection successfully established..!")  # Connection has been established, continue.
        except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):  # Catch common errors faced in pyodbc
            return "connection has timed out, or the database was not available - " \
                   "\nNo point in retrying... Please review connection credentials"
        except pyodbc.InterfaceError:
            # This is an error that is raised when the database interface is not available.
            print("Invalid connection to DB interface")
            print("\nTrying again...")  # Try reconnecting to the database again.
            if self.retry_count == 3:  # After 2 attempts exit
                exit("Error encountered")
            self.retry_count += 1  # Increase the retry timer by 1
            self.establish_connection()  # retry establishing connection by calling itself
        except Exception:  # base Exception makes this fall proof
            # This prevents exceptions falling through the exceptions handler (as this catches all possible exceptions)
            return "There was an error that occurred during the connection attempt..."
        else:
            # Return the connection, the cursor is a control structure
            return connection.cursor()
