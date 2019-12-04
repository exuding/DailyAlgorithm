#-*- coding:utf-8 -*-
'''
@project: DailyAlgorithm
@author: taoxudong
@time: 2019-12-04 09:30:52 
'''
import math  # 导入 math 模块
max = math.pow(2, 31)-1
min = math.pow(2,31)*-1
def reverse(x):
    if x>0:
        a = list(str(x))[::-1]
        for i in a:
            if i == 0:
                a.pop(i)
            else:
                break
        res = int(''.join(a))
        return res if min<res<max else 0

    else:
        a = list(str(x*-1))[::-1]
        for i in a:
            if i == 0:
                a.pop(i)
            else:
                break
        res = int(''.join(a))*-1
        return res if min<res<max else 0

print(reverse(-8910))
