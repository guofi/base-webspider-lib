from urllib.parse import urlunparse

"""
urlunparse: 实现了url的构造。
它接受的参数是一个可迭代对象，但是它的长度必须是 6，否则会抛出参数数量不足或者过多的问题。
"""


def fun():
    data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
    print(urlunparse(data))


"""
https://www.baidu.com/index.html;user?a=6#comment
"""
if __name__ == "__main__":
    fun()
