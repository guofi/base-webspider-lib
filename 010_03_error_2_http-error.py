from urllib import request, error

"""
HTTPError：
 URLError 的子类
 
有如下 3 个属性:
code：返回 HTTP 状态码，比如 404 表示网页不存在，500 表示服务器内部错误等。
reason：同父类一样，用于返回错误的原因。
headers：返回请求头。
"""


def fun():
    try:
        response = request.urlopen('https://baidu.com/1.htm')
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
    except error.URLError as e:
        print(e.reason)
    else:
        print('Request Successfully')


"""
Not Found
404
Content-Length: 203
Content-Type: text/html; charset=iso-8859-1
Date: Tue, 19 Mar 2024 03:11:20 GMT
Server: Apache
Connection: close
"""
if __name__ == "__main__":
    fun()
