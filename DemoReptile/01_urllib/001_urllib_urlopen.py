import urllib.request as request
import urllib.parse as parse

'''
最基础的HTTP库有：urllib， httplib2， requests， treq等 
'''

response = request.urlopen('https://www.python.org/')

print('test 111 : ', response)
# print('test 222 : ', response.read().decode('utf-8'))  # 结果跟网页源代码是一样的

print('test 333 : ', type(response))
# test 333 :  <class 'http.client.HTTPResponse'>  --- 说明了urllib是一个Python内置的Http相关库

print('test 444: ', response.status)
print('test 555: ', response.getheaders())
print('\ntest 666: ', response.getheader('Server'))
print('test 666: ', response.getheader('Connection'))
print('test 666: ', response.getheader('Content-Type'))
print('test 666: ', response.getheader('Date'))
print('test 666: ', response.getheader('Vary'))

'''
urllib.request 模块提供了最基本的构造Http请求的方法，利用它可以模拟浏览器的一个请求发起过程。
同时它还带有处理授权验证、重定向、浏览器Cookies以及其他内容。
'''

'''
urlopen的其他参数：
urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            *, cafile=None, capath=None, cadefault=False, context=None)
data: 1. 要传递该参数，需要使用byte()方法将参数转化为字节。
      2. 如果传递了该参数，那么请求方式就不再是Get方式，而是Post方式。
timeout: 超时时间，单位为妙
context: 必须是ssl.SSLContext类型，用来指定SSL设置
cafile: CA证书
capath: CA证书的路径
cadefault: 已经弃用
'''
data = bytes(parse.urlencode({'Python': "Hello"}), encoding='utf-8')
response = request.urlopen('http://httpbin.org/post', data)
# response = request.urlopen('http://httpbin.org/post', data, timeout=0.1)  # 需要用try except
print('\n\ntest 777 :', response.read())
