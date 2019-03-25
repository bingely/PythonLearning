#!/usr/bin/env python 
# -*- coding:utf-8 -*-

if 4 > 5:
    print('4 more than 5')
elif 8 > 7:
    print('8 dayu 7')
else:
    print("else")

# ************再议 input***********
birth = input('birth: ')
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')
