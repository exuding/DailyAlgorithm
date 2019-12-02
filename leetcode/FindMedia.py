#_*_coding:utf-8_*_
'''
@project: leetcode
@author: exudingtao
@time: 2019/11/30 10:04 下午
'''

'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    示例 1:
    nums1 = [1, 3]
    nums2 = [2]
    则中位数是 2.0
    示例 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    则中位数是 (2 + 3)/2 = 2.5
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        #奇数找中位数，偶数找中间两数平均
        #注意原数组是有序数组
        '''
            这个题目可以归结到寻找第k小(大)元素问题
            对于奇数的情况，直接找到最中间的数即可，偶数的话需要求最中间两个数的平均值。
            为了简化代码，不分情况讨论，我们使用一个小trick，我们分别找第 (m+n+1) / 2 个，和 (m+n+2) / 2 个，然后求其平均值即可，这对奇偶数均适用。
            思路可以总结如下：取两个数组中的第k/2个元素进行比较，
            如果数组1的元素小于数组2的元素，
            则说明数组1中的前k/2个元素不可能成为第k个元素的候选，
            所以将数组1中的前k/2个元素去掉，组成新数组和数组2求第k-k/2小的元素，
            因为我们把前k/2个元素去掉了，所以相应的k值也应该减小。
            另外就是注意处理一些边界条件问题，比如某一个数组可能为空或者k为1的情况。
        '''

        def findKthElement(arr1, arr2, k):
            len1, len2 = len(arr1), len(arr2)
            if len1 > len2:
                #数组长的作为参数2
                return findKthElement(arr2, arr1, k)
            if not arr1:
                #如果短的参数1为空 递归返回条件
                return arr2[k - 1]
            if k == 1:
                #递归返回条件
                return min(arr1[0], arr2[0])
            i, j = min(k // 2, len1) - 1, min(k // 2, len2) - 1
            if arr1[i] > arr2[j]:
                return findKthElement(arr1, arr2[j + 1:], k - j - 1)
            else:
                return findKthElement(arr1[i + 1:], arr2, k - i - 1)

        l1, l2 = len(nums1), len(nums2)
        left, right = (l1 + l2 + 1) // 2, (l1 + l2 + 2) // 2
        return (findKthElement(nums1, nums2, left) + findKthElement(nums1, nums2, right)) / 2
