#!flask/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from MySQLConnectionHandler import MySQLConnectionHandler

mysqlConnector = MySQLConnectionHandler()
db = mysqlConnector.getDatabase()
cursor = mysqlConnector.getCursor()

app = Flask(__name__)

@app.route('/get/category')
def getCategory():
        sql = "select DISTINCT(category) as category from vocabulary;"
        try:
           cursor.execute(sql)
           results = cursor.fetchall()
           response = {}
        #    return len(result)
           return jsonify(results)
        except:
            return "unknown error occured"


@app.route('/get/words', methods=["post"])
def getWords():
    req = request.json
    word = hiragana = romaji = kanji = example = category = ''
    no = 0
    count = ' limit 10000'
    returnValues = '*'
    if req is None:
        return "Invalid request parameter.", 400
    
    if 'no' in req:
        no = 'no>=' + str(req['no']) + ' '
    # if 'word' in req:
    #     word = formatQueryForDB('word', req['word'])
    # if 'hiragana' in req:
    #     hiragana = formatQueryForDB('hiragana', req['hiragana'])
    # if 'kanji' in req:
    #     kanji = formatQueryForDB('kanji', req['kanji'])
    # if 'example' in req:
    #     example = formatQueryForDB('example', req['example'])
    # if 'returnValues' in req:
    #     returnValues = req['returnValues']
    if 'category' in req:
        category = ' and ' + formatQueryForDB('category', req['category'])
    if 'count' in req:
        count = ' limit ' + str(req['count'])


    query = 'select ' + returnValues + ' from vocabulary where ' + no + category + count + ';'
    print query
    try:
        resultCount = cursor.execute(query)
        result = cursor.fetchall()
        db.commit()
        return jsonify(result)
    except:
        db.rollback()

    return jsonify(no)

def parseRequestParameters(parameter, value):
    return 0

def formatQueryForDB(parameter, value):
    if len(value) == 1:
        return parameter + " regexp '" + value[0] + "' "
    formattedQuery = parameter + ' regexp '
    val = "'"
    for i in value:
        val += str(i) + '|'
    val = val[:-1] + "'"
    return formattedQuery + val

if __name__ == '__main__':
    app.run(debug=True)
