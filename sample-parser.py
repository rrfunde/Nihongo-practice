#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
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
filename = "sample.txt"
file = open(filename, "r")
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
        if len(rawArray) < 1:
            continue
        else:
            word = rawArray[0]
            romaji = rawArray[1][:-2]

    # print word.strip() + "| " + hiragana.strip() + "| " + kanji.strip() + "| " + romaji.strip() + "| " + category.strip()
    sql = "INSERT INTO vocabulary(word, \
           hiragana, kanji, romaji, category) \
           VALUES ('%s', '%s', '%s', '%s', '%s')" % \
           (word.strip(), hiragana.strip(), kanji.strip(), romaji.strip(), category.strip())
    try:
       # Execute the SQL command
       x = cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
       print "success"
    except:
       # Rollback in case there is any error
       db.rollback()
       print "failed"

# disconnect from server
db.close()
