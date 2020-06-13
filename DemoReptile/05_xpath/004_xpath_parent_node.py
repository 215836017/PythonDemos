from lxml import etree

'''
通过连续的 / 或 // 可以查找子节点或子孙节点，那么假如我们知道了子节点，怎样来查找父节点呢？这可以用.. 来实现。
比如，现在首先选中 href 属性为 link4.html 的 a 节点，然后再获取其父节点，然后再获取其 class 属性，
'''
print('test 11111111111')
html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)
'''
打印结果为：
['item-1']
'''

'''
2. 同时，我们也可以通过 parent:: 来获取父节点，
'''
print('\n\ntest 222222222222')
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)
'''
打印结果为：
['item-1']
'''
