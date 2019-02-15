#coding:utf-8
import urllib
from jisuanurl import url_send
import json


def login_url():
    url = "http://hpg.zr44.com/public/apprentice.php/passport/ajax_login.html"
    postdata =urllib.parse.urlencode({
        "username": "ljhazyx",
        "password": "ed4b26a319d26fefb5a85ec6b2c52722",
        "remember": 0,
        "callback": None,
        "t": 0.9875236787365168
    }).encode('utf-8')
    header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": 103,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": """apprentice=rd6625ujufcifhv4shbt9k7q05; Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0=1547451236; 
            Hm_lvt_f5df380d5163c1cc4823c8d33ec5fa49=1547451236; hasSubscribeCls524009337=1547537658927; 
            Hm_lpvt_bfc6c23974fbad0bbfed25f88a973fb0=1547451309; Hm_lpvt_f5df380d5163c1cc4823c8d33ec5fa49=1547451309""",
            "Host": "hpg.zr44.com",
            "Origin": "http://hpg.zr44.com",
            "Referer": "http://hpg.zr44.com/public/apprentice.php/passport/login.html",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
    }

    str = url_send.url_sund(url,postdata,header,"POST")
    thisstr = json.loads(str)
    print(thisstr["msg"])
    return thisstr

login_url()