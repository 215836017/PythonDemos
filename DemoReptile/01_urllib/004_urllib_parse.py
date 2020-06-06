# from urllib.parse import urlparse
import urllib.parse as url_parse

'''
urllib库里面还提供了parse模块，它定义了处理URL的标准接口。例如实现URL各部分的抽取、合并以及链接转换。
它支持如下协议的URL处理：file、ftp、gopher、hdl、http、https、imap、mailto、mms、news、nntp、prospero、
rsync、trsp、trspu、sftp、sip、sips、snews、svn、svn+ssh、telnet 和 wais
'''

'''
1. urlparse()方法：
该方法可以实现URL的识别和分段。
'''
print("11111111111")
result = url_parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
'''
打印结果为：
<class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', 
params='user', query='id=5', fragment='comment')
结果中返回了ParseResult类型的对象，包含6个部分：scheme(协议)、netloc(域名)、path(访问路径)、params(参数)、
query(查询条件)和fragment()
'''

'''
2. urlunparse()方法：
urlunparse()是urlparse()方法的对立方法，它接收的参数是一个可迭代对象，但是它的长度必须是6，否则会抛出参数数量不足或过多的问题。
'''
print("\n222222222222222")
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(url_parse.urlunparse(data))
'''
打印结果为：
http://www.baidu.com/index.html;user?a=6#comment
即：实现了URL的构造
'''

'''
3. urlsplit()方法：
urlsplit()方法和urlparse()方法非常相似，只不过它不再单独解析params这一部分，只返回5个结果
'''
print('\n33333333333')
result = url_parse.urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
'''
打印结果为：
SplitResult(scheme='http', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')
返回的结果是SplitResult，它其实也是一个元组类型，既可以用属性获取，也可以索引来获取
'''

'''
4. urlunsplit()方法：
与urlunparse()方法类似，它也是讲链接各个部分组合成完整链接的方法。传入的参数也是一个可迭代对象
'''
print("\n444444")
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(url_parse.urlunsplit(data))
'''
打印结果为：
http://www.baidu.com/index.html?a=6#comment
'''

'''
5. urljoin()方法：
有了urlunparse()方法和urlunsplit()方法，可以完成链接的合并，不过前提是必须要有特定长度的对象，链接的每一部分都要清晰分开。
生成链接还有一个方法，那就是urljoin()方法。我们可以提供一个base_url(基础链接)作为第一个参数，将新的链接作为第二个参数，该方法
会分析base_url的scheme、netloc和path这3个内容并对心链接缺失部分进行补充，最后返回结果
'''
print('\n5555555555555')
print(url_parse.urljoin('http://www.baidu.com', 'FZQ.html'))
print(url_parse.urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FZQ.html'))
print(url_parse.urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FZQ.html?question=2'))
print(url_parse.urljoin('http://www.baidu.com/?wd=abc', 'https://cuiqingcai.com/index.php'))
print(url_parse.urljoin('www.baidu.com', '?category=2#comment'))
print(url_parse.urljoin('www.baidu.com#comment', '?category=2'))
'''
打印结果为：
http://www.baidu.com/FZQ.html
https://cuiqingcai.com/FZQ.html
https://cuiqingcai.com/FZQ.html?question=2
https://cuiqingcai.com/index.php
www.baidu.com?category=2#comment
www.baidu.com?category=2
可以发现：base_url提供了scheme、netloc和path这3项内容。如果这3项在新的链接中不存在，则予以补充；如果新的链接中存在，就使用
新的链接中的部分，而base_url中的params、query和fragment是不起作用的。
通过urljoin()方法，我们可以轻松实现链接的解析、合并与生成。
'''

'''
6. urlencode()方法：
urlencode()方法在构造GET请求参数的时候，可以将参数轻松地由字典类型转化为GET请求参数
'''
print('\n66666666666')
params = {
    'name': 'zhangSan',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + url_parse.urlencode(params)
print(url)
'''
打印结果为：
http://www.baidu.com?name=zhangSan&age=22
'''

'''
7. parse_qs()方法：
根urlencode()方法是相反的作用。如果我们有一串GET请求参数，利用parse_qs()方法，就可以将它转为字典
'''
print('\n77777777777')
query = 'name=zhangSan&age=22'
print(url_parse.parse_qs(query))
'''
打印结果为：
{'name': ['zhangSan'], 'age': ['22']}
'''

'''
8. parse_qsl()方法：
parse_qsl()方法可以将参数转化为元组组成的列表
'''
print('\n88888888888')
query = 'name=zhangSan&age=22'
print(url_parse.parse_qsl(query))
'''
打印结果为：
[('name', 'zhangSan'), ('age', '22')]
'''

'''
9. quote()方法：
该方法可以将内容转化为URL编码的格式。URL中带有中文参数时，有时可能会导致乱码的问题，此时用这个方法可以将中文字符转化为URL编码
'''
print('\n99999999999999')
keyword = "中文"
url = 'https://www.baidu.com/s?wd=' + url_parse.quote(keyword)
print(url)
'''
打印结果为：
https://www.baidu.com/s?wd=%E4%B8%AD%E6%96%87
'''

'''
10. unquote()方法：
unquote()方法是对quote()方法的解码
'''
print('\n10  10  10')
url = url_parse.unquote('https://www.baidu.com/s?wd=%E4%B8%AD%E6%96%87')
print(url)
'''
打印结果为：
https://www.baidu.com/s?wd=中文
'''