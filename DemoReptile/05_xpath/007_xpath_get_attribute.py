from lxml import etree

'''
1. 用XPath 中的 text 方法可以获取节点中的文本，那么节点属性该怎样获取呢？其实还是使用@符号就可以
'''
print("test 111111111111")
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)
'''
打印结果为：
['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
'''
'''
这里我们通过 @href 即可获取节点的 href 属性。注意，此处和属性匹配的方法不同：
属性匹配是中括号加属性名和值来限定某个属性，如 [@href="link1.html"]；
而此处的 @href 指的是获取节点的某个属性，二者需要做好区分。
'''
