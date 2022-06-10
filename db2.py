## How to create table of selected database

import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',db='demo2')

a=conn.cursor()

a.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY  NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT  NOT NULL,
        ADDRESS CHAR(50),
        SALARY  REAL)''')

print("Table created successfully")

conn.close()
