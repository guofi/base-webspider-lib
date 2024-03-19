import re

"""
贪婪与非贪婪

在贪婪匹配下，. 会匹配尽可能多的字符
非贪婪匹配的写法是 .*?，多了一个 ？

当 .? 匹配到 Hello 后面的空白字符时，再往后的字符就是数字了，而 \d + 恰好可以匹配，那么这里 .? 就不再进行匹配，交给 \d+ 去匹配后面的数字。


在做匹配的时候，字符串中间尽量使用非贪婪匹配，也就是用 .? 来代替 .，以免出现匹配结果缺失的情况。
"""


def fun():
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^He.*?(\d+).*Demo$', content)
    print(result)
    print(result.group(1))


"""
<re.Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
1234567
"""
if __name__ == "__main__":
    fun()
