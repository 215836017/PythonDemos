import urllib.request as req
import urllib.error as error

'''
URLError
URLError类来自urllib的error模块，它集成自OSError类。是error异常模块的基类， 由request模块产生的异常都可以
通过捕获这个类来处理。 它有一个属性reason，即返回错误的原因
'''

# try:
#     req.urlopen('https://abcdefghj.com/index.html')
# except error.URLError as e:
#     print(e.reason)

'''
HTTPError
HTTPError是URLError的子类，专门用来吃力HTTP请求错误，比如认证请求失败等。它有如下3个属性：
code：返回HTTP状态码，比如404,500等
reason: 同父类一样，用于返回错误的原因
headers：返回请求头
'''

# try:
#     req.urlopen('https://abcdefghj.com/index.html')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')

'''
因为URLError是HTTPError的父类，所以可以先选择捕获子类的错误， 再去捕获父类的错误，所以更好的写法如下：
'''
try:
    req.urlopen('https://abcdefghj.com/index.html')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
