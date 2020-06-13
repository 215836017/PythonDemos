from lxml import etree

'''
1. 通过 / 或 // 即可查找元素的子节点或子孙节点。假如现在想选择 li 节点的所有直接 a 子节点，可以这样实现：
'''
print('test 11111111111')
html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)
'''
打印结果为：
[<Element a at 0x28714b17200>, <Element a at 0x28714b17240>, <Element a at 0x28714b17280>, <Element a at 0x28714b172c0>, 
<Element a at 0x28714b17300>]
'''
'''
这里通过追加 /a 即选择了所有 li 节点的所有直接 a 子节点。因为 //li 用于选中所有 li 节点，/a 用于选中 li 节点的所有直接子节点 a，
二者组合在一起即获取所有 li 节点的所有直接 a 子节点。
'''

'''
2.  / 用于选取直接子节点，如果要获取所有子孙节点，就可以使用 //。例如，要获取 ul 节点下的所有子孙 a 节点，可以这样实现：
'''
print('\n\ntest 222222222222')
result = html.xpath('//ul//a')
print(result)
'''
打印结果为：
[<Element a at 0x1c89cdb8100>, <Element a at 0x1c89cdb8140>, <Element a at 0x1c89cdb8180>, <Element a at 0x1c89cdb81c0>,
<Element a at 0x1c89cdb8200>]
'''

'''
3. 但是如果这里用 //ul/a，就无法获取任何结果了。因为 / 用于获取直接子节点，而在 ul 节点下没有直接的 a 子节点，
只有 li 节点，所以无法获取任何匹配结果，代码如下：
'''
print('\n\ntest 33333333333')
result = html.xpath('//ul/a')
print(result)
'''
打印结果为：
[]
'''
