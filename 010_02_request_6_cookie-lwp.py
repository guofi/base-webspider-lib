import http.cookiejar, urllib.request

"""
LWPCookieJar :
保存的格式和 MozillaCookieJar 不一样，它会保存成 libwww-perl(LWP) 格式的 Cookies 文件

"""


def fun():
    filename = 'cookies2.txt'
    cookie = http.cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('https://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)


if __name__ == '__main__':
    fun()
