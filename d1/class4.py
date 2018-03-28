"""
# 处理子标签
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen(" http://www.pythonscraping.com/pages/page3.html")
bs0bj=BeautifulSoup(html,"html.parser")
for child in bs0bj.find("table",{"id":"giftList"}).children:
    # giftList中的L变成小写 
    # 则会发生AttributeErrror:'NoneType' object has no attribute 'children'
    print(child)
# 如果用descendants( )，函数而不是children( )函数
# 那么会有二十几个标签打印出来，包括img标签，span标签，以及每个td标签。

# 处理兄弟标签
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen(" http://www.pythonscraping.com/pages/page3.html")
bs0bj=BeautifulSoup(html,"html.parser")
for sibling in bs0bj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
# next_siblings()函数可以让收集表格数据成为简单的事情，尤其是带标题行的表格
# 标题行被跳过了。对象不能把自己作为兄弟标签，这个函数值调用后面的兄弟标签。
# next_siblings和previous_siblings返回一组标签。
# next_sibling和previous_sibling返回单个标签。
"""

# 处理父标签
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen(" http://www.pythonscraping.com/pages/page3.html")
bs0bj=BeautifulSoup(html,"html.parser")
print(bs0bj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())