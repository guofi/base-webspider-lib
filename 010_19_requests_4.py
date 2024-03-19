import requests

"""
json 获取字典格式的数据
"""


def fun():
    r = requests.get("http://httpbin.org/get")
    print(type(r.text))
    print(r.json())
    print(type(r.json()))


"""
<class 'str'>
{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 
'User-Agent': 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-65f91c5a-20dc97a77f1717cc55b81e18'},
 'origin': '119.123.41.143', 'url': 'http://httpbin.org/get'}
<class 'dict'>

"""
if __name__ == "__main__":
    fun()
