'''
    函数参数
        实际参数

'''


def fun01(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


# 位置实参：实参与形参的位置依次对应.
# fun01(1, 2, 3, 4)
# 关键字实参：实参与形参的名称  对应
# fun01(b=1, d=2, c=3, a=4)
# 序列实参：*将序列拆分后按位置与形参进行对应
#     如果参数很多，可以存储在一个序列中 通过*拆分，直接传入函数
# list01 = ['a', 'b', 'c', 'd']
# fun01(*list01)
# 字典实参：**将字典拆分后将名称与形参进行对应
di = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
fun01(**di)

'''
函数参数
    形式参数
'''

#
# def fun01(a=None, b=None, c=1, d=2):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#
#
# # 关键字实参+缺省形参：调用者可以睡衣传递参数
# fun01(1)
# def time_func(hour=0, minute=0, secound=0):
#     return hour * 3600 + minute * 60 + secound
#
#
# # 小时
# print(time_func(1))

# 位置传参：*将所有实参合并为一个元祖
# 作用：让实参个数无限制
# def fun01(*args):
#     print(args)
#
#
# fun01(12, 2, 34)


''''练习：定义函数，数值相加的函数。'''


def func02(*args):
    result = 0
    for item in args:
        result += item
    return result


print(func02(12, 3, 44))

# 关键字形参 : 在*后的参数
# def fun01(a, *args, b):
#     print(a)
#     print(args)
#     print(b)
#
#
# fun01(1, 2, 34, 5, b=2)


# def fun01(**kwargs):
#     print(kwargs)
#
#
# fun01(a=1, b=2)


# def fun07(a=0, b=0, *args, c, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#     print(kwargs)
#
#
# fun07(1, 2, 4, 5, c=3, aq=1, qa=2)

# def is_prime(number):
#     '''
#
#     :param number:
#     :return: 所有素数的列表
#     '''
#     for item in range(2, number):
#         if number % item == 0:
#             return False
#
#     return True
#
#
# def get_print(begin, end):
#     list01 = []
#     # 生成范围内的整数
#     for number in range(begin, end):
#         if is_prime(number):
#             list01.append(number)
#     return list01
#
#
# print(get_print(2, 10))
dict_commodity_info = {
    101: {'name': '屠龙刀', 'price': 10000},
    102: {'name': '倚天剑', 'price': 10000},
    103: {'name': '九阴白骨爪', 'price': 8000},
    104: {'name': '九阳神功', 'price': 9000},
    105: {'name': '祥龙十八章', 'price': 10000}

}
list_oder = []
#
#
'''def gou_wu():
    while True:
        item = int(input('1见购买, 2建结算'))
        if item == '1':
            for key, value in dict_commodity_info.items():
                print( (key,value["name"],value['price']))
            while True:
                cid = int(input('请输入商品编号:'))
                if cid in dict_commodity_info:
                    break
                else:
                    print('商品不存在')
            count = int(input('请输入购买数量:'))
            list_oder.append({'cid': cid, 'count': count})
            print('添加到购物车')
        elif item == '2':
            zong_jia = 0
            for item in list_oder:
                shang_pin = dict_commodity_info[item]
                print( )
                zong_jia += shang_pin['price'] * item
            while True:
                qian = float(input('总价%d元,请输入金额:'))
                if qian>=zong_jia:
                    print('购买成功,找回:%d元' %)
                    list_oder.clear()
                    break
                else:
                    print('金额不足')
gou_wu()'''
