import http.cookiejar, urllib.request

"""
BAIDUID=B0B2EC581D120A27C84698E92FC0FA22:FG=1
BIDUPSID=B0B2EC581D120A27ABEDCC043D465E0B
PSTM=1710816928
BD_NOT_HTTPS=1
"""
def fun():
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('https://www.baidu.com')
    for item in cookie:
        print(item.name + "=" + item.value)


if __name__ == '__main__':
    fun()
