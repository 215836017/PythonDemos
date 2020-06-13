from lxml import etree

'''
1. 一般会用 // 开头的XPath规则来选取所有符合要求的节点。示例如下：
'''
print('test 1111111')
html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//*')
print(result, '\n\n')
for item in result:
    print(item)
'''
打印结果：
[<Element html at 0x26ad3f87200>, <Element body at 0x26ad3f872c0>, <Element div at 0x26ad3f87300>, 
<Element ul at 0x26ad3f87340>, <Element li at 0x26ad3f87380>, <Element a at 0x26ad3f87400>, <Element li at 0x26ad3f87440>,
<Element a at 0x26ad3f87480>, <Element li at 0x26ad3f874c0>, <Element a at 0x26ad3f873c0>, <Element li at 0x26ad3f87500>,
<Element a at 0x26ad3f87540>, <Element li at 0x26ad3f87580>, <Element a at 0x26ad3f875c0>] 


<Element html at 0x26ad3f87200>
<Element body at 0x26ad3f872c0>
<Element div at 0x26ad3f87300>
<Element ul at 0x26ad3f87340>
<Element li at 0x26ad3f87380>
<Element a at 0x26ad3f87400>
<Element li at 0x26ad3f87440>
<Element a at 0x26ad3f87480>
<Element li at 0x26ad3f874c0>
<Element a at 0x26ad3f873c0>
<Element li at 0x26ad3f87500>
<Element a at 0x26ad3f87540>
<Element li at 0x26ad3f87580>
<Element a at 0x26ad3f875c0>
'''

'''
这里使用 * 代表匹配所有节点，也就是整个 HTML 文本中的所有节点都会被获取。可以看到，返回形式是一个列表，每个元素是 Element 类型，其后跟了
节点的名称，如 html、body、div、ul、li、a 等，所有节点都包含在列表中了。
'''

'''
2. 当然，此处匹配也可以指定节点名称。如果想获取所有 li 节点，示例如下：
'''
print('\n\ntest 2222222222222')
result = html.xpath('//li')
print(result)
'''
打印结果为：
[<Element li at 0x24e63767140>, <Element li at 0x24e637678c0>, <Element li at 0x24e63767900>, <Element li at 0x24e63767940>, 
<Element li at 0x24e63767980>]
'''
