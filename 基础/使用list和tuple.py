#!/usr/bin/env python
# -*- coding:utf-8 -*-

classmates = ['Michal', 'Bob', 'Cicy']
print(classmates)
print(len(classmates))  # 不是 classmate.getLen()

# add
classmates.append('DiDi')
print('append', classmates)

# delete
classmates.pop()
print('pop', classmates)
classmates.pop(1)
print('pop(1)', classmates)

# update
classmates.insert(1, "bingley")
classmates.append('Adam')
print('insert', classmates)

# search
print(classmates[0])
print(classmates[-1])

L = ['ABC', True, 123]
print(L)

# ***********************tuple**************
t = ('ABC', True, 123)
print(t)
t = (1,)
print("只有一个元素", t)

# 为啥不能操作，教程里面可以操作的？？？？
#  TypeError: 'tuple' object does not support item assignment
'''
t = ('a', 'b', ['A', 'B'])
t[2, 0] = 'X'
t[2, 1] = 'Y'
print('得到后', t)
'''

