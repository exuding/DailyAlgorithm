#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-13 14:24:04 
'''
'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
'''
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        res = []
        for i in range(len(array)):
            temp = []
            if tsum-array[i] in array[i+1:]:
                print(1)
                temp.append(array[i])
                temp.append(tsum-array[i])
                res.append(temp)
        if res:
            return res[0]
        else:
            return []
s = Solution()
a = s.FindNumbersWithSum([1,2,4,7,11,16],10)
print(a)
