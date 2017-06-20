#使用get方法实现电话本的功能
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

lable={
    'phone':'phone number',
    'addr':'address'
}

name=input('Name: ')

request=input('Phone number(p) or address(a)?')

if request=='p':
    key='phone'
if request=='a':
    key='addr'

person=people.get(name,{})
lable=lable.get(key,key)
result=person.get(key,'not available')
print("%s's %s is %s."%(name,lable,result))
