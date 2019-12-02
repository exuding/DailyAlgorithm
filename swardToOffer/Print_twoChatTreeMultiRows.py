#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-25 08:26:00 
'''
#从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return 0
        DataQueue = [pRoot,]
        tempQueue = []
        res = []
        #需要两个变量：一个变量表示在当前层中还没有打印的节点数；另一个变量表示下一层节点的数目。
        numOfThisLine = 1
        numOfNextLine = 0
        while len(DataQueue)>=1:
            tempNode = DataQueue.pop(0)
            tempQueue.append(tempNode.val)
            numOfThisLine = numOfThisLine -1
            if tempNode.left:
                DataQueue.append(tempNode.left)
                numOfNextLine = numOfNextLine +1
            if tempNode.right:
                DataQueue.append(tempNode.right)
                numOfNextLine = numOfNextLine + 1
            if numOfThisLine == 0:
                res.append(tempQueue)
                tempQueue = []
                numOfThisLine = numOfNextLine
                numOfNextLine = 0
        return res
