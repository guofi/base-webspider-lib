from urllib.parse import urlunsplit

"""
urlunsplit:
和 urlunparse 方法非常相似
它也是将链接各个部分组合成完整链接的方法，传入的参数也是一个可迭代对象，例如列表、元组等，唯一的区别是长度必须为 5
"""


def fun():
    data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
    print(urlunsplit(data))


"""
http://www.baidu.com/index.html?a=6#comment
"""
if __name__ == "__main__":
    fun()
