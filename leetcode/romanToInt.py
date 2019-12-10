#-*- coding:utf-8 -*-
'''
@project: DailyAlgorithm
@author: taoxudong
@time: 2019-12-09 19:51:48 
'''
#Python里有这个机制 负一索引对应的就是最后数组最后一个元素
def romanToInt(s):
    #"IV""XL""CD"  4系列
    #"IX""XC""CM"  9系列
    c = {'M':1000,
         'C':100,
         'D':500,
         'X':10,
         'L':50,
         'I':1,
         'V':5}
    res = 0
    for i in s:
        temp = c[i]
        res +=temp
    s_list = list(s)
    for i in range(1,len(s_list)):#Python里有这个机制 负一索引对应的就是最后数组最后一个元素
        if s_list[i]=='V' and s_list[i-1]=='I':
            res -=2
        elif s_list[i]=='L' and s_list[i-1]=='X':
            res -=20
        elif s_list[i]=='D' and s_list[i-1]=='C':
            res -=200
        elif s_list[i]=='X' and s_list[i-1]=='I':
            res -=2
        elif s_list[i]=='C' and s_list[i-1]=='X':
            res -=20
        elif s_list[i]=='M' and s_list[i-1]=='C':
            res -=200
        else:
            res =res
    return res
print(romanToInt('MMMCDXC'))



