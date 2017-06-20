#字典示例
#一个简单的数据库
#字典使用人名作为键值。每个人用另一个字典来表示，其键'phone'和'addr'分别表示他们的电话号码和地址
people={
    'Alice':{
        'phone':'2341',
        'addr':'Fpp driver 23'
    },

    'Beth':{
        'phone':'9102',
        'addr':'Bar street 42'
    },

    'Cecil':{
        'phone':"3158",
        'addr':'Baz avenue 90'
    }
}

#针对电话号码的地址使用的描述性标签，会在打印输出的时候用到
lable={
    'phone':'phone number',
    'addr':'address'
}

name=input('Name: ')
#查找电话号码还是地址?
request=input('Phone number(p) or address(a)?')
#使用正确的键值
if request=='p':
    key='phone'
if request=='a':
    key='addr'
#如果名字是字典中的有效键值才打印信息
if name in people:
    print("%s's %s is %s."%(name,lable[key],people[name][key]))