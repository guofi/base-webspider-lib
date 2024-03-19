from urllib.parse import urlsplit

"""
urlsplit:
和 urlparse 方法非常相似，只不过它不再单独解析 params 这一部分，只返回 5 个结果。上面例子中的 params 会合并到 path 中

SplitResult: 可以用属性获取值，也可以用索引来获取
"""


def fun():
    result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
    # print(result)
    print(result.scheme, result[0])  # http http


"""
SplitResult(scheme='http', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')
"""
if __name__ == "__main__":
    fun()
