import http.cookiejar, urllib.request

"""
MozillaCookieJar:
可以用来处理 Cookies 和文件相关的事件，比如读取和保存 Cookies，
可以将 Cookies 保存成 Mozilla 型浏览器的 Cookies 格式。

"""


def write():
    filename = 'cookies.txt'
    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('https://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)


def read():
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('cookies2.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    read()
