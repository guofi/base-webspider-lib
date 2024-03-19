from urllib.robotparser import RobotFileParser
from urllib import request

"""


"""


def fun():
    rp = RobotFileParser()
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
    }

    url = 'http://www.jianshu.com/robots.txt'
    req = request.Request(url=url, headers=headers)
    response = request.urlopen(req)
    rp.parse(response.read().decode('utf-8').split('\n'))
    print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
    print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))

"""
True
False
"""
if __name__ == "__main__":
    fun()
