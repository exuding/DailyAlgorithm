#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-17 09:43:01 
'''
'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
'''
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
       for i in range(len(numbers)):
           if numbers[i] in numbers[i+1:]:
               duplication.append(numbers[i])
               return duplication
           else:
               continue
       if len(duplication)==0:
            return False

s=Solution()
a = s.duplicate([2,4,3,1,5],[])
print(a)


