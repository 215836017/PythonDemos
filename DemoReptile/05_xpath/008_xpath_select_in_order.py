from lxml import etree

'''
1. 有时候，我们在选择的时候某些属性可能同时匹配了多个节点，但是只想要其中的某个节点，这时可以利用中括号传入索引的方法获取特定次序的节点
'''
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print('test 11111111111')
print(result)
result = html.xpath('//li[last()]/a/text()')
print('\n\ntest 22222')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print('\n\ntest 33333')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print('\n\ntest 4444444')
print(result)
'''
打印结果为：
test 11111111111
['first item']

test 22222
['fifth item']

test 33333
['first item', 'second item']

test 4444444
['third item']
'''
'''
这里我们使用了 last、position 等方法。在 XPath 中，提供了 100 多个方法，包括存取、数值、字符串、逻辑、节点、序列等处理功能，
它们的具体作用可以参考：http://www.w3school.com.cn/xpath/xpath_functions.asp。
'''
