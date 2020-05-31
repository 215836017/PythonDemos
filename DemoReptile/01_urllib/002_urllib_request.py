import urllib.request as req
import urllib.parse as parse

'''
urlopen()方法可以实现最基本的请求，但是这几个简单的参数不能满足构建一个完整的请求。
如果请求中需要加入Headers等信息，就需要用到Request类来构建
'''
request = req.Request('https://www.python.org/')
response = req.urlopen(request)

print('test 111: ', response.read())

'''
Request的构造方法
def __init__(self, url, data=None, headers={},
                 origin_req_host=None, unverifiable=False,
                 method=None)
url: 必要的参数，请求的url
data: 如果要传递，则必须是bytes类型的。如果是字典，可以先用urllib.parse模块里面的
      urlencode()编码
headers: 请求头， 是一个字典。可以在构造请求时通过headers参数直接生成，也可以通过
         调用请求实例的add_header()方法添加
         请求头最常用的方法就是通过修改User-Agent来伪装浏览器，默认的User-Agent是
         Python-urllib。比如要伪装火狐浏览器，可以设置为：
         Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11   
origin_req_host: 请求放的host或IP
: 表示这个请求是否是无法验证的，默认false。意识就是说用户没有足够权限来选择接收这个请求
的结果。比如：我们请求一个HTML文档中的图片，但是我们没有自动抓取图像的权限，这时unverifiable就是true
method: 是一个字符串，表示请求的类型: GET, POST, PUT                             
'''

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': "xiaoMing"
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
request = req.Request(url=url, data=data, headers=headers, method='POST')
response = req.urlopen(request)
print('test 222: ', response.read().decode('utf-8'))

'''
对于一些更高级的操作(比如Cookies处理、代理设置等)，就需要更加强大的工具类Handler了。简而言之，我们可以把它理解为各种
处理器。有专门处理登录验证的，有处理Cookies的，有处理代码设置的。利用这些Handler，我们几乎可以做到HTTP请求中的所有事情。
'''

'''
urllib.request模块里的BaseHandler类，它是所有Handler的父类。它提供了最基本的方法，例如：default_open(), protocol_request()等
'''

'''
常用的Handler类有如下几种：
HTTPDefaultErrorHandler：用于处理HTTP响应错误，错误都会抛出HTTPError类型的异常
HTTPRedirectHandler：用户处理重定向
HTTPCookiesProcessor：用户设置代理，默认代理为空
HTTPPasswordMgr：用于管理密码，它维护了用户名和密码的表
HTTPBasicAuthHandler：用户管理认证，如果一个链接打开时需要认证，那么可以用它来解决认证问题
'''

'''
另一个重要的类就是OpenerDirector，也称为Opener。 
如果要用到Handler实现更高级的功能，进行深入一层的配置，就需要用到Opener。也就是说：利用Handler来构建Opener
'''