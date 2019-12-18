#-*- coding:utf-8 -*-
'''
@project: DailyAlgorithm
@author: taoxudong
@time: 2019-12-17 09:55:02 
'''


def isValid(s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''

def isValid1(s):
    if len(s)==0:
        return True
    if len(s)%2 != 0:
        return False
    res = []
    for i in s:
        if i in ['(','{','[']:
            res.append(i)
        else:
            if res:
                if i==')' and res[-1] == '(' or i==']' and res[-1] == '[' or i=='}' and res[-1] == '{':
                    res.pop()#默认删除最后一个 也可指定索引
                else:
                    return False
            else:
                return False
    if res:
        return False
    else:
        return True
print(isValid1('[]{}()'))
