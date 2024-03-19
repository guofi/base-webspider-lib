import requests
import os

"""

抓取二进制数据
wb: 表示以二进制写的形式打开，可以向文件里写入二进制数据

"""


def fun():
    r = requests.get("https://github.com/favicon.ico")
    # print(r.text)
    # print(r.content)
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)


"""

"""
if __name__ == "__main__":
    fun()
