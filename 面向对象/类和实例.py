#!/usr/bin/env python 
# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_score2(self):   # 为啥定
        print('%s: %s' % (self.name, self.score))


# 如果想调用无参构造函数怎么办
bar = Student("bingley", 28)
print(bar)
print(bar.name)


# 数据封装
def print_score(std):
    print('%s:%s' % (std.name, std.age))    # 注意格式


# 为啥定义在类中的方法无效？？？？
print_score2(bar)
