# # 外层循环控制行
# def re():
#     for r in range(2):
#         for c in range(4):
#             # 内层循环控制列
#             print('*', end=' ')
#         print()
#
#
# re()


for i in range(4):
    for c in range(6):
        if c % 2 == 0:
            print('*', end=' ')
        else:
            print('#', end=' ')
#     print()
# for i in range(4):
#     for n in range(i+1):
#         print('*', end='')
#     print()
# list1 = [3, 80, 45, 5, 7, 1]
# for r in range(len(list1)-1):
#     for i in range(1, len(list1)):
#         pass
# list1[0] list1[c]

'''
WHILE
 while 条件：
    循环体
 '''
# 死循环：循环条件永远满足。
# while True:
#     usd = int(input('请输入美元:'))
#     print(usd * 6.9)
#     if input('输入q键退出:'):
#         break

# while True:
#     season = input('请输入季度:')
#     if season == '春':
#         print('1,2,3')
#     if season == '夏':
#         print('4,5,6')
#     if season == '秋':
#         print('7,8,9')
#     if season == '冬':
#         print('10,11,12')
#     else:
#
#         break

'''while 循环计数'''
# count = 0
# while count < 3:
#     count += 1
#     usd = int(input('请输入美元:'))
#     print(usd * 6.9)
# 在控制台中输入0 1 2 3 4 5
# count = 0
# while count < 6:
#
#     print(count)
#     count += 1
count = 0
while count <= 8:
    print(count)
    count += 2
