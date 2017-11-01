#!flask/bin/python
from flask import Flask, jsonify, request
from MySQLConnectionHandler import MySQLConnectionHandler

mysqlConnector = MySQLConnectionHandler()
db = mysqlConnector.getDatabase()
cursor = mysqlConnector.getCursor()

app = Flask(__name__)


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/api/getImage')
def getImage():
    query = ""
    if "num" in request.args:
        query = "and No > " + request.args["num"]

    sql = "select No, word, imageUrl from vocabulary where imageVerified = 'N' " + query + " limit 1;"

    try:
       cursor.execute(sql)
       results = cursor.fetchall()
       response = {}
       if len(results) == 0:
           return ""
       for row in results:
          No = row[0]
          word = row[1]
          imageUrl = row[2]
          response = {"No": No, "word": word, "imageUrl": imageUrl}
       return jsonify(response)
    except:
        return ""

@app.route('/api/setImage', methods=["post"])
def setImage():
    imgUrl = request.form["imgUrl"]
    num = int(request.form["No"])
    sql1 = "UPDATE vocabulary SET imageUrl = (%s), imageVerified= 'Y' WHERE No = (%s)"
    try:
         cursor.execute(sql1, (imgUrl,num))
         db.commit()
         print ("updated No. " + str(num))
         return jsonify({"status": 1})
    except:
         db.rollback()
         print("failed to update")
         return jsonify({"status": 0})

if __name__ == '__main__':
    app.run(debug=True)
