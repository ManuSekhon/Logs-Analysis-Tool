#!usr/bin/python3

# Internal reporting tool for Logs Analysis

from helpers import Log


DNAME = "news"
db = Log(DNAME)

status = db.badHttpStatus()

for s in status:
    print(s)
