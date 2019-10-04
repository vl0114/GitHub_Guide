import psycopg2 as pq
from secret import *
import meta


class psql:
    print("d")
    conn = pq.connect(
        host=SECRET.DB.HOST,
        user=SECRET.DB.USER,
        password=SECRET.DB.PW,
        port=SECRET.DB.PORT,
        database=SECRET.DB.DB
    )
    cur = conn.cursor()
    print(conn.get_dsn_parameters(), "\n")
    rows = cur.fetchall()
    print(rows)

    def send(self, q):
        pass

