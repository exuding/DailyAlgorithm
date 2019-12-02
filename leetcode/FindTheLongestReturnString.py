#-*- coding:utf-8 -*-
'''
@project: leetcode
@author: taoxudong
@time: 2019-12-02 10:51:03 
'''
'''
解法1：暴力解法，找到所有的子串，如果找到的子串比当前所存的最大子串长就替换
      很像选择排序
'''
def longestPalindrome1(s):
    s = list(s)
    sub = s[0:1]#存放最大子串变量
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            temp = s[i:j]
            tempRe = s[i:j][::-1]
            if (temp == tempRe and len(temp)>len(sub)):
                sub = temp

    return ''.join(sub)

'''
解法2:动态规划  算法时间复杂度为O(n*n)，空间复杂度为O(n*n)
动态规划讲解链接：http://hawstein.com/2013/03/26/dp-novice-to-advanced/
动态规划三个元素：最优子结构，边界，状态转移公式
#####本题####
假设dp[i,j]=1表示str[i...j]是回文子串，那个必定存在dp[i+1,j-1]=1。
这样最长回文子串就能分解成一系列子问题，可以利用动态规划求解了

'''
def longestPalindrome2(s):
    #当前算法，时间复杂度为O(n*n)，空间复杂度为O(n*n)
    k = len(s)# 计算字符串的长度
    matrix = [[0 for i in range(k)] for i in range(k)]# 初始化n*n的列表
    logestSubStr = ""# 存储最长回文子串
    logestLen = 0# 最长回文子串的长度

    for j in range(0, k):
        for i in range(0, j + 1):
            if j - i <= 1:
                if s[i] == s[j]:
                    matrix[i][j] = 1# 此时f(i,j)置为true
                    if logestLen < j - i + 1:# 将s[i:j]的长度与当前的回文子串的最长长度相比 
                        logestSubStr = s[i:j + 1]  # 取当前的最长回文子串
                        logestLen = j - i + 1  # 当前最长回文子串的长度
            else:
                if s[i] == s[j] and matrix[i + 1][j - 1]:# 判断
                    matrix[i][j] = 1
                    if logestLen < j - i + 1:
                        logestSubStr = s[i:j + 1]
                        logestLen = j - i + 1
    return logestSubStr

'''
解法三：解法二的优化 算法的空间复杂度就为O(2n)，即O(n)
当j>1时，判断f(i,j)是否为回文子串的操作只与j-1时的的操作相关，
即f(i,j) = g(f(i, j-1))，其中j>1，i in range(0, j+1)，所以接下来就变成求解g()函数了。    
用nlist存储j情况下所有的子串是否为回文子串的标志
用olist存储j-1情况下所有的子串是否为回文子串的标志
那么olist与nlist的关系是什么呢？
nlist[i] = g(olist[i+1])
'''
def longestPalindrome3(s):
    k = len(s)
    olist = [0] * k# 申请长度为n的列表，并初始化
    nList = [0] * k# 同上
    logestSubStr = ""
    logestLen = 0

    for j in range(0, k):
        for i in range(0, j + 1):
            if j - i <= 1:
                if s[i] == s[j]:
                    nList[i] = 1# 当 j 时，第 i 个子串为回文子串
                    len_t = j - i + 1
                    if logestLen < len_t:# 判断长度
                        logestSubStr = s[i:j + 1]
                        logestLen = len_t
            else:
                if s[i] == s[j] and olist[i + 1]:# 当j-i>1时，判断s[i]是否等于s[j]，并判断当j-1时，第i+1个子串是否为回文子串
                    nList[i] = 1# 当 j 时，第 i 个子串为回文子串
                    len_t = j - i + 1
                    if logestLen < len_t:
                        logestSubStr = s[i:j + 1]
                        logestLen = len_t
        olist = nList# 覆盖旧的列表
        nList = [0] * k# 新的列表清空
    return logestSubStr

print(longestPalindrome3('abacds'))