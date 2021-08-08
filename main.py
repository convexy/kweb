import json
import sqlite3
from sqlite3.dbapi2 import connect
from bottle import Bottle, static_file, request

app = Bottle()


def getT_MAP():
    ret = []
    conn = sqlite3.connect("./db/main.sqlite3")
    cur = conn.cursor()
    for row in cur.execute("select CX, CY, VAL from T_MAP"):
        ret.append([row[0], row[1], row[2]])
    cur.close()
    conn.close()
    return ret


@app.get("/")
@app.get("/<path:path>")
def callback(path="index.html"):
    if path.split("/")[0] == "data":
        return json.dumps(getT_MAP())
    return static_file(path, root="./htdocs")


app.run(host='localhost', port=8080, debug=True)
