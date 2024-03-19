# coding=utf-8
import urllib.request

"""
timeout 参数: 秒
urllib.error.URLError: <urlopen error timed out>
"""
def resp(url):
    response = urllib.request.urlopen(url, timeout=0.001)
    print(response.read())


if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    resp(url)
