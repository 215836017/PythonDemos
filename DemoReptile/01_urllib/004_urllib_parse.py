# from urllib.parse import urlparse
import urllib.parse as url_parse

'''
urllib库里面还提供了parse模块，它定义了处理URL的标准接口。例如实现URL各部分的抽取、合并以及链接转换。
它支持如下协议的URL处理：file、ftp、gopher、hdl、http、https、imap、mailto、mms、news、nntp、prospero、
rsync、trsp、trspu、sftp、sip、sips、snews、svn、svn+ssh、telnet 和 wais
'''

'''
urlparse()方法：
该方法可以实现URL的识别和分段。
'''
result = url_parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

'''
urlunparse()方法：

'''

'''
urlsplit()方法：

'''

'''
urlunsplit()方法：
'''

'''
urljoin()方法：

'''

'''
urlecode()方法：
'''

'''
parse_qs()方法：
'''

'''
parse_qsl()方法：
'''

'''
quote()方法：

'''

'''
unquote()方法：
'''
