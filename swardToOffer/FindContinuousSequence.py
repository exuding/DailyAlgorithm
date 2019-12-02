#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-13 11:38:22 
'''
'''
9~16的和,是100。
究竟有多少种连续的正数序列的和为100(至少包括两个数)。
另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列?
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        res = []
        start = 1
        end = 2
        for i in range(start,tsum):
            while sum(range(i,end+1))<tsum:
                end = end + 1
            if sum(range(i,end+1)) == tsum:
                res.append([j for j in range(i,end+1)])
                end = i + 1
                continue
            elif sum(range(i,end+1)) > tsum:
                end = i + 1
                continue
        return res

s = Solution()
a = s.FindContinuousSequence(100)
print(a)
