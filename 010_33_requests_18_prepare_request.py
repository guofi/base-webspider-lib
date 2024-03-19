from requests import Request, Session

"""
urllib 中，我们可以将请求表示为数据结构，其中各个参数都可以通过一个 Request 对象来表示。
这在 requests 里同样可以做到，这个数据结构就叫 Prepared Request

"""


def fun():
    url = 'http://httpbin.org/post'
    data = {'name': 'germey'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
        }
    s = Session()
    req = Request('POST', url, data=data, headers=headers)
    prepped = s.prepare_request(req)
    r = s.send(prepped)
    print(r.text)



"""
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "name": "germey"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "11", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65f92c0f-110101624c1f635b1c2ff894"
  }, 
  "json": null, 
  "origin": "119.123.41.143", 
  "url": "http://httpbin.org/post"
}
"""
if __name__ == "__main__":
    fun()
