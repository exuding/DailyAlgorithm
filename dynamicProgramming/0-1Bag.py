#-*- coding:utf-8 -*-
'''
@project: Exuding
@author: taoxudong
@time: 2019-08-19 15:16:41 
'''
'''
经典动态规划问题  背包问题
有N件物品和一个容量为V的背包。第i件物品的费用是c[i]，价值是w[i]。
求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。 
'''
'''
0/1背包问题是最基本的背包问题，每个物品最多只能放一次或者选择不放。
思路B：
动态规划的思想本质就是找到递归的表达式。
在找递归的表达式的时候肯定是存在一定的边界限制（如青蛙跳台阶这种题目就没有限制）
那么这道题它给出了一个边界限制：容量M，当容量满的时候就再也放不下东西了，故我们在进行递归的时候需要考虑当前的容量，这就是我们的限制条件
目标函数是什么？目标函数就是我们的价值最大化max(value)

背包问题(Knapsack problem)是一种组合优化的NP完全问题
NP完全问题(NP-C问题)，是世界七大数学难题之一。

动态规划解题步骤（问题抽象化、建立模型、寻找约束条件、判断是否满足最优性原理、找大问题与小问题的递推关系式、填表、寻找解组成）

'''
