#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-13 14:52:14 
'''
'''
汇编语言中有一种移位指令叫做循环左移（ROL）
就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
'''
class Solution:
    def LeftRotateString(self, s, n):
        if len(s)==0:
            return ''
        if n>len(s):
            n = n % len(s)
        else:
            n = n
        s = list(s)
        s = s[n:]+s[:n]
        s = ''.join(s)
        return s
s = Solution()
a = s.LeftRotateString('sfdsfsf',3)
print(a)