from urllib.parse import quote

"""

将中文字符转化为 URL 编码

"""


def fun():
    keyword = '壁纸'
    url = 'https://www.baidu.com/s?wd=' + quote(keyword)
    print(url)


"""
https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8
"""
if __name__ == "__main__":
    fun()
