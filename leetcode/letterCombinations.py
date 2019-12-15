#_*_coding:utf-8_*_
'''
@project: DailyAlgorithm
@author: exudingtao
@time: 2019/12/14 3:27 下午
'''

#方法一 遍历上次的组合结果，逐个合并
def letterCombinations(digits):
    KEY = {'2': ['a', 'b', 'c'],
           '3': ['d', 'e', 'f'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']}
    if not digits:
        return ''
    res = ['']#res就是一个逐渐添加的 又每一轮都遍历 完成了全排列
    for num in digits:
        temp =[]
        for char_item in KEY[num]:
            for r in res:
                temp.append(char_item+r)
        res = temp
    return res

#递归
'''
当没有数字的时候返回空
当只有一个数字的时候，返回该数字对应的字母
当有两个数字的时候，返回第一个数字对应的字母分别加上第二个数字所对应的字母，生成字符串列表
当有三个数字的时候，返回第一个数字对应的字母分别加上后两个数字生成的字符串列表
'''


def letterCombinations1(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    dic = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    result = []
    tail = []
    len_d = len(digits)
    if len_d == 0:
        return tail
    if len_d == 1:
        return dic[digits]

    tail = letterCombinations(digits[1:])

    for i in dic[digits[0]]:
        for j in tail:
            result.append(i + j)
    return result
'''
回溯算法（Backtracking）实际上是一个类似枚举的深度优先搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，
当发现已不满足求解条件时，就“回溯”返回到上一步还能执行的状态，尝试别的路径，类似于走迷宫一样。
每次退回就是每次的回溯，所以回溯法要保存每一次的状态。
回溯算法也是一种选优搜索法，按照选优条件向前搜索，以达到目标。
但当探索到某一步时，发现原先选择并不优或者达不到目标，就退回一步重新选择，
这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为“回溯点”。
其实就是深度优先搜索的策略，从根结点出发深度搜索。
当探索到某一节点时，要先判断该节点是否包含问题的解，
如果包含，就从该节点出发继续探索下去，若该节点不包含问题的解，则逐层向其祖先节点回溯。
若用回溯法求问题的所有解时，要回溯到根，且跟节点的所有可行的子树都要已被搜索遍才结束。
'''

print(letterCombinations1('23'))

