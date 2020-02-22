# coding:utf-8
import requests
import json

query = '孙瑜'
''' 下载图片 '''


def download(src, id):
    dir = './' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载')


''' for 循环 请求全部的 url '''
for i in range(0, 86, 20):
    url = 'https://www.douban.com/search?cat=1025&q=' + \
          query + '&limit=20&start=' + str(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    html = requests.get(url=url, headers=headers).text  # 得到返回结果
    response = json.loads(html, encoding='utf-8')  # 将 JSON 格式转换成 Python 对象
    for image in response['images']:
        print(image['src'])  # 查看当前下载的图片网址
        download(image['src'], image['id'])  # 下载一张图片
