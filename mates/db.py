import psycopg2 
import logging
log = logging.getLogger("db.py")

class database:

    def get_db_con(self):
        try:

            self.connection = psycopg2.connect(user = "root",
                                          password = "",
                                          host = "localhost",
                                          port = "3306",
                                          database = "test")
            connection =self.connection
            self.cursor = connection.cursor()
            log.info("Connected to database ")

        except (Exception, psycopg2.Error) as error :
            log.error ("Error while connecting to Xampp", error)

        return (connection, self.cursor)


    def close_db_con(self):
        if(self.connection):
            self.cursor.close()
            self.connection.close()
            log.info("Xampp connection is closed")