from lxml import etree

'''
1.  节点轴选择:
XPath 提供了很多节点轴选择方法，包括获取子元素、兄弟元素、父元素、祖先元素等
'''
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)
'''
打印结果为：
[<Element html at 0x1ae832a3fc8>, <Element body at 0x1ae83414308>, <Element div at 0x1ae83414348>, <Element ul at 0x1ae83414388>]
[<Element div at 0x1ae83414348>]
['item-0']
[<Element a at 0x1ae83414308>]
[<Element span at 0x1ae83414348>]
[<Element a at 0x1ae83414388>]
[<Element li at 0x1ae834145c8>, <Element li at 0x1ae834144c8>, <Element li at 0x1ae83414288>, <Element li at 0x1ae834143c8>]
'''

'''
第一次选择时，我们调用了 ancestor 轴，可以获取所有祖先节点。其后需要跟两个冒号，然后是节点的选择器，这里我们直接使用 *，
表示匹配所有节点，因此返回结果是第一个 li 节点的所有祖先节点，包括 html、body、div 和 ul。

第二次选择时，我们又加了限定条件，这次在冒号后面加了 div，这样得到的结果就只有 div 这个祖先节点了。

第三次选择时，我们调用了 attribute 轴，可以获取所有属性值，其后跟的选择器还是 *，这代表获取节点的所有属性，返回值就是 li 节点的所有属性值。

第四次选择时，我们调用了 child 轴，可以获取所有直接子节点。这里我们又加了限定条件，选取 href 属性为 link1.html 的 a 节点。

第五次选择时，我们调用了 descendant 轴，可以获取所有子孙节点。这里我们又加了限定条件获取 span 节点，所以返回的结果只包含 span 节点
而不包含 a 节点。

第六次选择时，我们调用了 following 轴，可以获取当前节点之后的所有节点。这里我们虽然使用的是 * 匹配，但又加了索引选择，所以只获取了
第二个后续节点。

第七次选择时，我们调用了 following-sibling 轴，可以获取当前节点之后的所有同级节点。这里我们使用 * 匹配，所以获取了所有后续同级节点。

以上是 XPath 轴的简单用法，更多轴的用法可以参考：http://www.w3school.com.cn/xpath/xpath_axes.asp。
'''
