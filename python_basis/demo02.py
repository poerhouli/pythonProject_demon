'''列表推导式，使用简易方法，将可迭代对象转换为列表'''
ls = [5, 56, 6, 77, 7, 8, 9]
# li02 = [i + 1 for i in ls]
# print(li02)
# ls02 = []
# for i in ls:
#
#     if i>10:
#         ls02.append(i+1)
# ls02 = [i+1 for i in ls if i > 10]
# print(ls02)
# 生成1--10之间的数字，的平方存入lso1

list01 = [i ** 2 for i in range(1, 11)]
print(list01)
