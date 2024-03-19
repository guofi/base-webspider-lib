import requests

"""
实际上，请求分为两个阶段，即连接（connect）和读取（read）。
 timeout 将用作连接和读取这二者的 timeout 总和。

如果要分别指定，就可以传入一个元组：


如果想永久等待，可以直接将 timeout 设置为 None，或者不设置直接留空，因为默认是 None。这样的话，如果服务器还在运行，但是响应特别慢，那就慢慢等吧，它永远不会返回超时错误的。或直接不加参数：
"""


def fun():
    # r = requests.get('https://www.taobao.com', timeout=1)
    # r = requests.get('https://www.taobao.com', timeout=(5, 30))
    # r = requests.get('https://www.taobao.com', timeout=None)
    r = requests.get('https://www.taobao.com')
    print(r.status_code)


"""

"""
if __name__ == "__main__":
    fun()
