import MySQLdb
class MySQLConnectionHandler:
    # Open database connection and set utf-8 encoding as we are using japanese characters
    db = MySQLdb.connect("localhost","root","Async128","Sweety")
    cursor = db.cursor()
    cursor.execute("SET NAMES utf8;")
    cursor.execute("SET CHARACTER SET utf8;")
    cursor.execute("SET character_set_connection=utf8;")

    def getDatabase(self):
        return self.db

    def getCursor(self):
        return self.cursor
