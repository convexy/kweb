import sqlite3
import datetime

TARGETS = {
    "T_MAP": False,
    "T_MAP2": True,
}

if TARGETS["T_MAP"]:

    DELETE_T_MAP = "delete from T_MAP"
    INSERT_T_MAP = "insert into T_MAP (CX, CY, VAL) values (?, ?, ?)"

    try:
        conn = sqlite3.connect("./db/main.sqlite3")
        conn.execute(DELETE_T_MAP)
        for i in range(1000):
            for j in range(40):
                conn.execute(INSERT_T_MAP, (i, j, i * j / 1000 / 40))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        if conn:
            conn.close()

if TARGETS["T_MAP2"]:

    DELETE_T_MAP2 = "delete from T_MAP2"
    INSERT_T_MAP2 = "insert into T_MAP2 (DT, Y, VAL) values (?, ?, ?)"

    try:
        conn = sqlite3.connect("./db/main.sqlite3")
        conn.execute(DELETE_T_MAP2)
        dt = datetime.datetime(2021, 7, 1, 0, 0, 0)
        for i in range(3600):
            dt = dt + datetime.timedelta(seconds=1)
            for j in range(40):
                conn.execute(INSERT_T_MAP2, (dt, j, i * j / 1000 / 40))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        if conn:
            conn.close()
