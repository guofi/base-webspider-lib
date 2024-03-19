from urllib.parse import parse_qs

"""
如果我们有一串 GET 请求参数，利用 parse_qs 方法，就可以将它转回字典，示例如下：
"""


def fun():
    query = 'name=germey&age=22'
    print(parse_qs(query))


"""
{'name': ['germey'], 'age': ['22']}
"""
if __name__ == "__main__":
    fun()
