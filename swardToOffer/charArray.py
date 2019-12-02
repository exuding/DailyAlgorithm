#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-03 14:58:11 
'''
#输入一个字符串,按字典序打印出该字符串中字符的所有排列。
#例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
class Solution:
    def Permutation(self, ss):
        ss_list = list(ss)


