import re

"""
通用匹配

刚才我们写的正则表达式其实比较复杂，出现空白字符我们就写 \s 匹配，出现数字我们就用 \d 匹配，这样的工作量非常大。其实完全没必要这么做，
因为还有一个万能匹配可以用，那就是.（点星）。其中.（点）可以匹配任意字符（除换行符），（星）代表匹配前面的字符无限次，
所以它们组合在一起就可以匹配任意字符了
"""


def fun():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    result = re.match('^Hello.*Demo$', content)
    print(result)
    print(result.group())
    print(result.span())



"""
<re.Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
Hello 123 4567 World_This is a Regex Demo
(0, 41)
"""
if __name__ == "__main__":
    fun()
