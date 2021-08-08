import sqlite3

DELETE_T_MAP = "delete from t_map"
INSERT_T_MAP = "insert into t_map (CX, CY, VAL) values (?, ?, ?)"

try:
    conn = sqlite3.connect("./db/main.sqlite3")
    conn.execute(DELETE_T_MAP)
    for i in range(1000):
        for j in range(40):
            conn.execute(INSERT_T_MAP, (i / 1000.0, j, i * j / 1000 / 40))
    conn.commit()
    print("committed")
except:
    conn.rollback()
    print("rollbacked")
finally:
    if conn:
        conn.close()
        print("closed")
