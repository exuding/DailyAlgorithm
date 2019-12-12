#_*_coding:utf-8_*_
'''
@project: DailyAlgorithm
@author: exudingtao
@time: 2019/12/7 8:26 下午
'''


class Solution:
    def isMatch(self, s, p):
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]  # 初始化二维表dp
        dp[0][0] = True  # s 和 p 都为空时
        #  若 s 为空时
        for j in range(1, len(p) + 1):
            # dp[0][j]= (p[j-1]=="*")and(j>=2)and(dp[0][j-2])            #  等同于下列语句
            if p[j - 1] == '*':
                if j >= 2:
                    dp[0][j] = dp[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                #  j-1才为正常字符串中的索引
                #  p当前位置为"*"时，(代表空串--dp[i][j-2]、一个或者多个前一个字符--( dp[i-1][j] and (p[j-2]==s[i-1] or p[j-2]=='.'))
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (
                                dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))  # dp[i][j-1] or
                #  p当前位置为"."时或者与s相同时，传递dp[i-1][j-1]的真值
                else:
                    dp[i][j] = (p[j - 1] == '.' or p[j - 1] == s[i - 1]) and dp[i - 1][j - 1]

        return dp[len(s)][len(p)]
