import os
import pymysql
import dotenv
import random


dotenv.load_dotenv(dotenv_path='.env')
hostenv = os.getenv('host')
userenv = os.getenv("user")
passwordenv = os.getenv("password")
dbenv = os.getenv("db")
charsetenv = os.getenv("charset")


def selectUsers(uid, upw):
    db1 = pymysql.connect(host=hostenv, user=userenv, password=passwordenv, db=dbenv, charset=charsetenv)
    cur1 = db1.cursor()
    row = None
    setkey = None
    try:
        sql = "SELECT userNo, userName, serverNo, userRole FROM pondUser WHERE userPasswd=password(%s) AND userId=%s AND attrib NOT LIKE %s"
        cur1.execute(sql, (upw, uid, str("%XXX")))
        row = cur1.fetchone()
        if row is not None:
            setkey = random.randint(100000,999999)
    except Exception as e:
        print('접속오류', e)
    finally:
        cur1.close()
        db1.close()
    return row


