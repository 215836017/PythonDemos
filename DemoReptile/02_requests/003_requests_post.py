import requests

'''
HTTP中另一种常见的请求方式为post。
'''

'''
1. 使用requests实现post请求也非常简单。
'''
print('test 111111111')
data = {
    'name': "liSi",
    'age': 22
}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
'''
打印结果为：
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "age": "22", 
    "name": "liSi"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "16", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.23.0", 
    "X-Amzn-Trace-Id": "Root=1-5edc411f-f6c7fa68006e9ca84ac6a73c"
  }, 
  "json": null, 
  "origin": "125.118.133.104", 
  "url": "http://httpbin.org/post"
}
可以发现: form部分就是提交的数据
'''