from urllib.parse import parse_qsl

"""

 parse_qsl 方法，它用于将参数转化为元组组成的列表

"""


def fun():
    query = 'name=germey&age=22'
    print(parse_qsl(query))


"""
[('name', 'germey'), ('age', '22')]
"""
if __name__ == "__main__":
    fun()
