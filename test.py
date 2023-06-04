import sqlite3
import argparse
import os
parser = argparse.ArgumentParser(description='Specify db and queries.')
parser.add_argument('--dbs_path', type=str)
parser.add_argument('--queries_path', type=str)
args = parser.parse_args()
total = 0
bug = 0
for db in os.listdir(args.dbs_path):
    sql = db[:-3]+".sql"
    log = os.path.join(args.queries_path, db[:-3]+".log")
    if db[:-3] + ".log" not in os.listdir(args.queries_path):
        continue
    if sql not in os.listdir(args.queries_path):
        continue
    con = sqlite3.connect(db)
    cur = con.cursor()
    for line in open(log).readlines():
        try:
            cur.execute(line)
            con.commit()
        except:
            pass
    
    line = open(os.path.join(args.queries_path, sql)).readlines()
    sql_one = line[0]
    sql_two = line[1]
    try:
        res_one = cur.execute(sql_one)
        res_one = cur.fetchone()
        res_two = cur.execute(sql_two)
        res_two = cur.fetchone()
        file_one = open(os.path.join(args.queries_path, db[:-3]+"_"+sqlite3.sqlite_version+"_result_one.txt"),'w')
        file_one.write(str(res_one))
        file_one.close()
        file_two = open(os.path.join(args.queries_path, db[:-3]+"_"+sqlite3.sqlite_version+"_result_two.txt"),'w')
        file_two.write(str(res_two))
        file_two.close()
        if res_one != res_two:
            bug += 1
        total += 1
    except:
        con.close()
        continue
        pass

    con.close()
print(sqlite3.sqlite_version)
print("total: ", total, "correct: ",total-bug)