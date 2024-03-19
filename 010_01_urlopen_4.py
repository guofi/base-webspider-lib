# coding=utf-8
import urllib.error
import urllib.request
import socket

"""
可以通过设置这个超时时间来控制一个网页如果长时间未响应，就跳过它的抓取。这可以利用 try except 语句来实现
"""


def resp(url):
    try:
        response = urllib.request.urlopen(url, timeout=0.1)
        print(response.read())
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')


if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    resp(url)
