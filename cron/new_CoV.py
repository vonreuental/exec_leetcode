import requests
import time
import json
import pandas as pd


time = int(time.time() * 1000)

url = "https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_time_line&callback=jQuery34106544350360778219_1580991577861&_=" + \
    str(time)

res = requests.get(url).text
data_jaon = json.loads(json.loads(res[41:len(res) - 1])['data'])

df = pd.DataFrame(data_jaon)
df = df.sort_values(by="time", ascending=False)
# df = pd.read_json('data.json', encoding='utf-8', orient='recodes')
df.to_excel('new_CoV.xls', encoding='utf-8', index=False, header=False)
# print(df[['title', 'desc', 'source']])
