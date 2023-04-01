from establish_connection import establish_connection
from  read_csv import read_csv

data = read_csv()
cursor = establish_connection()

for each in data[:5]:
    date = each['date']
    symbol = each['symbol']
    name = each['name']
    high = each['high']
    low = each['low']

    # print(each)

    sql = f"""
    insert into MYSHARE(DATE,SYMBOL,NAME,HIGH,LOW)
    VALUES('{date}','{symbol}','{name}','{high}','{low}')
    """
    cursor.execute(sql)
    print("data inserted successfully")