import requests

'''
  发送HTTP请求后，得到的自然是响应结果。除了使用text和content获取响应的内容外，还有很多属性和方法可以用来获取其他信息，比如状态码、响应头、
Cookies等。
'''
r = requests.get('http://www.jianshu.com')
print("1111: ", type(r.status_code), r.status_code)
if r.status_code == requests.codes.ok:  # requests库中提供了一个内置的状态码查询对象 requests.codes
    print("请求成功了!")
else:
    print("请求失败了...")
print("2222: ", type(r.headers), r.headers)
print("3333: ", type(r.cookies), r.cookies)
print("4444: ", type(r.url), r.url)
print("5555: ", type(r.history), r.history)
'''
打印结果为：
1111:  <class 'int'> 403
2222:  <class 'requests.structures.CaseInsensitiveDict'> {'Server': 'Tengine', 'Date': 'Sun, 07 Jun 2020 01:27:59 GMT',
 'Content-Type': 'text/html', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 
 'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload', 'Content-Encoding': 'gzip'}
3333:  <class 'requests.cookies.RequestsCookieJar'> <RequestsCookieJar[]>
4444:  <class 'str'> https://www.jianshu.com/
5555:  <class 'list'> [<Response [301]>]
'''