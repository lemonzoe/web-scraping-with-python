from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html ")
bs0bj=BeautifulSoup(html,"html.parser")
# 通过BeautifulSoup对象，
# 可以用findAll函数抽取只包含在<span class="green"></span>标签里的文字
nameList=bs0bj.findAll("span",{"class":"green"})
# bs0bj.tagName只能获取页面中的第一个指定的标签
# bsobj.(tagName,tagAttributes)可以获取页面中所有指定的标签
for name in nameList:
    print(name.get_text())
    # get_text()会把正在处理的HTML文档中所有的标签都清除，然后返回一个只包含文字的字符串
    # 通常在准备打印、存储和操作数据时，应该最后才使用.get_text()
""" 
findAll(tag,attributes,recursive,text,limit,keywords)
find(tag,attributes,recersive,text,keywords)

1、标签参数tag，可以传一个标签的名称或多个标签名称组成的python列表做标签参数
如：返回一个包含HTML文档中所有标题标签的列表
.findAll({"h1","h2","h3","h4","h5","h6"})
属性参数attributes，用一个python字典封装一个标签的若干属性和对应的属性值。
如：返回HTML文档里红色与绿色两种颜色的span标签
.findAll("span",{"class":{"green","red"}})
2、递归参数recursive是一个布尔变量，如果recursive设置为True（默认值），
findAll就会根据要求去查找标签参数的所有子标签，以及子标签的子标签。
如果recursive设置为False，findAll就只查找文档的一级标签。
3、文本参数text是用标签的文本内容去匹配，而不是用标签的属性
如：查找包含“the prince”内容的标签数量
nameList=bs0bj.findAll(text="the prince")
print(len(nameList))
4、范围限制参数limit， 只用于findAll。find等价于findAll的limit等于1时的情形。
如果只对网页中获取的前x项结果感兴趣，可以设置它。
设置这个参数所获得的前几项结果是按照网页上的顺序排序。
5、关键词参数keyword，可以选择具有指定属性的标签。
如：
allText=bs0bj.findAll(id="text")
print(allText[0].get_text())
tips: 
1)以下两行代码完全一样：
bs0bj.findAll(id="text")
bs0bj.findAll("",{"id":"text"})
2)class是python中受保护的关键字，不能当作变量或参数名使用
但可以在后面加下划线： bsobj.findAll(class_="green")
或使用引号：bs0bj.findAll("",{"class":"green"})
"""