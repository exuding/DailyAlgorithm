#-*- coding:utf-8 -*-
'''
@project: Exuding
@author: taoxudong
@time: 2019-08-16 09:52:41 
'''
'''
213. House Robber2
[1,3,6,8,9,5]
挑出和最大的值，不能挑连续的。房间连续就会报警 另外房间首位相接
较简单的动态规划问题

状态转移方程：
dp[0] = num[0] （当i=0时） 
dp[1] = max(num[0], num[1]) （当i=1时） 
dp[i] = max(num[i] + dp[i - 2], dp[i - 1]) （当i !=0 and i != 1时）
'''
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        N = len(nums)
        return max(self.rob_range(nums[0: N - 1]), self.rob_range(nums[1: N]))

    def rob_range(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

