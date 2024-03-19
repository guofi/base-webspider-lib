import re

"""
 match 方法可以得到匹配到的字符串内容
 
 这里可以使用 () 括号将想提取的子字符串括起来。() 实际上标记了一个子表达式的开始和结束位置，
 被标记的每个子表达式会依次对应每一个分组，调用 group 方法传入分组的索引即可获取提取的结果
"""


def fun():
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^Hello\s(\d+)\sWorld', content)
    print(result)
    print(result.group())
    print(result.group(1))
    print(result.span())



"""
<re.Match object; span=(0, 19), match='Hello 1234567 World'>
Hello 1234567 World
1234567
(0, 19)
"""
if __name__ == "__main__":
    fun()
