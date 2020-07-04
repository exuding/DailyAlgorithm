#_*_coding:utf-8_*_
'''
@project: Exuding
@author: exudingtao
@time: 2019/12/28 2:54 下午
'''
#包含有效括号的个数

#用栈和下标
def longestValidParentheses(s):
    stack_temp = []
    stack_temp.append(-1)#-1用的很巧秒
    max_len = 0
    for i in range(len(s)):
        if (s[i] == "("):
            stack_temp.append(i)
        else:
            stack_temp.pop()
            if not stack_temp:#为空
                stack_temp.append(i)
            else:#不为空
                print(stack_temp[-1])
                max_len = max(max_len,i-stack_temp[-1])#就用下标相减，原始是-1
    return max_len
#动态规划
def longestValidParentheses(s):
    if (not s):
        return 0
    res = 0
    n = len(s)
    dp = [0] * n
    for i in range(1, len(s)):
        if (s[i] == ")"):
            if (s[i - 1] == "("):
                dp[i] = dp[i - 2] + 2
            if (s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "("):
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
            res = max(res, dp[i])
    return res
print(longestValidParentheses("()(())"))