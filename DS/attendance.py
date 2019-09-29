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