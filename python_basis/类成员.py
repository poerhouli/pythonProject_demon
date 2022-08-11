'''

类成员
    @classmethod
    def 方法名称（cls,参数列表）
'''


class Icbc:
    # 表示总行的钱
    total_money = 100000

    # 因为类方法没有对象地址self，所以不能访问实例成员
    @classmethod
    def print_cle_lei(cls):
        print(cls, Icbc)
        print('总行还剩%d' % Icbc.total_money)

    def __init__(self, name, money):
        self.name = name
        self.money = money
        Icbc.total_money -= money


p = Icbc('农行', 10000)
print('总行还剩%d' % Icbc.total_money)
Icbc.print_cle_lei()

'''
定义老婆类，创建三个老婆对象
通过类变量记录老婆

'''


class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print('我有%d房' % Wife.count)

    def __init__(self, name):
        self.name = name
        Wife.count += 1


p0 = Wife('如花')
p1 = Wife('小花')
p2 = Wife('小张')
Wife.print_count()
