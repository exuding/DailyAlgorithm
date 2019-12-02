#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-14 17:13:12 
'''
#写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''
思路：位运算
两个数异或：相当于每一位相加，而不考虑进位；
两个数相与，并左移一位：相当于求得进位；
将上述两步的结果相加

下Python对位操作简直是深坑一座- -
主要原因还是因为python没有无符号又移操作，所以需要越界检查一波～
'''
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, a, b):
        while(b):
           a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
        return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)