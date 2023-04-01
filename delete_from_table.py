from establish_connection import establish_connection

cursor = establish_connection()
sql ="""
delete from myshare 
where symbol ='CFCL'
"""

cursor.execute(sql)
print("data deleted successfully !!")