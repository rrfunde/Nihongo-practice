#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from MySQLConnectionHandler import MySQLConnectionHandler

hiragana = ""
english = ""
category = "Regular Verbs"

mysqlConnector = MySQLConnectionHandler()
db = mysqlConnector.getDatabase()
cursor = mysqlConnector.getCursor()

# Parse data from file
filename = "data files/hiragana-english.txt"
file = open(filename, "r")
for line in file:
    hiragana, english = line.split("	", 1)
    print line
    # sql = "INSERT INTO vocabulary(word, \
    #        hiragana, category) \
    #        VALUES ('%s', '%s', '%s')" % \
    #        (english, hiragana, category)
    # try:
    #    # Execute the SQL command
    #    x = cursor.execute(sql)
    #    # Commit your changes in the database
    #    db.commit()
    #    print "success"
    # except:
    #    # Rollback in case there is any error
    #    db.rollback()
    #    print "failed"

# disconnect from server
db.close()
