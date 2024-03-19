from urllib.parse import urljoin

"""
有了 urlunparse 和 urlunsplit 方法，我们可以完成链接的合并，不过前提必须要有特定长度的对象,
链接的每一部分都要清晰分开。

urljoin: 实现链接的解析、拼合与生成

提供一个 base_url（基础链接）作为第一个参数，将新的链接作为第二个参数，该方法会分析 base_url 的 
scheme、netloc 和 path 这 3 个内容并对新链接缺失的部分进行补充，最后返回结果

base_url 提供了三项内容 scheme、netloc 和 path。如果这 3 项在新的链接里不存在，就予以补充；
如果新的链接存在，就使用新的链接的部分。而 base_url 中的 params、query 和 fragment 是不起作用的。

"""


def fun():
    print(urljoin('http://www.baidu.com', 'FAQ.html'))
    print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
    print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
    print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
    print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
    print(urljoin('http://www.baidu.com', '?category=2#comment'))
    print(urljoin('www.baidu.com', '?category=2#comment'))
    print(urljoin('www.baidu.com#comment', '?category=2'))


"""

http://www.baidu.com/FAQ.html
https://cuiqingcai.com/FAQ.html
https://cuiqingcai.com/FAQ.html
https://cuiqingcai.com/FAQ.html?question=2
https://cuiqingcai.com/index.php
http://www.baidu.com?category=2#comment
www.baidu.com?category=2#comment
www.baidu.com?category=2

"""
if __name__ == "__main__":
    fun()
