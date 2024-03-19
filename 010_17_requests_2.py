import requests

"""

"""


def fun():
    r = requests.get('http://httpbin.org/get')
    print(r.text)


"""
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.31.0", 
    "X-Amzn-Trace-Id": "Root=1-65f91b9e-54a8ae763bdc431d3935dba2"
  }, 
  "origin": "119.123.41.143", 
  "url": "http://httpbin.org/get"
}

"""
if __name__ == "__main__":
    fun()
