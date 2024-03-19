from bs4 import BeautifulSoup

"""
prettify() 方法:

这个方法可以把要解析的字符串以标准的缩进格式输出

"""


def fun(html):
    soup = BeautifulSoup(html, 'lxml')
    print(soup.prettify())
    print(soup.title.string)


if __name__ == '__main__':
    html = '''
    
    <html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>

    
    '''

    fun(html)
