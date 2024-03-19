import requests

"""
响应

headers 和 cookies 这两个属性得到的结果分别是 CaseInsensitiveDict 和 RequestsCookieJar 类型

"""


def fun():
    r = requests.get('https://www.baidu.com')
    print(type(r.status_code), r.status_code)
    print(type(r.headers), r.headers)
    print(type(r.cookies), r.cookies)
    print(type(r.url), r.url)
    print(type(r.history), r.history)


"""

<class 'int'> 200
<class 'requests.structures.CaseInsensitiveDict'> {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Tue, 19 Mar 2024 05:22:45 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:24:17 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
<class 'requests.cookies.RequestsCookieJar'> <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
<class 'str'> https://www.baidu.com/
<class 'list'> []
"""
if __name__ == "__main__":
    fun()
