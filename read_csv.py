import csv
import json

def read_csv():
    with open("share.csv" , 'r') as fp :
        reader= csv.reader(fp, delimiter=',')
        shares = []
        for index, data in enumerate(reader):
            if index==0:
                continue
            # print(data)
            each ={
                "date": data[1],
                "symbol": data[3],
                "name": data[4],
                "high": data[6],
                "low": data[7],
            }
            shares.append(each)

    return shares

    # print(shares)
#
# with open("first_five.csv",'w') as fp:
#     data = shares[:5]
#     json.dump(data, fp, indent=2)
# print("data added successful")

