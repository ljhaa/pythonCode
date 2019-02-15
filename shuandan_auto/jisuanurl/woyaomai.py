
#coding:utf-8
import urllib
from jisuanurl import url_send
import json


def woyaomai_url():
    url = "http://hpg.zr44.com/public/apprentice.php/task/index.html"

    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "hpg.zr44.com",
        "Referer": "http://hpg.zr44.com/public/apprentice.php/task/submitted.html",
        "Upgrade-Insecure-Requests": 1,
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"
    }

    str = url_send.url_sund(url,None,header,"GET")

    print(str)
    return str

woyaomai_url()