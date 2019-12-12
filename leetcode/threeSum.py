#-*- coding:utf-8 -*-
'''
@project: DailyAlgorithm
@author: taoxudong
@time: 2019-12-12 09:24:17 
'''

def threeSum(nums):
    res = []
    #[0,0]
    if len(nums)<3:
        return []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            temp = 0 - (nums[i] + nums[j])
            if temp in nums[j+1:]:
                temp_res = []
                temp_res.append(nums[i])
                temp_res.append(nums[j])
                temp_res.append(temp)
                temp_res.sort()
                res.append(temp_res)
    lis2 = list()
    for li in res:
        if li not in lis2:
            lis2.append(li)
    return lis2

def threeSum1(nums):
    '''
    1.特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 [][]。
    2.对数组进行排序。
    3.遍历排序后数组：
        3.1若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于0，直接返回结果。
        3.2对于重复元素：跳过，避免出现重复解
        3.3令左指针 L=i+1，右指针 R=n-1，当 L<R 时，执行循环：
            3.3.1当 nums[i]+nums[L]+nums[R]==0，满足存储。在此基础上继续执行循环，如（-1 1 2 2 3）
                 判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R移到下一位置，寻找新的解
            3.3.2若和大于 0，说明 nums[R] 太大，R左移
            3.3.3若和小于 0，说明 nums[L] 太小，L右移

    '''
    # 对列表进行排序
    nums.sort()
    res, k = [], 0
    for k in range(len(nums) - 2):
        # 如果出现最小元素为正数，则不存在和为0的情况，直接返回
        if nums[k] > 0:
            break
        # 如果出现第一个元素重复的情况，为避免重复结果，跳过后续执行
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        # 定义接下来的两个元素的双指针
        i, j = k + 1, len(nums) - 1
        while i < j:
            s = nums[k] + nums[i] + nums[j]
            if s < 0:
                i += 1
                # 跳过重复元素
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
            elif s > 0:
                j -= 1
                # 跳过重复元素
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            else:
                # 当出现元素满足条件是，将结果加入到列表
                res.append([nums[k], nums[i], nums[j]])
                # 接着更新索引（注意跳过相同元素）
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
    return res
print(threeSum([1,2,-2,-1]))