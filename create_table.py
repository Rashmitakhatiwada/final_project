from  establish_connection import establish_connection

cursor = establish_connection()

cursor.execute("drop table if exists myshare")
sql="""
create table MYSHARE(
date char(20),
symbol char(20),
name char(100),
high float,
low float
)
"""
cursor.execute(sql)
print("table created succesfully !!")
