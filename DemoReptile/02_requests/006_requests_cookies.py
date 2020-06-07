import requests

'''
使用urllib处理Cooki时写法比较复杂，而使用requests后，获取和设置Cookies只需要一步即可完成
'''

'''
1. 获取Cookies的过程：
'''
print('test 11111111111')
r = requests.get("https://www.baidu.com")
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)

'''
打印结果为：
<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
BDORZ=27315
'''

'''
2. 第一种方法：获取相应的Cookie，将其设置到Headers里面
   第二种方法：构造RequestsCookieJar对象
'''