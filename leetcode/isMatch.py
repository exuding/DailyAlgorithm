#_*_coding:utf-8_*_
'''
@project: DailyAlgorithm
@author: exudingtao
@time: 2019/12/7 8:26 下午
'''
def isMatch(s, p):
    dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
    dp[0][0] = True
    for j in range(1, len(p) + 1):
        dp[0][j] == (j >= 2) and (p[j - 1] == '*') and (dp[0][j - 2])

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))
            else:
                dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '.')

    return dp[len(s)][len(p)]