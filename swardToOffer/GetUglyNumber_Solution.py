#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-10 17:16:25 
'''
'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
# class Solution:
#     def GetUglyNumber_Solution(self, index):
#         count = 1
#         i = 2
#         temp = [2,3,5]
#         while count<index:
#             if index ==1:
#                 return 1
#             else:
#                 res = Solution.isUglyNumber(self,i)
#                 flag = 1
#                 for j in res:
#                     if j not in temp:
#                         flag = 0
#                         break
#                 if len(res) >3:
#                     i = i + 1
#                 elif len(res)<=3 and flag ==1:
#                     count = count + 1
#                     i = i + 1
#         return i
#
#     def isUglyNumber(self,n):
#         #找一个数的所有质因子
#         res = []
#         for i in range(1,int(n/2)):
#             if n%i == 0 and i%2 == 0:
#                 res.append(i)
#         return res
#
#
# s = Solution()
# a = s.GetUglyNumber_Solution(5)
# print(a)
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<1:
            return 0
        data=[1,]
        index2=0
        index3=0
        index5=0
        indexitter=0
        while indexitter<index:
            indexitter+=1
            d= min(data[index2]*2,data[index3]*3,data[index5]*5)
            data.append(d)
            if data[index2]*2==d:
                index2+=1
            if data[index3]*3==d:
                index3+=1
            if data[index5]*5==d:
                index5+=1
        return data[index-1]
s = Solution()
a = s.GetUglyNumber_Solution(10)
print(a)
