'''元祖'''

tuple01 = (1, 2, 3, 4)
e = tuple01[1]
print(type(e))
month = int(input('请输入月份:'))
if month < 1 or month > 12:
    print('输入有误')
else:
    day_month = (31, 28, 31, 30, 31, 30, 31, 30, 31)
    print(day_month[month - 1])
