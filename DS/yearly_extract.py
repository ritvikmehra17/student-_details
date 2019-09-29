# for any student based on month/year
import sqlite3
import sys,datetime
roll_no=int(input("Enter Roll No of Student: "))

year=int(input("Enter year : "))

def viewall(roll_no,year):
    sdate=datetime.date(year,1,1)
    edate=datetime.date(year,12,31)
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance where roll_no=? and day>=? and day<=? ", (roll_no,sdate,edate))
    global data
    data= cur.fetchall()
    # print(data)



def feedfile(data):
    f = open('student_details_for_a_year.csv','w')
    for row in data:
        for ele in row:
            f.write(str(ele))
            f.write(',')
        f.write('\n')
    f.close()
viewall(roll_no,year)
feedfile(data)