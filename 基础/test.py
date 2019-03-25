#!/usr/bin/env python 
# -*- coding:utf-8 -*-


t = ('a', 'b', ['A', 'B'])
t[2, 0] = 'X'
t[2, 1] = 'Y'
print('得到后', t)