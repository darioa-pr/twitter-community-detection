#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect("127.0.0.1", "root", "", "brexit")

cur = db.cursor()

fp = open("brexit_pulita.txt", "r")

for line in fp:

    blocks = line.split('\t', 20)
    userID = blocks[0]
    twitt = blocks[7]
    date = blocks[1]
    name = blocks[2]
    username = blocks[3]
    lat = blocks[8]
    lng = blocks[9]
    type = blocks[10].split('\r')[0]

    try:
        cur.execute("UPDATE users SET name='"+name+"', username='"+username+"', lat="+lat+", lng="+lng+" WHERE userID = " + str(userID))
        #cur.execute("INSERT IGNORE INTO twitts (userID, date, message, type) VALUES (" + str(userID) + " , " + date + " , '" + twitt + "' , " + type + " )")
        db.commit()
    except Exception as e:
        db.rollback()
        print e

pass

fp.close()

db.close()
