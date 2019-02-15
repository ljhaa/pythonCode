#coding:utf-8
import urllib
import json
import http.cookiejar


def url_sund(url,postdata,header,math_type):


    req = urllib.request.Request(url=url, data=postdata, headers=header,method=math_type)
    #自动记住cookie
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(req)

    try:
        strmap = r.read().decode('utf-8')
    except UnicodeDecodeError:
        print("eree")
    return strmap