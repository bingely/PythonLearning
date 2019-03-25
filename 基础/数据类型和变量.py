#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 如何输出不同类型的数据结合，下面该怎么修改  --- 使用format
print("thisis %s" % (not True))

print('i\'m \"ok\"')

print(3 > 2)
print(True and False)
print(True or False)
print(not True)

print(None)

a = 'ABC'
b = a
a = 'XYZ'
print(b)