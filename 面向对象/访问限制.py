#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 如何做到可以访问另外一个文件里面的类


class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print("this is age"+self.__name)

    def get_age(self):
        print(self.__age)  # 为啥不能添加str


st = Student("bingley", 12)
print(st.get_name())
print(st.get_age())



