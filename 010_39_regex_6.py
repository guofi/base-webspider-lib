import re

"""
加了一个换行符:

.*? 就不能匹配了，所以导致匹配失败。这里只需加一个修饰符 re.S，即可修正这个错误
"""


def fun():
    content = '''Hello 1234567 World_This
    is a Regex Demo
    '''
    # result = re.match('^He.*?(\d+).*?Demo$', content)
    result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
    print(result.group(1))


"""

"""
if __name__ == "__main__":
    fun()
