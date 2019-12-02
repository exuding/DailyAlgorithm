#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-14 17:07:17 
'''
#求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
#Python版的短路求值代码
#要注意python中逻辑运算符的用法，a  and  b，a为False，返回a，a为True，就返回b
class Solution:
    def Sum_Solution(self, n):
        # write code here
        ans=n
        temp=ans and self.Sum_Solution(n-1)
        ans=ans+temp
        return ans