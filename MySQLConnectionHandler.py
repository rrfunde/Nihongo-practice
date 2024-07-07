import mysql.connector

class MySQLConnectionHandler:
    def __init__(self):
        # Open database connection and set utf-8 encoding as we are using Japanese characters
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Sweety"
        )
        self.cursor = self.db.cursor()
        self.cursor.execute("SET NAMES utf8;")
        self.cursor.execute("SET CHARACTER SET utf8;")
        self.cursor.execute("SET character_set_connection=utf8;")

    def getDatabase(self):
        return self.db

    def getCursor(self):
        return self.cursor
