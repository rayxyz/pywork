#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="www.ray-xyz.com",    # your host, usually localhost
                     user="root",         # your username
                     passwd="rayxyz123",  # your password
                     db="supervisor")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("select t.* from t_attachment t;")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0], row[1], row[3], row[4]

db.close()