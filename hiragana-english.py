#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from MySQLConnectionHandler import MySQLConnectionHandler

hiragana = ""
english = ""
category = "Regular Verbs"

mysqlConnector = MySQLConnectionHandler()
db = mysqlConnector.getDatabase()
cursor = mysqlConnector.getCursor()

# Parse data from file
filename = "data files/hiragana-english.txt"
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        hiragana, english = line.split("\t", 1)
        print(line.strip())

        sql = "INSERT INTO vocabulary (word, hiragana, category) VALUES (%s, %s, %s)"
        values = (english.strip(), hiragana.strip(), category)

        try:
            # Execute the SQL command
            cursor.execute(sql, values)
            # Commit your changes in the database
            db.commit()
            print("success")
        except Exception as e:
            # Rollback in case there is any error
            db.rollback()
            print("failed:", e)

# disconnect from server
db.close()
