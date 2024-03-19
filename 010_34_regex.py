import re

"""
match 方法会尝试从字符串的起始位置匹配正则表达式，如果匹配，就返回匹配成功的结果；如果不匹配，就返回 None
"""


def fun():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
    print(result)
    print(result.group())
    print(result.span())



"""
41
<re.Match object; span=(0, 25), match='Hello 123 4567 World_This'>
Hello 123 4567 World_This
(0, 25)
"""
if __name__ == "__main__":
    fun()
