#-*- coding:utf-8 -*-
'''
@project: DailyAlgorithm
@author: taoxudong
@time: 2019-12-17 09:55:02 
'''


def isValid(self, s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''