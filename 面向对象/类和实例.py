#!/usr/bin/env python 
# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 数据封装
    def print_score(std):
        print('%s:%s' % (std.name, std.age))  # 注意格式


# 如果想调用无参构造函数怎么办
bar = Student("bingley", 28)
print(bar)
print(bar.name)


# 为啥定义在类中的方法无效？？？？
bar.print_score()
