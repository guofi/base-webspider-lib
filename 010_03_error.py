from urllib import request, error

"""
捕获URLError异常：
可以避免程序异常终止，同时异常得到了有效处理。
"""

def fun():
    try:
        response = request.urlopen('https://allen.com/index.htm')
    except error.URLError as e:
        print(e.reason)


if __name__ == "__main__":
    fun()
