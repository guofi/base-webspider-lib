from urllib.parse import urlparse

"""
ParseResult 类型的对象，它包含 6 个部分，
分别是 scheme、netloc、path、params、query 和 fragment。

标准的链接格式： scheme://netloc/path;params?query#fragment
 #后面是锚点，用于直接定位页面内部的下拉位置。
"""


def fun():
    result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
    print(result)


"""

ParseResult(scheme='https', netloc='', path='www.baidu.com/index.html', params='user', query='id=5', fragment='comment')


"""
if __name__ == "__main__":
    fun()
