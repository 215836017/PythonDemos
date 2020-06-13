from lxml import etree

print('网页解析库使用 -- XPath')
'''
1. XPath概览：
    XPath，全称XML Path Language，即XML路径语音，它是一门在XML文档中查找信息的语音。最初是用来搜寻XML文档的，但是同样适用于HTML文档的搜索。
所以，在做爬虫中，完全可以使用XPath来做相应的信息抽取。
    XPath的选择功能十分强大，它提供了非常简洁明了的路径选择表达式。另外，它还提供了超过100个内建函数，用于对字符串、数值、时间的匹配以及节点、
序列的处理等。几乎所有我们想要定位的节点，都可以用XPath来选择。
'''

'''
2. XPath常用规则
nodename     选择此节点的所有子节点
/            从当前节点选择直接子节点
//           从当前节点选择子孙节点
.            选取当前节点
..           选取当前节点的父节点
 @           选取属性
 
示例如下：
//title[@lang='eng]
这就是一个XPath规则，它代表选择所有名称为title，同时属性lang的值为eng的节点
'''

'''
3. 实例体验
'''
print('test 1111111111')
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
result = etree.tostring(html)
print(result.decode('utf-8'))

'''
另外，也可以直接读取文本文件进行解析
'''
print('test 2222222222')
html = etree.parse('test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
