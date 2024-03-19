import re

"""
转义匹配
"""


def fun():
    content = '(百度) www.baidu.com'
    result = re.match('\(百度\) www\.baidu\.com', content)
    print(result)


"""
<re.Match object; span=(0, 18), match='(百度) www.baidu.com'>
"""
if __name__ == "__main__":
    fun()
