import requests
import re

'''
HTTP中最常见请求之一的就是GET请求，现在来学习一些利用requests构建GET请求
'''

'''
测试请求的网站工具：http://httpbin.org
'''

'''
1. 最简单的请求
'''
print("test  11111111111111")
# r = requests.get('http://httpbin.org/get')
# print(r.text)
'''
打印结果为：
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.23.0", 
    "X-Amzn-Trace-Id": "Root=1-5edc325c-8e0e88186f5788af6523d172"
  }, 
  "origin": "125.118.133.104", 
  "url": "http://httpbin.org/get"
}
'''

'''
2. 在GET中添加参数
'''
print('\ntest 222222222')
# r = requests.get('http://httpbin.org/get?name=zhangSan&age=22')
# print(r.text)
'''
打印结果为：
{
  "args": {
    "age": "22", 
    "name": "zhangSan"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.23.0", 
    "X-Amzn-Trace-Id": "Root=1-5edc32fc-5b7be5ccb409ee0897d94dbb"
  }, 
  "origin": "125.118.133.104", 
  "url": "http://httpbin.org/get?name=zhangSan&age=22"
}
'''

'''
更加方便地设置参数的方式如下：
'''
print('\ntest 222222 ---- 222222222')
data = {
    'name': 'zhangSan',
    'age': 22
}
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)
'''
打印结果同2中相同
'''

'''
3. 上面返回的结果是JSON格式的字符串，如果想直接解析结果从而得到一个字典格式的话，可以直接调用json()方法
'''
print('\ntest 333333333')
# r = requests.get('http://httpbin.org/get')
# print(type(r.text))
# print(type(r.json()))
# print(r.json())
'''
打印结果为：
<class 'str'>
<class 'dict'>
{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 
'python-requests/2.23.0', 'X-Amzn-Trace-Id': 'Root=1-5edc3470-301408889966cace261993f4'}, 'origin': '125.118.133.104', 
'url': 'http://httpbin.org/get'}
'''

'''
4. 尝试网页：上面的请求返回的是JSON格式的字符串，如果请求普通网页的话，则肯定能获得相应的的内容了。 以“知乎”--“发现”页面为例
'''
print('\ntest 4444444444')
headers = {
    'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)
'''
打印结果为：
[] 
这个结果，无语了.....
'''

'''
5. 抓取二进制数据
  图片、音频、视频这些文件本质上都是二进制码组成的，由于有特定的保存格式和对应的解析方法，我们才可以看到这些形形色色的多媒体。所以，
想要抓取它们，就要拿到相应的二进制码。 下面以GitHub的站点图标为例
'''
print('\ntest 5555555555')
r = requests.get('https://github.com/favicon.ico')
print(r.text)
print(r.content)
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
'''
打印结果为乱码，这里省略显示
'''

