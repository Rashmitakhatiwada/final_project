from establish_connection import establish_connection

cursor = establish_connection()
sql="""
update myshare set 
name = 'laxmi bank'
where symbol = 'LBL'
"""

cursor.execute(sql)
print("data updated successfully")