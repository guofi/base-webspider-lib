from urllib.robotparser import RobotFileParser

"""


"""


def fun():
    rp = RobotFileParser()
    rp.set_url('http://www.jianshu.com/robots.txt')
    rp.read()
    print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
    print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))


"""
False
False
"""
if __name__ == "__main__":
    fun()

