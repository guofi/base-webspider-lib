import requests

"""
Session:
维持同一个会话，也就是相当于打开一个新的浏览器选项卡而不是新开一个浏览器
"""

"""
{
  "cookies": {}
}
"""


def fun():
    requests.get('http://httpbin.org/cookies/set/number/123456789')
    r = requests.get('http://httpbin.org/cookies')
    print(r.text)


"""

{
  "cookies": {
    "number": "123456789"
  }
}
"""


def fun2():
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)


"""

"""
if __name__ == "__main__":
    fun()
    fun2()
