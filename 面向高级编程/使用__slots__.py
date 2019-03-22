#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# PEP 8: expected 2 blank lines, found 0   说的是声明函数的那一行的上方必须有两行的空行，否则便出现这个情况。
from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'bingley'
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)
print(s.age)
property(s.name)


