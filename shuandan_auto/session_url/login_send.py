import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

def get_session():

    url = "http://hpg.zr44.com/public/apprentice.php/passport/login.html"



    #构造Session
    session = requests.Session()

    resp = session.get(url)

    #登录后才能访问的网页
    postdata ={
        "username": "ljhazyx",
        "password": "ed4b26a319d26fefb5a85ec6b2c52722",
        "remember": 0,
        "callback": None,
        "t": 0.9875236787365168
    }

    #登录时表单提交到的地址（用开发者工具可以看到）
    login_url = 'http://hpg.zr44.com/public/apprentice.php/passport/ajax_login.html'
    resp = session.post(login_url, postdata)
    print(resp.content.decode('utf-8'))

    return session

