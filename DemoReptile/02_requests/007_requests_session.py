import requests

'''
session可以方便地维持一个会话，而且不用担心cookies的问题，它会帮助我们自动处理好。
'''
s = requests.Session()
s.get('http://www.httpbin.org/cookies/set/number/123456789')
r = s.get('http://www.httpbin.org/cookies')
print(r.text)
'''
打印结果为：
{
  "cookies": {
    "number": "123456789"
  }
}
'''