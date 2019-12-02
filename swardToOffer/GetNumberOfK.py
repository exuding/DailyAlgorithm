#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-11 15:49:47 
'''
'''
统计一个数字在排序数组中出现的次数
'''
class Solution:
    def GetNumberOfK(self, data, k):
        #二分查找到位置,前后统计个数
        #[]----情况
        if len(data) == 0:
            return 0
        #[3]3----情况
        if len(data)==1 and k in data:
            return 1
        index = Solution.getNumber(self, data, 0, len(data) - 1, k)
        #[1，2，3，4] 5---情况
        if index == None:
            return 0
        count = 0
        if index != None:
            count = 1
            flagA = 1
            flagB = 1
            tempb = index+1
            if index ==0:
                count = 0
                tempa = 0
            else:
                tempa = index - 1
            while flagA:
                if data[tempa] == k:
                    count = count +1
                    if tempa == 0:
                        flagA = 0
                    else:
                        tempa = tempa -1
                else:
                    flagA = 0

            while flagB:
                if data[tempb] == k:
                    count = count + 1
                    if tempb == len(data)-1:
                        flagB = 0
                    else:
                        tempb = tempb + 1
                else:
                    flagB = 0
        return count

    def getNumber(self,data,i,j,k):
        mid = int((i + j)/2)
        if k>data[-1]:
            return None
        if k<data[0]:
            return None
        if k not in data:
            return None
        if data[mid] == k:
            return mid
        elif data[mid]>k:
            return Solution.getNumber(self,data,i,mid,k)
        else:
            return Solution.getNumber(self,data,mid,j,k)
s = Solution()
a = s.GetNumberOfK([],2)
print(a)


