import sqlite3
import datetime

def insert(roll_no,fname,lname,day,status):
    conn=sqlite3.connect("college.db")
    cur=conn.cursor()
    # print(roll_no,fname,lname,day,status)
    cur.execute("INSERT INTO attendance VALUES (?,?,?,?,?)",(roll_no,fname,lname,day,status))
    conn.commit()
    conn.close()

def parse(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """

    table = []
    with open(csvfilename, "r") as csvfile:
        for line in csvfile:
            line = line.rstrip()
            columns = line.split(',')
            table.append(columns)
    return table

def feeddb(table):

    for col in table:
        a=int(col[0])
        b=str(col[1])
        c = str(col[2])
        d=(col[3].strip()).split('-')
        dy=int(d[0])
        mon=int(d[1])
        yr=int(d[2])
        d1=datetime.date(yr,mon,dy)
        e=str(col[4])
        insert(a,b,c,d1,e)

table = parse("stu.csv")
feeddb(table)
