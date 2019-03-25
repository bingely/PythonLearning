#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math


def my_abs(x):
    if x > 0:
        return x
    return 0


# 加入参数检查内置函数isinstance()
def my_abs_improve(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad type error')
    if x > 0:
        return x
    return 0


print(my_abs(0))
print(my_abs_improve(11))


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(10, 11, 2)
print(x, y)

'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。

提示：计算平方根可以调用math.sqrt()函数：
'''


def quadratic(a, b, c):
    pass
