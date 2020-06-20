from lxml import etree

'''
1. 属性匹配：在选取的时候，我们还可以用 @ 符号进行属性过滤。比如，这里如果要选取 class 为 item-0 的 li 节点，可以这样实现:
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

'''
2. 属性多值匹配：有时候，某些节点的某个属性可能有多个值，此时如果还想用之前的属性匹配获取，就无法匹配了，获取的结果就有可能是空的，
此时需要contains()函数
'''
print('\n\ntest 222222222222')
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)
'''
打印结果为：
['first item']
'''
'''
此种方式在某个节点的某个属性有多个值时经常用到。
'''

'''
3. 多属性匹配：另外我们可能还遇到一种情况，那就是根据多个属性确定一个节点，这是就要匹配多个属性。此时需要使用运算符and来连接
'''
print('\n\ntest 3333333333333')
text = '''  
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)
'''
打印结果为：
['first item']
'''

'''
运算符及其介绍

运算符	     描　　述	        实　　例	                返　回　值
or	           或	         age=19 or age=20	     如果 age 是 19，则返回 true。如果 age 是 21，则返回 false
and	           与	         age>19 and age<21	     如果 age 是 20，则返回 true。如果 age 是 18，则返回 false
mod	       计算除法的余数	 5 mod 2	             1
+	           加法	         6 + 4	                 10
-	           减法	         6 - 4	                 2
*	           乘法	         6 * 4	                 24
div	           除法	         8 div 4	             2
=	           等于	         age=19	                 如果 age 是 19，则返回 true。如果 age 是 20，则返回 false
!=	           不等于	     age!=19	             如果 age 是 18，则返回 true。如果 age 是 19，则返回 false
<	           小于	         age<19	                 如果 age 是 18，则返回 true。如果 age 是 19，则返回 false
<=	        小于或等于	     age<=19	             如果 age 是 19，则返回 true。如果 age 是 20，则返回 false
>	           大于	         age>19	                 如果 age 是 20，则返回 true。如果 age 是 19，则返回 false
>=	        大于或等于	     age>=19	             如果 age 是 19，则返回 true。如果 age 是 18，则返回 false
'''
