'''
            继承


'''


# 多个子类在概念上是一至的，所以就抽象出一个父类
# 多个子类的共性，可以提取到父类中
class Person:
    pass


class Student(Person):
    def study(self):
        print('学习')

    def say(self):
        print('说话')


class Teacher(Person):
    def teach(self):
        print('讲课')

    def say(self):
        print('说话')
