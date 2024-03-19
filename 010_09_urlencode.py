from urllib.parse import urlencode

"""
有时为了更加方便地构造参数，我们会事先用字典来表示。要转化为 URL 的参数时，只需要调用该方法即可。

"""


def fun():
    params = {
        'name': 'germey',
        'age': 22
    }
    base_url = 'http://www.baidu.com?'
    url = base_url + urlencode(params)
    print(url)


"""
http://www.baidu.com?name=germey&age=22
"""
if __name__ == "__main__":
    fun()
