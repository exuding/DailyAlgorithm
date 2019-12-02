#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-11 10:42:47 
'''

'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
'''
#复杂度太高 O(n^2)
# class Solution:
#     def InversePairs(self, jupyter):
#         count = 0
#         for i in range(len(jupyter)):
#             for j in range(i+1,len(jupyter)):
#                 if jupyter[i] > jupyter[j]:
#                     count = count + 1
#         res = count%1000000007
#         return res
#归并排序时间复杂度是O(n logn)，但同时归并排序需要一个长度为n的辅助数组，
# 相当于用O（n）的空间消耗换来了时间效率的提升，因此这是一种空间换时间的算法。
# class Solution:
#     def InversePairs(self, jupyter):
#         # write code here
#         return self.inverseCount(jupyter[:], 0, len(jupyter) - 1, jupyter) % 1000000007
#
#     def inverseCount(self, tmp, start, end, jupyter):
#         #tmp为辅助数组，和原数组相同
#         if end - start < 1:
#             return 0
#         if end - start == 1:
#             if jupyter[start] <= jupyter[end]:
#                 return 0
#             else:
#                 tmp[start], tmp[end] = jupyter[end], jupyter[start]
#                 return 1
#         mid = (start + end) // 2
#         cnt = self.inverseCount(jupyter, start, mid, tmp) + \
#               self.inverseCount(jupyter, mid + 1, end, tmp)
#         # print(start, mid, end, cnt, jupyter)
#         i = start
#         j = mid + 1
#         ind = start
#
#         while (i <= mid and j <= end):
#             if jupyter[i] <= jupyter[j]:
#                 tmp[ind] = jupyter[i]
#                 i += 1
#             else:
#                 tmp[ind] = jupyter[j]
#                 cnt += mid - i + 1
#                 j += 1
#             ind += 1
#         while (i <= mid):
#             tmp[ind] = jupyter[i]
#             i += 1
#             ind += 1
#         while (j <= end):
#             tmp[ind] = jupyter[j]
#             j += 1
#             ind += 1
#         return cnt


class Solution:
    def InversePairs(self, data):
        # 发现可以用归并排序，归并拼接后用计算排序时元素的index变动了多少
        # 两个有序序列，每个元素移动index数（严格来说不是移动，这里不知怎么表达）之和好像刚好等于逆序对的个数
        # 我也不知为什么，找了半天发现了这个规律
        _, s = self.MergeSort(data)
        return s % 1000000007

    def MergeSort(self, data):
        n = len(data)
        # 递归基
        if n == 1: return data, 0
        # 分两半来排序
        part1, part2 = data[:n // 2], data[n // 2:]
        sorted_part1, s1 = self.MergeSort(part1)
        sorted_part2, s2 = self.MergeSort(part2)
        # 排序后拼接这两半，拼接后先计数，然后将两个有序序列合并
        s, sorted_temp = 0, sorted_part1 + sorted_part2
        # 用p、q两个指针指向两段，计算q中每个元素离插入点的index差
        p, q, len1, len_all = 0, sorted_temp.index(sorted_part2[0]), len(sorted_part1), len(sorted_temp)
        while p < len1 and q < len_all:
            # 移动p使p成为插入排序的插入点，计算要移动多少个位置
            while p < len1:
                if sorted_temp[q] < sorted_temp[p]:
                    s += len1 - p
                    break
                p += 1
            q += 1
        # 完成排序，并把排序后的内容回溯给上一级做准备
        l = []
        p, q = 0, sorted_temp.index(sorted_part2[0])
        while p < len1 and q < len_all:
            if sorted_temp[p] < sorted_temp[q]:
                l.append(sorted_temp[p])
                p += 1
            else:
                l.append(sorted_temp[q])
                q += 1
        if p == len1: l += sorted_temp[q:]
        if q == len_all: l += sorted_part1[p:]
        return l, s + s1 + s2
s = Solution()
a = s.InversePairs([1,2,3,4,5,6,7,0])
print(a)