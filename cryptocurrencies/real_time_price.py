import requests
import time
import pandas as pd

url = "http://api.coincap.io/v2/assets?"

payload = {}
headers = {}

dict = {'timestamp':[]}

x = 5
counter = 0

while x > 0:

    time_here = time.localtime()

    year = time_here[0]
    month = time_here[1]
    day = time_here[2]
    hour = time_here[3]
    min = time_here[4]
    sec = time_here[5]

    current_time = "{:02d}/{:02d}/{}, {:02d}:{:02d}:{:02d}".format(day, month, year, hour, min, sec)
    dict['timestamp'].append(current_time);

    for i in range(10):

        response = requests.request("GET", url, headers=headers, data=payload)
        response_json = response.json()

        keys = ['id', 'priceUsd']
        values = list(map(response_json['data'][i].get, keys))
        coin = values[0]
        price = values[1]

        if coin not in dict:
            dict[coin] = [price]
        else:
            dict[coin].append(price)

    x -= 1

    time.sleep(15)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.DataFrame.from_dict(dict)
print(df)
