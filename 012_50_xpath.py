from lxml import etree

"""
HTML 文本中的最后一个 li 节点是没有闭合的，但是 etree 模块可以自动修正 HTML 文本。
经过处理之后，li 节点标签被补全，并且还自动添加了 body、html 节点。
"""


def fun(text):
    html = etree.HTML(text)
    # html = etree.parse('./test.html', etree.HTMLParser()) # 读取文本
    result = etree.tostring(html)
    print(result.decode('utf-8'))


if __name__ == "__main__":
    text = """
    <div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
    """

    html = etree.HTML(text)
    result = etree.tostring(html)
    print(result.decode('utf-8'))
