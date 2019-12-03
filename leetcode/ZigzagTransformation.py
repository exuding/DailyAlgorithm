#-*- coding:utf-8 -*-
'''
@project: DailyAlgorithm
@author: taoxudong
@time: 2019-12-03 09:25:21 
'''

#解法一：暴力解法
def convert(s, numRows):
    if len(s)==1:
        return s
    if numRows ==1:
        return s
    s = list(s)
    n = 0
    temp = [[0 for i in range(len(s))] for j in range(numRows)]
    for j in range(0, len(s), numRows - 1):#numRows - 1 不能为0
            for i in range(0,numRows):
                if i<=numRows-1 and n<len(s):
                    temp[i][j] = s[n]
                    n = n+1
                else:
                    break
            for i in range(1,numRows-1):
                if i<=numRows-2 and n <len(s):
                    temp[numRows-i-1][j+i] = s[n]
                    n = n + 1
                else:
                    break
    res = []
    for row in range(len(temp)):
        for col in range(len(s)):
            if temp[row][col]!=0:
                res.append(temp[row][col])

    return ''.join(res)
print(convert('sfdfsfsdfd',4))