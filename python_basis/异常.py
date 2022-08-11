'''def dev_applice(applice1):
    person = int(input('请输入人数:'))
    result = applice1 / person
    print('每人分:', result)


# 建议分门别类

try:
    dev_applice(10)
except ValueError:
    print('输入必须是整数')
except ZeroDivisionError:
    print('输入不能为0')
except Exception:
    print('未知错误')
finally:
    # 无论是否异常，一定会执行的代码
    print('没有出错的代码')'''


def sourl():
    while True:
        result = int(input('请输入成绩:'))
        try:
            sore = int(result)
        except ValueError:
            continue
        if 0 <= sore <= 100:

            return result
        else:
            print('输入整数')


print(sourl())
