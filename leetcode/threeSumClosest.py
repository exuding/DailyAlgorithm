#-*- coding:utf-8 -*-
'''
@project: DailyAlgorithm
@author: taoxudong
@time: 2019-12-13 09:16:36 
'''
'''
双指针法的解题思路：
    1.先让数组有序，也就是需要先对数组进行排序
    2.然后每次固定一个元素，再去寻找另外两个元素，也就是双指针
双指针法的代码实现：
    1.对数组进行排序
    2.初始化一个用于保存结果的值 result = nusm[0] + nums[1] + nums[2] （不要自己设初值，直接从数组中抽取三个元素，假设这是最接近的三数之和，然后再更新就是了）。
    3.利用下标 i 对数组进行遍历，此时就是在固定第一个元素，注意，下标 i 的边界为 i < nums.length-2，否则设置指针的时候会出现数组越界。
    4.每次遍历的过程中设置两个指针，分别是 left = i + 1、right = nums.length - 1。
    5.检查 sum = nums[i] + nums[left] + nums[right]与 target 的距离，如果该距离比之前保存的 result 与 target 的距离更小，就更新 result。
    6.然后就是移动双指针：
    如果 sum 的值比 target 大，那么我们让 right--，因为数组是有序的，right --会使得下一次的 sum 更小，也就更接近 target 的值
    同理，如果 sum 的值 target 小，那么我们让 left++。·
    left++ 和 right-- 的界限自然是 left != right，如果 left == right，说明我们已经将所有的元素都遍历过一遍了。
    重复上面的操作，直到i循环结束为止，返回 result。
    '''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return ''
        nums.sort()
        min_num = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            first = i+1
            last = len(nums)-1
            while first != last:
                temp = nums[first]+nums[last]+nums[i]
                if temp == target:#相等
                    return target
                if abs(temp - target) < abs(min_num - target):#更新结果
                    min_num = temp
                if temp > target:#更新指针
                    last-=1
                    # 跳过重复元素
                    while first < last-1 and nums[last] == nums[last - 1]:
                        last -= 1
                else:#更新指针
                    first += 1
                    #跳过重复元素
                    while first < last-1 and nums[first] == nums[first + 1]:
                        first += 1
        return min_num


def threeSumClosest1(nums,target):
    if len(nums)<3:
        return ''
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        first = i + 1
        last = len(nums) - 1
        while first != last:
            sum = nums[first] + nums[last] + nums[i]
            if abs(sum - target) < abs(result - target):  # 更新结果
                result = sum
            if sum > target:  # 更新指针
                last -= 1
            else:  # 更新指针
                first += 1
    return result

