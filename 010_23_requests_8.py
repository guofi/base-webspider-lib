import requests

"""
POST请求

form部分表示提交的数据

"""


def fun():
    data = {'name': 'germey', 'age': '22'}
    r = requests.post("http://httpbin.org/post", data=data)
    print(r.text)


"""

{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "age": "22", 
    "name": "germey"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "18", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.31.0", 
    "X-Amzn-Trace-Id": "Root=1-65f92076-1261765105528b5802a583cd"
  }, 
  "json": null, 
  "origin": "119.123.41.143", 
  "url": "http://httpbin.org/post"
}
"""
if __name__ == "__main__":
    fun()
