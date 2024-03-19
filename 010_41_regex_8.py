import re

"""
search:

match 方法是从字符串的开头开始匹配的，一旦开头不匹配，那么整个匹配就失败

search，它在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果。也就是说，
正则表达式可以是字符串的一部分，在匹配时，search 方法会依次扫描字符串，直到找到第一个符合规则的字符串，
然后返回匹配内容，如果搜索完了还没有找到，就返回 None

如果想要获取匹配正则表达式的所有内容： findall
"""


def fun():
    content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
    result = re.search('Hello.*?(\d+).*?Demo', content)
    print(result)


def fun2():
    html = '''<div id="songs-list">
    <h2 class="title"> 经典老歌 </h2>
    <p class="introduction">
    经典老歌列表
    </p>
    <ul id="list" class="list-group">
    <li data-view="2"> 一路上有你 </li>
    <li data-view="7">
    <a href="/2.mp3" singer="任贤齐"> 沧海一声笑 </a>
    </li>
    <li data-view="4" class="active">
    <a href="/3.mp3" singer="齐秦"> 往事随风 </a>
    </li>
    <li data-view="6"><a href="/4.mp3" singer="beyond"> 光辉岁月 </a></li>
    <li data-view="5"><a href="/5.mp3" singer="陈慧琳"> 记事本 </a></li>
    <li data-view="5">
    <a href="/6.mp3" singer="邓丽君"> 但愿人长久 </a>
    </li>
    </ul>
    </div>'''

    results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)  # 由于代码有换行，所以这里第三个参数需要传入 re.S
    print(results)
    print(type(results))
    for result in results:
        print(result)
        print(result[0], result[1], result[2])


"""
<re.Match object; span=(13, 53), match='Hello 1234567 World_This is a Regex Demo'>

[('/2.mp3', '任贤齐', ' 沧海一声笑 '), ('/3.mp3', '齐秦', ' 往事随风 '), ('/4.mp3', 'beyond', ' 光辉岁月 '), ('/5.mp3', '陈慧琳', ' 记事本 '), ('/6.mp3', '邓丽君', ' 但愿人长久 ')]
<class 'list'>
('/2.mp3', '任贤齐', ' 沧海一声笑 ')
/2.mp3 任贤齐  沧海一声笑 
('/3.mp3', '齐秦', ' 往事随风 ')
/3.mp3 齐秦  往事随风 
('/4.mp3', 'beyond', ' 光辉岁月 ')
/4.mp3 beyond  光辉岁月 
('/5.mp3', '陈慧琳', ' 记事本 ')
/5.mp3 陈慧琳  记事本 
('/6.mp3', '邓丽君', ' 但愿人长久 ')
/6.mp3 邓丽君  但愿人长久 
"""
if __name__ == "__main__":
    # fun()
    fun2()
