
from jisuanurl import url_send,login_url,woyaomai


def login_new_cookie():
    url = "http://hpg.zr44.com/public/apprentice.php/passport/login.html"
    str = url_send.url_sund(url,None,{},"GET")
    print(str)

login_new_cookie()
login_url.login_url()
woyaomai.woyaomai_url()