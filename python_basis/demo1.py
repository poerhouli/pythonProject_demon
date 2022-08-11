# 浅拷贝
# li = [800, [1000, 500]]
#
# li01 = li.copy()
# print(li01)
# import copy
#
# li = [800, [1000, 500]]
# li01 = copy.deepcopy(li)
# li01[1][0] = 900
# print(li01[1][0])

# name=input('请输入你的邮箱：')
# if name.endswith('@qq.com'):
#     print('这是一个qq邮箱')
# elif name.endswith('@163.com'):
#     print('这是一个网易邮箱')
# else:
#     print('请输入正确的邮箱')

# ls1 = ['1', '2', '3', '4', '5']
# ls1[1] = 'li'
# print(ls1)  #通过索引对列表进行复赋值
ls1 = [1, 6, 3, 4, 5, 8, 9, 10]
# print(ls1[::-1])  #序列反转
# ls1.append('6') #末尾添加
# ls1.remove('6')  #删除
# del ls1[4]  # 通过下标删除
# print(ls1)
# ls1.sort()  #升序
# ls1.sort(reverse=True)  #降序
# 元祖转换列表
# tu=(1,2,'hello','world')
# ls = list(tu)
# print(ls)
dict1 = {'name': '张三', 'age': '18'}
for k, v in dict1.items():
    print(k, v)
