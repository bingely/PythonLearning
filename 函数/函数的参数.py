#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2, 5))
print(power(3))


def add_end(L=[]):
    L.append('END')
    return L


def add_end_improve(L=None):  # 定义默认参数要牢记一点：默认参数必须指向不变对象！
    if L is None:
        L = []
    L.append('END')
    return L


'''
为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
'''

result = add_end([1, 2, 3])
print(result)

add_end()
print(add_end())

add_end_improve()
print(add_end_improve())


#  可变参数


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))
s = [1, 2, 3]
print(calc(*s))
