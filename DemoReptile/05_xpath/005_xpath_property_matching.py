from lxml import etree

'''
1. 在选取的时候，我们还可以用 @ 符号进行属性过滤。比如，这里如果要选取 class 为 item-0 的 li 节点，可以这样实现:
'''
print('test 1111111')
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)
'''
打印结果为：
[<Element li at 0x26430337380>, <Element li at 0x264303373c0>]
'''
'''
这里我们通过加入 [@class="item-0"]，限制了节点的 class 属性为 item-0，而 HTML 文本中符合条件的 li 节点有两个，所以结果应该返回两个
匹配到的元素。
'''