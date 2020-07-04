#_*_coding:utf-8_*_
'''
@project: DailyAlgorithm
@author: exudingtao
@time: 2019/12/18 1:36 下午
'''

#特殊法
def generateParenthesis(n):
    if n == 0:
        return [""]
    elif n == 1:
        return ["()"]
    elif n == 2:
        return ["()()", "(())"]
    result = []
    for i in range(n):
        j = n - 1 - i
        temp1 = generateParenthesis(i)
        temp2 = generateParenthesis(j)
        result.extend(["(%s)%s" % (p, q) for p in temp1 for q in temp2])
    return result
#回溯法     ----做总结
#https://leetcode-cn.com/problems/generate-parentheses/solution/dong-hua-yan-shi-22-gua-hao-sheng-cheng-by-user743/
'''
回溯算法基本思想：能进则进，进不了则换，换不了则退
    括号生成算法类似于二叉树先序遍历
    可用递归生成问题解空间树
    再用剪枝函数来对解空间树进行剪枝
    括号生成:
        进入左子树条件： ( 括号小于 n
        进入右子树条件： ） 括号小于 （ 括号
'''
def generateParenthesis1(n):
    ans = []
    def backtrack(S = '', left = 0, right = 0):
        if len(S) == 2 * n:#S由''变成一个符合要求的括号组则保存
            ans.append(S)
            return
        if left < n:
            backtrack(S+'(', left+1, right)
        if right < left:
            backtrack(S+')', left, right+1)

    backtrack()
    return ans
#动态规划   ----做总结
def generateParenthesis(n):
    if n == 0:
        return []
    total_l = []
    total_l.append([None])  # 0组括号时记为None
    total_l.append(["()"])  # 1组括号只有一种情况
    for i in range(2, n + 1):  # 开始计算i组括号时的括号组合
        l = []
        for j in range(i):  # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
            now_list1 = total_l[j]  # p = j 时的括号组合情况
            now_list2 = total_l[i - 1 - j]  # q = (i-1) - j 时的括号组合情况
            for k1 in now_list1:
                for k2 in now_list2:
                    if k1 == None:
                        k1 = ""
                    if k2 == None:
                        k2 = ""
                    el = "(" + k1 + ")" + k2
                    l.append(el)  # 把所有可能的情况添加到 l 中
        total_l.append(l)  # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
    return total_l[n]



