#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from MySQLConnectionHandler import MySQLConnectionHandler

hiragana = ""
word = ""
category = ""
kanji = ""
romaji = ""
remainingArray = []

mysqlConnector = MySQLConnectionHandler()
db = mysqlConnector.getDatabase()
cursor = mysqlConnector.getCursor()

# Parse data from file
filename = "data files/sample.txt"
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        splitter = " – "
        if splitter not in line:
            splitter = ", "
        rawArray = line.split(splitter)

        if len(rawArray) == 1:
            category = rawArray[0]
            continue
        else:
            hiragana = rawArray[0]
            rawArray = rawArray[1].split("(")
            if len(rawArray) < 2:
                continue
            else:
                word = rawArray[0]
                romaji = rawArray[1][:-2]

        # print(word.strip() + "| " + hiragana.strip() + "| " + kanji.strip() + "| " + romaji.strip() + "| " + category.strip())
        sql = """INSERT INTO vocabulary(word, hiragana, kanji, romaji, category)
                 VALUES (%s, %s, %s, %s, %s)"""
        values = (word.strip(), hiragana.strip(), kanji.strip(), romaji.strip(), category.strip())
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
