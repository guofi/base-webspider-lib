import socket
import urllib
from urllib import request, error

"""
HTTPError：

reason 属性返回的不一定是字符串，也可能是一个对象

"""


def fun():
    try:
        response = request.urlopen('https://baidu.com', timeout=0.001)
    except urllib.error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')


"""
<class 'socket.timeout'>
TIME OUT
"""
if __name__ == "__main__":
    fun()
