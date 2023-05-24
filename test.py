import sqlite3
import argparse

parser = argparse.ArgumentParser(description='Specify db and queries.')
parser.add_argument('--db_path', type=str, required=True)
parser.add_argument('--queries_path', type=str, required=True)
args = parser.parse_args()
con = sqlite3.connect(args.db_path)
sqls = open(args.queries_path,'r')
cur = con.cursor()
for line in sqls.readlines():
    print(line.strip())
    cur.execute(line.strip())
res = cur.execute("SELECT t0.c2 FROM t0 GROUP BY t0.c2")
print(res.fetchone())
res = cur.execute("SELECT ALL t0.c2 FROM t0 GROUP BY t0.c2 HAVING ((((((COUNT(t0.c1)) NOT NULL))AND(((t0.c0) BETWEEN (t0.c0) AND (t0.c2)))))AND(t0.c2)) UNION ALL SELECT ALL t0.c2 FROM t0 GROUP BY t0.c2 HAVING (NOT (((((((COUNT(t0.c1)) NOT NULL))AND(((t0.c0) BETWEEN (t0.c0) AND (t0.c2)))))AND(t0.c2)))) UNION ALL SELECT ALL t0.c2 FROM t0 GROUP BY t0.c2 HAVING ((((((((COUNT(t0.c1)) NOT NULL))AND(((t0.c0) BETWEEN (t0.c0) AND (t0.c2)))))AND(t0.c2))) ISNULL)")
print(res.fetchone())