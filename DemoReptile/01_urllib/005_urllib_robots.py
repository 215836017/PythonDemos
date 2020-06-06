import urllib.robotparser as robotparser

'''
利用urllib中的robotparser模块，可以实现网站Robots协议的分析
'''

'''
1. Robots协议：
  Robots协议也称作为爬虫协议、机器人协议，它的全名叫作网络爬虫排除标准，用来告诉爬虫和所搜引擎哪些页面可以抓取，哪些页面
不可以抓取。它通常是一个叫作robots.txt的文件，一般放在网站的根目录下。
  当搜索爬虫访问一个站点时，它首先会检查这个站点根目录下是否存在robots.txt文件，如果存在，搜索爬虫会根据其中定义的爬取范围来爬取；
如果没有找到这个文件，搜索爬虫便会访问所有可以直接访问的页面。
  如下是一个tobots.txt的样例：
  User-agent: *
  Disallow: /
  Allow: /public/
  这实现了对所有爬虫只允许爬取public目录的功能。
详细说明：
User-agent描述了搜索爬虫的名称，*表示该协议对任何爬虫有效。如果设置为： User-agent： Baiduspider，则只对百度的爬虫是有效的。
Disallow 指定了不允许抓取的目录，比如上面例子中设置为/ 则表示不允许抓取所有页面
Allow 一般和Disallow一起使用，一般不会单独使用，用来排除某些限制。现在我们设置为/public/，则表示所有页面不允许抓取，但可以抓取public目录
'''

'''
2. 爬虫名称
爬虫名是哪里来的呢？为什么就叫这个？其实它是有固定名字的，以下是一些常见的搜索爬虫的名称及对应的网站
  爬虫名称                          名  称                       网  站
BaiduSpider                        百度                      www.baidu.com
Googlebot                          谷歌                      www.google.com
360Spider                          360搜索                   www.so.com
YodaoBot                           有道                      www.youdao.com
ia_archiver                        Alexa                    www.alexa.cn
Scooter                            altavista                www.altavista.com
'''

'''
3. robotparser
  了解了Robots协议之后，就可以使用robotparser模块来解析robots.txt了。该模块提供了一个RoboFileParser,它可以根据某网站的robots.txt
文件来判断一个爬虫是否有权限来爬取这个网页。
  该类使用非常简单，只要在构造方法中传入robots.txt的链接即可。当然也可以在声明时不传入参数，再使用set_url()方法设置即可。
  常用的方法有：
  set_url(): 设置robots.txt文件的链接
  read(): 读取robots.txt文件并进行解析
  parse(): 用来解析robots.txt文件，传入的参数是robots.txt某些行的内容，它会按照robots.txt的语法规则来分析这些内容
  can_fetch(): 传入的第一个参数时User-agent，第二个是要抓取的URL。返回的是该搜索引擎是否可以抓取这个URL，返回结果为True或False
  mtime(): 上次抓取和分析robots.txt的时间。这对于长时间分析和抓取的搜索爬虫是很有必要的。可能需要定期检查来抓取最新的robots.txt
  modified(): 将当前时间设置为上次抓取和分析robots.txt的时间
'''
# rp = robotparser.RobotFileParser("http://www.jianshu.com/rotots.txt")
rp = robotparser.RobotFileParser()
rp.set_url("http://www.jianshu.com/rotots.txt")
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'http://www.jianshu.com/serch?q=python&page=1&type=collections'))
'''
打印结果为：
False
False
'''