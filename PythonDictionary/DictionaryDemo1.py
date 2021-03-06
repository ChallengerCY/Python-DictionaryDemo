#字典
#字典是Python中唯一内建的映射类型。字典中没有特殊的顺序，但都是存储在一个特定的键(key)下面，键可以是数字，字符串，甚至是元组

#一、字典的使用
#在某些情况下，字典比列表更加适用:
#1、表示一个游戏棋盘的状态，每个键都是由坐标值组成的元组
#2、存储文件修改时间，用文件名作为键;
#3、数字电话\地址薄

#1、使用列表创建一个电话本,(这里用字符串表示电话号码，以0开头的数字回会被编译成8进制数字)
name=["A","B","C","D"]
phone=["2341","9102","3158","0142","5551"]
print(phone[name.index("B")])
#这样做可以，但是不实用

#二、创建和使用字典
#创建一个字典,字典由多个键与其对应的值构建成的键-值对组成，中间由冒号隔开，项之间用逗号隔开，字典由大括号括起来。空字典由{}组成
#字典中的键是唯一的，而值不唯一
phonebook={"Alice":"2431",'Beth':'9102','Cecil':'3258'}

#1、dict函数，可以使用dict函数，通过其他映射(比如其他字典)或者(键，值)对的序列建立字典
items=[('name','Gumby'),('age',42)]
d=dict(items)
print(d)
print(d['name'])

#dict函数也可以通过关键字参数来创建字典
a=dict(name="CY",num=42)
print(a['name'])

#2、基本字典的操作
#大部分操作与序列相似

#返回字典中键值对的数量
print(len(a))


