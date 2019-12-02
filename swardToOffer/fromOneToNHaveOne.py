#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-10 10:25:45 
'''
'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次。
把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
'''
#内存溢出
# import sys
# sys.setrecursionlimit(100000) #例如这里设置为十万
# def NumberOf1Between1AndN_Solution(n):
#     number_n = list(str(n))
#     if n == 1:
#         return 1
#     else:
#         count = 0
#         for i in number_n:
#             if i == '1':
#                 count = count + 1
#         return NumberOf1Between1AndN_Solution(n-1)+count
#
# a = NumberOf1Between1AndN_Solution(10000)
# print(a)
class Solution:
    def getNhaveOneNum(self,n):
        count = 0
        number_n = list(str(n))
        for i in number_n:
            if i == '1':
                count = count +1
        return count
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        sum = 0
        #注意n+1
        for i in range(1,n+1):
            count = Solution.getNhaveOneNum(self,i)
            sum = sum + count
        return sum

s = Solution()
a = s.NumberOf1Between1AndN_Solution(10)
print(a)