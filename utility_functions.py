from datetime import datetime
import json
import requests

old_csrf = "8XVjDGraABm8hdOBGfAaXAyxERBSnV27"

def get_cookie():
    login_url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
    insta_session = requests.Session()
    time = int(datetime.now().timestamp())
    csrf = old_csrf

    payload = {
        'username': 'reel_iterator',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:ujjwal2887#@',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/",
        "x-csrftoken":csrf
    }

    login_response = insta_session.post(login_url, data=payload, headers=login_header)
    json_data = json.loads(login_response.text)

    if json_data["authenticated"]:
        cookies = login_response.cookies
        cookie_jar = cookies.get_dict()
        csrf = cookie_jar['csrftoken']
        cookie = ''
        for i in cookie_jar:
            ck = "{0}={1};".format(i, cookie_jar[i])
            cookie+=ck
        return cookie
    else:
        return 'failed'