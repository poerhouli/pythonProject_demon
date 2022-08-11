'''
    装饰器
'''
'''def outter():  #外函数
    age = 20   #外函数变量

    def inner():   #内函数
        print(age)  #内函数引用外函数变量

    return inner   #外函数返回内函数变量


f = outter()
print(type(f))
f()'''


# 增加新功能不修改功能
def verify():
    print('权限验证')


def enter():
    verify()
    print('进入后台')


def delete():
    verify()
    print('删除订单')


enter()
delete()
