import requests

'''
  requests可以模拟提交一些数据。假如有的网站需要上传文件，也可以用requests库来实现
'''
files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)
'''
打印结果为：
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "data:application/octet-stream;base64,AAAB...AAA="
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "6665", 
    "Content-Type": "multipart/form-data; boundary=04ccd5a36a8f5ecf84359a0756df13c9", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.23.0", 
    "X-Amzn-Trace-Id": "Root=1-5edc4677-a26e03e8803389d8a44d8ea0"
  }, 
  "json": null, 
  "origin": "125.118.133.104", 
  "url": "http://httpbin.org/post"
}
'''