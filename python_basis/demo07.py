# class Wife:
#     def __init__(self,name,sex):
#         #self是调用当前方法的对象地址
#         self.name = name
#         self.sex = sex
#     def paly(self):
#         print(self.name + '玩耍')
# p = Wife('丽丽','女')
# p.paly()
# class List_student_info:
#
#     def __init__(self, name, age, score, sex):
#         self.name = name
#         self.age = age
#         self.score = score
#         self.sex = sex
#
#     def student(self):
#
#         print(self.name, self.age, self.score, self.sex)
#
#
#
# s01 = list01[0]
# s01.name = '小赵'
# s01.scroe = 98
# print(list01[0].name)
# p = List_student_info('张三', '12', '13', '女')
# p.student()


# list01 = [
#     Student('赵敏', 28, 100, '女'),
#     Student('苏大强', 58, 10, '女'),
#     Student('苏大强', 58, 10, '女'),
# ]


# class Stun:

# def fun(self):
#     for item in list01:
#         if item.name == '苏大强':
#             return item
# print()
def fun01():
    list02 = []
    for item in list01:
        if item.sex == '女':
            list02.append(item)
    return list02


re = fun01()
print(re)


def foun1():
    pass
