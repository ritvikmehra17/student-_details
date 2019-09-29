# for any student based on month/year
import sqlite3
import sys,datetime
roll_no=int(input("Enter Roll No of Student: "))


def viewall(roll_no):

    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance where roll_no=?  ", (roll_no,))
    global data
    data= cur.fetchall()

def feedfile(data):
    f = open('details_for_a_student.csv','w')
    for row in data:
        for ele in row:
            f.write(str(ele))
            f.write(',')
        f.write('\n')
    f.close()
viewall(roll_no)
feedfile(data)