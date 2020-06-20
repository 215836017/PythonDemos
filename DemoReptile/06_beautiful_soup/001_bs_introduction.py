from bs4 import BeautifulSoup

print('学习 Python 的一个HTML或XML的解析库：BeautifulSoup ')
'''
 1. 使用场景： 在使用正则表达式的时候，一旦正则表达式写的有问题，得到的可能就不是我们想要的结果了。而且对于一个网页来说，都有一定的特殊结构
和层级关系，而且很多节点都有 id 或 class 来作区分，所以借助它们的结构和属性来提取不也可以吗？
    现在就来学习一个强大的解析工具 Beautiful Soup，它借助网页的结构和属性等特性来解析网页。有了它，我们不用再去写一些复杂的
正则表达式，只需要简单的几条语句，就可以完成网页中某个元素的提取。
'''

'''
2. Beautiful Soup 简介: 
    简单来说，BeautifulSoup 就是 Python 的一个HTML或XML的解析库，我们可以用它来方便地从网页中提取数据，官方的解释如下：
    BeautifulSoup 提供一些简单的、Python 式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要
抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。 BeautifulSoup 自动将输入文档转换为 Unicode 编码，输出文档
转换为 utf-8 编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时你仅仅需要说明一下原始编码方式就可以了。 BeautifulSoup 
已成为和 lxml、html5lib 一样出色的 Python 解释器，为用户灵活地提供不同的解析策略或强劲的速度。

所以说，利用它可以省去很多烦琐的提取工作，提高了解析效率。
'''

'''
3. 解析器：Beautiful Soup 在解析时实际上依赖解析器，它除了支持Python标准库中的HTML解析器外，还支持一些第三方解析器（比如 lxml）。
下面列出了 Beautiful Soup 支持的解析器。
解析器	                使用方法	                              优势	                                                  劣势
Python标准库	      BeautifulSoup(markup, "html.parser")	  Python 的内置标准库、执行速度适中 、文档容错能力强	        Python 2.7.3 or 3.2.2前的版本中文容错能力差
LXML HTML解析器	  BeautifulSoup(markup, "lxml")	          速度快、文档容错能力强	                                    需要安装 C 语言库
LXML XML解析器	  BeautifulSoup(markup, "xml")	          速度快、唯一支持 XML 的解析器	                            需要安装 C 语言库
html5lib	      BeautifulSoup(markup, "html5lib")	      最好的容错性、以浏览器的方式解析文档、生成 HTML5 格式的文档	速度慢、不依赖外部扩展
'''

'''
4. 先用实例看看Beautiful Soup 的基本用法
'''
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)
'''
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title" name="dromouse">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    <!-- Elsie -->
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ;
and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
The Dormouse's story

'''
'''
    这里首先声明变量 html，它是一个 HTML 字符串。但是需要注意的是，它并不是一个完整的 HTML 字符串，因为 body 和 html 节点都没有闭合。
接着，我们将它当作第一个参数传给 BeautifulSoup 对象，该对象的第二个参数为解析器的类型（这里使用 lxml），此时就完成了 BeaufulSoup 
对象的初始化。然后，将这个对象赋值给 soup 变量。
    接下来，就可以调用 soup 的各个方法和属性解析这串 HTML 代码了。
    1.调用 prettify() 方法。这个方法可以把要解析的字符串以标准的缩进格式输出。这里需要注意的是，输出结果里面包含body和html节点，
也就是说对于不标准的 HTML 字符串 BeautifulSoup，可以自动更正格式。这一步不是由 prettify() 方法做的，而是在初始化 BeautifulSoup 时就完成了。
    2.调用 soup.title.string，这实际上是输出 HTML 中 title 节点的文本内容。所以，soup.title 可以选出 HTML 中的 title 节点，
再调用 string 属性就可以得到里面的文本了，所以我们可以通过简单调用几个属性完成文本提取。
'''
