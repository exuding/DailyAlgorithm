#-*- coding:utf-8 -*-
'''
@project: Exuding
@author: taoxudong
@time: 2019-08-15 14:58:05 
'''
'''
198. House Robber
[1,3,6,8,9,5]
挑出和最大的值，不能挑连续的。房间连续就会报警
较简单的动态规划问题
'''
class Solution:
    def rob(self, nums):
        if 0<len(nums)<=2:
            return max(nums)
        if not nums:
            return 0
        if len(nums) ==3:
            return max(nums[0]+nums[2],nums[1])
        res = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if i==0 or i==1:
                res[i]=nums[i]
            if i==2:
                res[i] = nums[i-2]+nums[i]
            else:
                res[i] = max(res[i-3],res[i-2])+nums[i]
        return max(res)