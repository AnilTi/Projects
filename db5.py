## How to update record

import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',db='demo2')

a=conn.cursor()

a.execute("UPDATE COMPANY set SALARY =5000.00 where ID=1")
a.execute("UPDATE COMPANY set NAME ='Lucious' where ID=2")
conn.commit()

a.execute("SELECT id, name, age, address, salary  from COMPANY")
data=a.fetchall()

for row in data:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("AGE = ", row[2])
   print("ADDRESS = ", row[3])
   print("SALARY = ", row[4], "\n")

print("Operation done successfully")
conn.close()
