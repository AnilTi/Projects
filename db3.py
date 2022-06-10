## How to insert records into a table

import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',db='demo2')

a=conn.cursor()

a.execute("INSERT INTO COMPANY VALUES(1, 'Paul', 32, 'California',20000.00)")
a.execute("INSERT INTO COMPANY VALUES(2, 'Sam', 31, 'Bahamas', 40000.00 )")
a.execute("INSERT INTO COMPANY VALUES(3, 'Dean', 35, 'Corsica', 10000.00 )")
a.execute("INSERT INTO COMPANY VALUES(4, 'Lucy', 36, 'Amazon', 90000.00 )")
a.execute("INSERT INTO COMPANY VALUES(5, 'John', 37, 'Mars', 22000.00 )")
a.execute("INSERT INTO COMPANY VALUES(6, 'Gerard', 22, 'Texas', 30000.00 )")
conn.commit()

print("Records Inserted....")


conn.close()
