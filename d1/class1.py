from urllib.request import urlopen
# 导入urlopen，调用html.read()获取网页的HTML内容
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/page1.html")
"""
这行代码主要可能会发生两种异常：
1、网页在服务器上不存在（或者获取页面的时候出现错误）
返回HTTP错误，可能是“404 page not found”“500 internal server error”
可以用try语句处理异常：
"""
try:
    html=urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # 返回空值，中断程序，或执行另一个方案
else:
    # 程序继续。如果已经在上面异常捕捉那一段代码里返回或中断（break），就不需要用else
"""2、服务器不存在（链接打不开或者URL链接写错）
返回一个None对象，与null类似，可增加一个判断语句检测返回的html是不是none
"""
if html is None:
    print("URL is not found")
else:
    # 程序继续
bs0bj=BeautifulSoup(html.read(),"html.parser")
# 需要添加解析器类型 否则会有warning
print(bs0bj.h1)
"""
从对象里提取h1标签,下面函数调用都可以产生同样的效果：
bs0bj.html.body.h1
bs0bj.body.h1
bs0bj.html.h1
"""