#_*_coding:utf-8_*_
'''
@project: Exuding
@author: exudingtao
@time: 2019/12/26 1:44 下午
'''
'''

思路：
    先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
    再找出另一个最大索引 l 满足 nums[l] > nums[k]；
    交换 nums[l] 和 nums[k]；
    最后翻转 nums[k+1:]。
举个例子：
    比如 nums = [1,2,7,4,3,1]，下一个排列是什么？
    我们找到第一个最大索引是 nums[1] = 2
    再找到第二个最大索引是 nums[4] = 3
    交换，nums = [1,3,7,4,2,1];
    翻转，nums = [1,3,1,2,4,7]
    完毕!
时间复杂度：O(n)
空间复杂度：O(1)
'''


def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    firstIndex = -1
    n = len(nums)

    def reverse(nums, i, j):
        while i < j:#双指针翻转元素，学会
            nums[i], nums[j] = nums[j], nums[i]#必须写在一行
            i += 1
            j -= 1

    for i in range(n - 2, -1, -1):#为啥从-1开始
        if nums[i] < nums[i + 1]:
            firstIndex = i
            break
    # print(firstIndex)
    if firstIndex == -1:
        reverse(nums, 0, n - 1)
        return
    secondIndex = -1
    for i in range(n - 1, firstIndex, -1):
        if nums[i] > nums[firstIndex]:
            secondIndex = i
            break
    nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]#两个元素互换
    reverse(nums, firstIndex + 1, n - 1)#翻转不用返回值
