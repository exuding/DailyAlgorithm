#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-10 11:29:55 
'''
'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
class Solution:
    def PrintMinNumber(self, numbers):
        res = []
        #循环一遍选择一个最小的作为第一个元素
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                flag = Solution.getMinNumber(self,numbers[i],numbers[j])
                if flag ==1:
                    temp = numbers[i]
                    numbers[i] = numbers[j]
                    numbers[j] = temp
            res.append(numbers[i])
        re = ''.join('%s'%num for num in res)
        return re

    #比较两个数字谁放在前面更小
    def getMinNumber(self,a,b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        list_ab = list(ab)
        list_ba = list(ba)
        for i in range(len(list_ab)):
            if list_ab[i] > list_ba[i]:
                #选择b
                flag = 1
                return flag
            elif list_ab[i] == list_ba[i]:
                continue
            else:
                #选择a
                flag = 0
                return flag
s = Solution()
a = s.PrintMinNumber([3,5,1,4,2])
print(a)