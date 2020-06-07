import requests

'''
  requests提供了证书验证的功能。当发送HTTP请求的时候，它会检查SSL证书，我们可以使用verify参数控制是否检查此证书。
如果不加verify参数的话，默认是True，会自动验证
'''

r = requests.get('https://www.12306.cn')
print(r.status_code)
'''
打印结果为：
200
'''

'''
  如果提示一个错误：requests.exception.SSLError, 表示证书验证错误。所以，如果请求一个HTTP站点，但是证书验证错误的页面时，就会报这样的错误。
那么该如何报这样的错误呢？很简单，把verify设置为False即可
'''
r = requests.get('https://www.12306.cn', verify=False)
print(r.status_code)
'''
D:\Anaconda3\envs\lib\site-packages\urllib3\connectionpool.py:997: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.12306.cn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
D:\Anaconda3\envs\lib\site-packages\urllib3\connectionpool.py:997: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.12306.cn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
200

发现：虽然返回了200， 但是也报了一个警告，它建议我们给它指定证书。
'''
