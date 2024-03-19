from lxml import etree

"""
用 // 开头的 XPath 规则来选取所有符合要求的节点
 / 和 // 的区别，其中 / 用于获取直接子节点，// 用于获取子孙节点。
 
 我们知道通过连续的 / 或 // 可以查找子节点或子孙节点，那么假如我们知道了子节点，怎样来查找父节点呢？这可以用.. 来实现。
 
 也可以通过 parent:: 来获取父节点
 
 用 @符号进行属性过滤
 
  text 方法获取节点中的文本
 
 
 可以直接用 // 加 text 方法的方式，这样可以保证获取到最全面的文本信息，但是可能会夹杂一些换行符等特殊字符。
 如果想获取某些特定子孙节点下的所有文本，可以先选取到特定的子孙节点，然后再调用 text 方法方法获取其内部文本，这样可以保证获取的结果是整洁的。
 
"""


def fun(text):
    html = etree.HTML(text)
    # result = html.xpath('//*')
    # result = html.xpath('//li/a')
    # result = html.xpath('//a[@href="link4.html"]/../@class')
    # result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
    # result = html.xpath('//li[@class="item-0"]')
    # result = html.xpath('//li[@class="item-0"]/a/text()')
    result = html.xpath('//li[@class="item-0"]//text()')

    print(result)


'''
[<Element html at 0x1ad63036880>, <Element body at 0x1ad63147f80>, <Element div at 0x1ad63147fc0>, 
<Element ul at 0x1ad6314f040>, <Element li at 0x1ad6314f080>, <Element a at 0x1ad6314f100>, 
<Element li at 0x1ad6314f140>, <Element a at 0x1ad6314f180>, <Element li at 0x1ad6314f1c0>, 
<Element a at 0x1ad6314f0c0>, <Element li at 0x1ad6314f200>, <Element a at 0x1ad6314f240>, 
<Element li at 0x1ad6314f280>, <Element a at 0x1ad6314f2c0>]


[<Element a at 0x2577bf47e80>, <Element a at 0x2577bf47ec0>, <Element a at 0x2577bf47f00>, <Element a at 0x2577bf47f40>, <Element a at 0x2577bf47f80>]


['item-1']

['item-1']

[<Element li at 0x24d39577f80>, <Element li at 0x24d39577fc0>]

['first item', 'fifth item']

['first item', 'fifth item', '\n     ']

'''
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
    fun(text)


