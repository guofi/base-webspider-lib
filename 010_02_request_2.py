# coding=utf-8
from urllib import request, parse

"""
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "name": "Germey"
  }, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Content-Length": "11", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)", 
    "X-Amzn-Trace-Id": "Root=1-65f8fae0-3a4e1fe87988eb5b290d290b"
  }, 
  "json": null, 
  "origin": "119.123.41.143", 
  "url": "http://httpbin.org/post"
}
"""


def fun(url):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
               'Host': 'httpbin.org'
               }
    dict = {'name': 'Germey'}
    data = bytes(parse.urlencode(dict), encoding='utf8')
    # req = request.Request(url=url, data=data, headers=headers, method='POST')

    req = request.Request(url=url, data=data, method='POST')
    req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')

    res = request.urlopen(req)
    print(res.read().decode('utf-8'))


if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    fun(url)
