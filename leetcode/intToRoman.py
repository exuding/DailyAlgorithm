#-*- coding:utf-8 -*-
'''
@project: DailyAlgorithm
@author: taoxudong
@time: 2019-12-09 14:09:58 
'''

#利用字符串
def intToRoman(num):
    c = {0: ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
         1: ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
         2: ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
         3: ("", "M", "MM", "MMM")}
    res = ''
    str_num = str(num)
    for i in str(num):
        res += c[len(str(num)) - 1][int(i)]
        num = str_num[1:]
    return res
#利用余数和整除
def intToRoman1(num):
    M = ("", "M", "MM", "MMM")
    C = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
    X = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
    I = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")
    return M[num // 1000] + C[(num % 1000) // 100] + X[((num % 100) // 10)] + I[num % 10]

print(intToRoman(1994))