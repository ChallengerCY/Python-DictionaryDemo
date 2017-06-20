#2、copy方法返回一个具有相同键值对的新字典(这个方法实现的是浅复制，因为值本身是相同的，而不是副本),使用copy复制过来的字典，如果替换值时不受影响，如果修改(增，删)值，原始字典也会改变

x={'username':'admin','machines':['foo','bar','baz']}
y=x.copy()
y['username']='mlh'
y['machines'].remove('bar')
print(y)
print(x)

#避免上述问题，可以使用深复制 deepcopy函数
from copy import deepcopy
d={}
d['name']=['Alfred','Bertrand']
c=d.copy()
dc=deepcopy(d)
d['name'].append('Clive')
print(c)
print(dc)

#3、fromkeys方法使用给定的键建立新的字典，每个键都对应一个None
print({}.fromkeys(['name','age']))
#以上方法使用空字典，建立另一个字典有些多余，可以直接使用dict方法
print(dict.fromkeys(['name','age']))
#也可以指定默认值
print(dict.fromkeys(['name','age'],'(unknown)'))

#4、get方法是很宽松的访问字典的方法，不使用get，访问字典中不存在的项会出错,会返回none
d={}
print(d.get('name'))
#还可以自定义"默认值"
print(d.get('name',"N/A"))
#如果键存在，get使用方法和普通字典查询一样
d['name']='CY'
print(d.get('name'))