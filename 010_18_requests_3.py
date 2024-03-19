import requests

"""
params 接收传递的参数
"""


def fun():
    data = {
        'name': 'germey',
        'age': 22
    }
    r = requests.get("http://httpbin.org/get", params=data)
    print(r.text)


"""
{
  "args": {
    "age": "22", 
    "name": "germey"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.31.0", 
    "X-Amzn-Trace-Id": "Root=1-65f91be9-055676f227ac0f5651bd1209"
  }, 
  "origin": "119.123.41.143", 
  "url": "http://httpbin.org/get?name=germey&age=22"
}

"""
if __name__ == "__main__":
    fun()
