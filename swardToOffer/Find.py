#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-07-16 16:08:32 
'''

'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        flag = False
        if len(array)==0:
            return flag
        else:
            if len(array[0])==0:
                return flag
        len_columns = len(array)
        for i in range(len_columns):
            if target > array[i][-1]:
                continue
            else:
                if target in array[i]:
                    flag = True
        return flag
s = Solution()
a = s.Find(7,[[]])
print(a)