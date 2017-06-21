#字典的格式化字符串
#在每个转换说明符的后面，可以加上键(用括号括起来)，后面再加上说明元素
phonebook={'Beth':'9102','Alice':'1111','tom':'1551'}
print("tom's phoneNum is %s" % phonebook["tom"])
print("tom's phoneNum is %(tom)s" % phonebook)

#除了增加的字符串键外，转换说明符还是像以前一样工作。，当以这种方式使用字典的时候，只要所有给出的键都能在字典中找到，就可以使用任意数量的转换说明符。
#这类字符串格式化在模板系统中非常有用
template="""<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>
"""

data={"title":"My Home Page","text":"Welcome to my home page!"}
print(template % data)
