#-*- coding:utf-8 -*-
'''
@project: DailyAlgorithm
@author: taoxudong
@time: 2019-12-06 09:32:51 
'''
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1),-2**31)