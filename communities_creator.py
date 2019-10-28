#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect("127.0.0.1", "root", "", "brexit")

cur = db.cursor()

fp = open("Brexit_Reduced [Nodes]_res1.csv", "r")

for line in fp:

    line = line.strip('\n')
    userID, commID = line.split(',')

    try:
        cur.execute("INSERT IGNORE INTO users (userID, communityID) VALUES (" + str(userID) + " , " + str(commID) + ")")
        db.commit()
    except Exception as e:
        db.rollback()
        print e

pass

fp.close()

db.close()
