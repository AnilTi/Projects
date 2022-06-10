## How to Display all records of table

import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',db='demo2')

a=conn.cursor()

a.execute("SELECT * from COMPANY")

data=a.fetchall()

for row in data:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("AGE = ", row[2])
   print("ADDRESS = ", row[3])
   print("SALARY = ", row[4], "\n")

print("Operation done successfully")
conn.close()
