import requests


host = 'https://api01.aliyun.venuscn.com'
path = '/ip'
method = 'GET'
appcode = '9056891bb6a14b459a95ceafe035675e'
querys = 'ip=101.87.134.78'
bodys = {}
url = host + path + '?' + querys
header = {'Authorization': 'APPCODE ' + appcode}


res = requests.get(url, headers=header, data=bodys)
print(res.json())
