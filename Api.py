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
        sql = "select DISTINCT(category) from vocabulary;"
        try:
           cursor.execute(sql)
           results = cursor.fetchall()
           categories = [i[0] for i in results]
           response = {}
           response["categories"] = categories
           return jsonify(response)
        except:
            return "unknown error occured"


@app.route('/get/words', methods=["post"])
def getWords():
    req = request.json
    word = hiragana = romaji = kanji = example = category = ''
    no = ' no>=0 '
    count = ' limit 10000'
    returnValues = '*'
    if req is None:
        return "Invalid request parameter.", 400

    if 'no' in req:
        no = ' no>=' + str(req['no']) + ' '
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

        rowHeaders=[x[0] for x in cursor.description] #this will extract row headers
        results = cursor.fetchall()

        jsonData=[]
        for item in results:
            jsonData.append(dict(zip(rowHeaders, item)))
        return jsonify(jsonData)
    except:
        return "Invalid request parameter.", 400

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

@app.route('/')
def root():
    return app.send_static_file('home.html')

@app.route('/practice')
def practice():
    return app.send_static_file('practice.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
