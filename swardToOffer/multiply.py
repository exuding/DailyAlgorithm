#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-17 14:40:39 
'''
'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。
'''
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        for i in range(len(A)):
        	temp = 1
        	for j in range(len(A)):
        		if i!=j:
        			temp = temp*A[j]
        	B.append(temp)
        return B

s = Solution()
a = s.multiply([1,3,5,7])
print(a)