import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1

"""
 OAuth 认证，不过此时需要安装 oauth 包
 
 pip3 install requests_oauthlib

"""


def fun():
    # r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
    r = requests.get('http://localhost:5000', auth=('username', 'password'))
    print(r.status_code)


def fun2():
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
                  'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
    requests.get(url, auth=auth)

"""

"""
if __name__ == "__main__":
    fun()
    fun2()
