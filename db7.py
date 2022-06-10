import sqlite3 as db

conn=db.connect('demo.db')

conn.execute('drop table if exists temps')
conn.execute("create table temps(data text,temp int)")
conn.execute("insert into temps values('22mar',22)")
conn.execute("insert into temps values('23mar',29)")
conn.execute("insert into temps values('24mar',27)")
conn.execute("insert into temps values('25mar',27)")
conn.commit()

cursor=conn.execute('select * from temps')
rows=cursor.fetchall()

for row in rows:
    print ("%s %d" %(row[0],row[1]))



conn.execute('delete from temps  where temp=29')
conn.commit()

cursor=conn.execute('select * from temps')
rows=cursor.fetchall()

for row in rows:
    print ("%s %d" %(row[0],row[1]))

conn.close()
