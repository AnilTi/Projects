## pip install pymysql
## How to connect Mysql database & create new database

import pymysql
conn=pymysql.connect(host='localhost',user='root',password='')

a=conn.cursor()
a.execute('create database demo2')
print("demo Database created")

