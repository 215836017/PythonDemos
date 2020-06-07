print("学习正则表达式")

'''
  正则表达式是处理字符串的强大工具，它有自己特定的语法结构，有了它，实现字符串的检索、替换、匹配验证都非常简单
'''

'''
 中国提供的正则表达式测试工具 http://tool.oschina.net/regex/  
 打开这个网页，输入待匹配的文本，然后选择常用的正则表达式，就可以得到相应的匹配结果了。
'''

'''
正则表达式常用的匹配规则：
\w  匹配字母、数字及下划线
\W	匹配不是字母、数字及下划线的字符
\s	匹配任意空白字符，等价于[\t\n\r\f]
\S	匹配任意非空字符
\d	匹配任意数字，等价于[0-9]
\D	匹配任意非数字的字符
\A	匹配字符串开头
\Z	匹配字符串结尾，如果存在换行，只匹配到换行前的结束字符串
\z	匹配字符串结尾，如果存在换行，同时还会匹配换行符
\G	匹配最后匹配完成的位置
\n	匹配一个换行符
\t	匹配一个制表符
^	匹配一行字符串的开头
$	匹配一行字符串的结尾
.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
[...]	用来表示一组字符，单独列出，比如[amk]匹配a、m或k
[^...]	不在[]中的字符，比如[^abc]匹配除了a、b、c之外的字符
*	匹配0个或多个表达式
+	匹配1个或多个表达式
?	匹配0个或1个前面的正则表达式定义的片段，非贪婪方式
{n}	精确匹配n个前面的表达式
{n, m}	匹配n到m次由前面正则表达式定义的片段，贪婪方式
a|b	匹配a或b
()	匹配括号内的表达式，也表示一个组
'''

'''
常用正则表达式

汉字	        ^[\u4e00-\u9fa5]{0,}$
空白行	    \n\s*\r
邮箱地址	    /.+@.+\.[a-z]+/
手机号	    ^1(3|4|5|6|7|8|9)\d{9}$
中国邮政编码	[1-9]\d{5}(?!\d)
18位身份证号	^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$
通用时间  	(20\d{2}([.-/|年月\s]{1,3}\d{1,2}){2}日?(\s?\d{2}:\d{2}(:\d{2})?)?)|(\d{1,2}\s?(分钟|小时|天)前)
整数	        ^-?[1-9]\d*$
域名	        ^((http://)|(https://))?(a-zA-Z0-9?.)+[a-zA-Z]{2,6}(/)
IP	        ((?😦?:25[0-5]|2[0-4]\d|[01]?\d?\d).){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))
HH:mm:ss	([0-1][0-9]|2[0-3])😦[0-5][0-9])😦[0-5][0-9])
'''