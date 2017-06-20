#5、items
#item方法将字典所有的项以列表方式返回，返回时没有特定的次序
# 3.x 里面，iteritems()和viewitems()这两个方法都已经废除了，而items()得到的结果是和2.x里面viewitems()一致的。在3.x里用items()替换iteritems()，可以用于for来循环遍历。
d={'title':'ppp','name':'ccc'}
print(d.items())

#6、keys()将字典中的键以列表形式返回
print(d.keys())

#7、pop方法用来获得对应于给定键的值，然后将这个键值对从字典中移除
d1={'aasd':"sadad",'asdasd':"sadsadad"}
print(d1.pop('aasd'))
print(d1)

#8、popitem
#popitem方法类似于list.pop,后者弹出列表最后一个元素。但不同的是，popitem弹出随机的项，因为字典中没有最后的元素，该方法适合一个接一个旳移除并且处理项(不用首先获取键的列表，所以很高效)
d2={'a':'b',"c":'d'}
print(d2.popitem())
print(d2)

#9、setdefault
#setdefault在某种程度上类似于get，可以获得与给定键相关的值，setdefault还能在字典中不含给定键的情况下设定相应的键值,如果键值存在，不会修改原来的键值
d3={}
d3.setdefault('name','None')
print(d3)
d3['name']='CY'
print(d3.setdefault('name','None'))

#10、update
#update方法可以利用一个字典更新另一个字典,如果键值存在则直接覆盖，如果不存在则会添加
d={'title':'sasdadadad',"url":"asdasdadsad","change":'asdasdada'}
a={'title':"a"}
d.update(a)
print(d)

#11、values,用于返回当前字典中的值
d={}
d[1]=1
d[2]=2
print(d.values())