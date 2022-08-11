'''
函数练习
'''

# def print_list(list_tar):
#     for item in list_tar:
#         print(item)
#
#
# list_target = [1, 2, 3, 4, 56, 5, 767]
# print_list(list_target)
# def print_list(doublt):
#     '''
#     打印二维列表
#     :param doublt:
#     :return:
#     '''
#     for line in doublt:
#         for item in line:
#             print(item, end=' ')
#         print()
#
#
# list_target = [
#     [1, 2, 3, 4, 5],
#     [1, 23, 43, 45],
#     [12, 2]
# ]
# print_list(list_target)
# '''
# 函数返回值
# '''
#
#
# # 参数是调用者传递给定义这的信息
# # 返回值：定义这传递给调用者的结果
# def func(a):
#     print('func01执行')
#     # 作用 ： 1.返回结果   2.退出方法
#     return 20


# re = func(10)
# print(re)
# def add(a, b):
#     return a + b
#
#
# a = int(input('请输入第一个数字:'))
# b = int(input('请输入第二个数字:'))
#
# re = add(a, b)
# print(re)
# def print_o(number):
#     result = number % 10
#     result += number//10%10
#     result += number//100%10
#     result += number//1000
#     return result
#
# number = int(input('请输入四位整数:'))
# p = print_o(234)
# print(p)

# def calculate_weight(liang_weight):
#     '''
#     根据两计算斤
#     :param liang_weight:
#     :return:
#     '''
#     jin = liang_weight//16
#     liang = liang_weight % 16
#     return jin,liang
# p = calculate_weight(1)
# print(str(p[0])+ '斤,两'+str(p[1]))
# def is_repeation(list_target):
#     for r in range(0,len(list_target) -1):
#         for c in range(r+1,len(list_target)):
#             if list_target[r] == list_target[c]:
#                 return True #有重复
#         return False  #没有重复
# print(is_repeation([3,81,3,5,81,4]))

# def foun01(a):
#     a = 100
# num = 1
# foun01(num)
# print(num)
'''
不可变类型参数：

    数值型（整数）函数内部不可改变原数据
    布尔
    空值
    字符串
    元祖
    固定集合
可变类型参数：函数内部可以改变原数据
    列表
    字典
    集合

'''
import json

data = {
    "databaseAddress\":\"\",\"databaseName\":\"\",\"databasePassword\":\"\",\"databaseUser\":\"\",\"deploymentIp\":\"172.31.56.89\",\"enabled\":1,\"environment\":\"dev\",\"id\":14,\"jdEdiServiceUrl\":\"\",\"jdSettlementServiceUrl\":\"\",\"lastReportIp\":\"172.31.56.89\",\"lastReportTime\":1635143755000,\"monitor\":2,\"paymentIp\":\"172.31.56.87\",\"paymentPort\":\"11810\",\"projectFileAddress\":\"xps_grxy_project\",\"projectId\":146798369,\"projectName\":\"测试项目\",\"purchaseIp\":\"172.31.56.88\",\"purchasePort\":\"12110\",\"salesIp\":\"172.31.56.89\",\"salesPort\":\"12010\",\"supplierId\":\"\"}"}
data2 = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
print(data2)
