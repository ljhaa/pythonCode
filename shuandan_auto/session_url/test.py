from session_url import login_send





def test():
    session = login_send.get_session()
    url_wym = "http://hpg.zr44.com/public/apprentice.php/task/index.html"
    resp = session.get(url_wym)
    print(resp.content.decode('utf-8'))

test()