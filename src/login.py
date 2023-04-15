import requests
import re

def login():
    login_url = 'http://172.17.0.1/login.php'
    username = 'admin'
    password = 'password'

    session = requests.Session()

    response = session.get(login_url)
    token = re.findall("user_token'\s*value='(.*?)'", response.text)[0]

    response = session.post(login_url, data={
        'username': username,
        'password': password,
        'user_token': token,
        'Login': 'Login'
    })

    return session