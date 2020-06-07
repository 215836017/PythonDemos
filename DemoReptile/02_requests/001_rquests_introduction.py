import requests

'''
1. 通过学习urllib库的基本用法，了解到其中确实有不方便的地方，比如处理网页验证和Cookies时，需要写Opener和Handler来处理。为了更加方便
地实现这些操作，就有了更加强大的库requests。有了它，Cookies、登录验证、代理设置等操作都变的非常简单了
'''

'''
2. 在使用requests库时，需要先安装这个库，可以使用pip进行安装，也可以Anaconda进行安装
'''

'''
3. 初步体验
  urllib中的urlopen()方法实际上是GET请求，而requests中相应的方法就是get()方法，是不是感觉更加明确一些。
'''
r = requests.get('http://www.baidu.com')
print('111: ', type(r))
print('\n222: ', r.status_code)
print('\n333: ', type(r.text))
print('\n444: ', r.text)
print('\n555: ', r.cookies)
'''
打印结果为：
111:  <class 'requests.models.Response'>

222:  200

333:  <class 'str'>

444:  <!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta 
http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet 
type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css><title>ç¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é</title>
</head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> 
<div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> 
</div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> 
<input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> 
<input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr">
<input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span><span class="bg s_btn_wr">
<input type=submit id=su value=ç¾åº¦ä¸ä¸ class="bg s_btn"></span> </form> </div> </div> <div id=u1> 
<a href=http://news.baidu.com name=tj_trnews class=mnav>æ°é»</a> <a href=http://www.hao123.com name=tj_trhao123 
class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>å°å¾</a> <a href=http://v.baidu.com 
name=tj_trvideo class=mnav>è§é¢</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>è´´å§</a> <noscript> 
<a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 
name=tj_login class=lb>ç»å½</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?
login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+
 '" name="tj_login" class="lb">ç»å½</a>');</script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri 
 style="display: block;">æ´å¤äº§å</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> 
 <a href=http://home.baidu.com>å³äºç¾åº¦</a> <a href=http://ir.baidu.com>About Baidu</a> </p> 
 <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>ä½¿ç¨ç¾åº¦åå¿è¯»</a>&nbsp; 
 <a href=http://jianyi.baidu.com/ class=cp-feedback>æè§åé¦</a>&nbsp;äº¬ICPè¯030173å·&nbsp; <img 
 src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>

555:  <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>

Process finished with exit code 0

'''