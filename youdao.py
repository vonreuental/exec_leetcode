import json
import time
import requests
import random
import hashlib


def md5(e, salt):
    sign_str = "fanyideskweb" + e + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
    md5 = hashlib.md5()
    md5.update(sign_str.encode())
    return md5.hexdigest()


def translate(type, text):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Cookie": "DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=-1060991336@101.87.134.78; JSESSIONID=abcgrDg4f7vUD96zUjqax; OUTFOX_SEARCH_USER_ID_NCOO=13650470.730056982; _ntes_nnid=004cfb2674a17c77ee5c13bfefd52c34,1580818969049; ___rl__test__cookies=1580819099612",
        "Referer": "http://fanyi.youdao.com/?keyfrom=fanyi-new.logo"}

    ts = str(int(time.time() * 1000))
    salt = ts + str(random.randint(0, 9))

    to = "en" if type == "1" else "ja"

    data = {
        "i": text,
        "from": "zh-CHS",
        "to": to,
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": md5(text, salt),
        "ts": ts,
        "bv": "901200199a98c590144a961dac532964",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }
    res = requests.post(url, headers=header, data=data).text
    return json.loads(res)["translateResult"][0][0]["tgt"]


while True:
    type = input("请选择中翻英（输入：1）或者中翻日（输入2）：")
    if type.upper() == "Q":
        break
    elif type == "1" or type == "2":
        find_text = input("请输入需要翻译的单词:")
        print(f"[{find_text}]翻译的结果是：{translate(type, find_text)}")
        print("退出请输入(Q)\n")
    else:
        print("翻译类型输入错误")
        continue
