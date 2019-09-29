# for any student based on month/year
import sqlite3
import sys,datetime
#roll_no=int(input("Enter Roll No of Student: "))
#month=int(input("Enter Month in digits: "))
#year=int(input("Enter year : "))

def viewall():
    sdate=datetime.date(2018,4,1)
    edate=datetime.date(2018,4,30)
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance where day>=? and day<=? ", (sdate,edate))
    global data
    data= cur.fetchall()

def feedfile(data):
    f = open('student_details_for_a_month.csv','w')
    for row in data:
        for ele in row:
            f.write(str(ele))
            f.write(',')
        f.write('\n')
    f.close()
viewall()
feedfile(data)
