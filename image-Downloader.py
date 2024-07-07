from bs4 import BeautifulSoup
import urllib.request
import json
from MySQLConnectionHandler import MySQLConnectionHandler

mysqlConnector = MySQLConnectionHandler()
db = mysqlConnector.getDatabase()
cursor = mysqlConnector.getCursor()

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
sql = "SELECT hiragana, word FROM vocabulary"

def get_soup(url, header):
    req = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(req)
    return BeautifulSoup(response, 'html.parser')

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        hiragana = row[0]
        word = row[1] + " animated"
        query = word.split()
        query = '+'.join(query)
        url = "https://www.google.co.in/search?q=" + query + "&source=lnms&tbm=isch"

        soup = get_soup(url, header)
        i = 0
        linkUrl = ""
        for a in soup.find_all("div", {"class": "rg_meta"}):
            link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
            linkUrl = linkUrl + " " + link
            i += 1
            if i > 3:
                break

        sql1 = "UPDATE vocabulary SET imageUrl = %s WHERE hiragana = %s"
        try:
            cursor.execute(sql1, (linkUrl.strip(), hiragana))
            db.commit()
            print("success")
        except Exception as e:
            db.rollback()
            print("failed:", e)
except Exception as e:
    print("Error: unable to fetch data:", e)

# disconnect from server
db.close()
