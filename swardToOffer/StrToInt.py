#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-17 08:59:08 
'''
'''
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，
但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 
数值为0或者字符串不是一个合法的数值则返回0。
'''


class Solution:
    def StrToInt(self, s):
        # write code here
        res = []
        if len(s) == 0 or s == '0':
            return 0
        list_s = list(s)
        if list_s[0] == '-':
            flag = -1
        else:
            flag = 1
        num = 0
        for i in range(len(list_s)):
            if i == 0 and list_s[i] == '-':
                continue
            if i == 0 and list_s[i] == '+':
                continue
            if list_s[i] < '0' or list_s[i] > '9':
                return 0
            #'5'--->ord('5')=53 -485
            temp = ord(list_s[i]) - 48
            num = num * 10 + temp
        return num if flag == 1 else -num
s = Solution()
a = s.StrToInt('13424')
print(a)