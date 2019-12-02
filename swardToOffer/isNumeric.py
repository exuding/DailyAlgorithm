#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-18 09:08:29 
'''
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是
'''
#规则e在中间，其他特殊字符不能出现两次
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        list_s = list(s)
        count_fuhao = 0
        temp = []
        for i in range(len(list_s)):
            if list_s[i] < '0' or list_s[i] > '9':
                if list_s[i] == 'e' and i != len(list_s)-1:
                    temp.append(list_s[i])
                    continue
                elif list_s[i] == 'e' and i == len(list_s)-1:
                    return False
                elif list_s[i] != 'e' and list_s[i] != 'E' and list_s[i] != '+' and list_s[i] != '-' and list_s[i] != '.':
                    return False
                else:
                    temp.append(list_s[i])
        if len(temp)<=1:
            if '+' in temp:
                print(list_s.index('+'))
                if list_s.index('+')!=0:
                    return False
            if '-' in temp:
                if list_s.index('-')!=0:
                    return False
            else:
                return True
        if len(temp)>=2:
            if temp.count('.')>=2:
                return False
            if 'e' in temp and '.' in temp:
                if temp.index('.')>temp.index('e'):
                    return False
            for i in range(len(temp)):
                if temp[i] =='+' or temp[i]=='-':
                    count_fuhao = count_fuhao +1
                    if count_fuhao >=2:
                        if (temp[0] == '+' or temp[0] == '-')and (temp[temp.index('-')-1]=='e' or temp[temp.index('-')-1]=='E'):
                            continue
                        elif (temp[0] == '+' or temp[0]== '-') and (temp[-1]=='+' or temp[-1]=='-')  and len(temp)>=3:
                            continue
                        else:
                            return False
        return True