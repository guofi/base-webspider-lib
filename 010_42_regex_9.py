import re

"""
sub： 来修改文本。比如，想要把一串文本中的所有数字都去掉，如果只用字符串的 replace 方法，那就太烦琐了，这时可以借助 sub 方法

"""


def fun():
    content = '54aK54yr5oiR54ix5L2g'
    content = re.sub('\d+', '', content)
    print(content)


'''
aKyroiRixLg
'''
if __name__ == "__main__":
    fun()
