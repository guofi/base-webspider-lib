import re

"""
贪婪与非贪婪


？ --> 匹配 0 个或 1 个前面的正则表达式定义的片段，非贪婪方式

在做匹配的时候，字符串中间尽量使用非贪婪匹配，也就是用 .? 来代替 .，以免出现匹配结果缺失的情况。
"""


def fun():
    content = 'http://weibo.com/comment/kEraCN'
    result1 = re.match('http.*?comment/(.*?)', content)
    result2 = re.match('http.*?comment/(.*)', content)
    print('result1', result1.group(1))
    print('result2', result2.group(1))


"""
result1 
result2 kEraCN
"""
if __name__ == "__main__":
    fun()
