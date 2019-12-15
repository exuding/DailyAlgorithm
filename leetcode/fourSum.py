#_*_coding:utf-8_*_
'''
@project: DailyAlgorithm
@author: exudingtao
@time: 2019/12/15 11:01 下午
'''
def fourSum(nums,target):
    if not nums:
        return []
    nums.sort()
    res = []
    for i in range(len(nums)):
        first = i+1
        last = len(nums)-1
        while first<last:
            temp_list = []
            temp = nums[i] + nums[first] + nums[last]
            if target - temp in nums[first+1:last]:
                temp_list.append(nums[i])
                temp_list.append(nums[first])
                temp_list.append(nums[last])
                temp_list.append(target-temp)
                if temp_list not in res:
                    res.append(temp_list)
                #res.append((nums[i],nums[first],nums[last],target-temp))
            if first+1<last:
                last-=1
            else:
                last = len(nums) - 1
                first+=1

    return res

def fourSum1(nums, target):
    nums.sort()
    length = len(nums)
    ans = []
    for i in range(length):
        for j in range(i + 1, length):
            l, r, t = j + 1, length - 1, target - nums[i] - nums[j]
            while l < r:
                while l < r and t > nums[l] + nums[r]: l += 1
                while l < r and t < nums[l] + nums[r]: r -= 1
                if l < r and nums[l] + nums[r] == t:
                    ans.append([nums[i], nums[j], nums[l], nums[r]])
                l += 1
    return list(set(map(tuple, ans)))
print(fourSum([-3,-1,0,2,4,5],2))


