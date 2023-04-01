from establish_connection import establish_connection

cursor = establish_connection()
sql = """
select * from myshare
"""

cursor.execute(sql)
result = cursor.fetchall()
print(result)
