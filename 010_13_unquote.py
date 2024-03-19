from urllib.parse import unquote

"""

将中文字符转化为 URL 编码

"""


def fun():

    url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
    print(unquote(url))


"""
https://www.baidu.com/s?wd=壁纸
"""
if __name__ == "__main__":
    fun()
