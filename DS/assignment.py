import sqlite3
connection = sqlite3.connect("college.db")

cursor = connection.cursor()

# delete
# cursor.execute("""DROP TABLE attendance;""")

sql_command = ''' 
CREATE TABLE attendance ( 
roll_no INTEGER, 
fname VARCHAR(20), 
lname VARCHAR(30), 
day DATE,
status CHAR(1) );'''

cursor.execute(sql_command)

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

# for any student based on month/year

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

# for any student based on month/year

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

# for any student based on month/year

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



