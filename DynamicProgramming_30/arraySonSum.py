#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-04 13:58:56 
'''
'''
在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        len_array = len(array)
        if len_array == 0:
            return 0
        curMax = []
        resMax = array[0]
        curMax.append(resMax)
        for i in range(1,len_array):
            #动态规划转移方程
            if curMax[i-1]>0:
                curMax.append(curMax[i-1] + array[i])
            else:
                curMax.append(array[i])
            #更新最大值
            if curMax[i]>resMax:
                resMax = curMax[i]
        return resMax
s = Solution()
a = s.FindGreatestSumOfSubArray([1,3,5,-1,5,-6])
print(a)