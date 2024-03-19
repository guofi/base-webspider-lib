from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

"""
本地搭建了一个代理，它运行在 9743 端口上。
"""
def fun():
    proxy_handler = ProxyHandler({
        'http': 'http://127.0.0.1:9743',
        'https': 'https://127.0.0.1:9743'
    })
    opener = build_opener(proxy_handler)

    try:
        response = opener.open('https://www.baidu.com')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)


if __name__ == '__main__':
    fun()
