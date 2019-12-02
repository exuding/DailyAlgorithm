#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-11 18:03:59 
'''
'''
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''
'''
对于根节点，我要求这个节点的最大深度，那么只要求两棵左右子树的最大深度，并且max一下，然后＋1就行了
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#广度优先用队列，深度优先用栈
#层次遍历不可以？
# class Solution:
#     def TreeDepth(self, pRoot):
#         res = []
#         list_tree = [pRoot,]
#         while list_tree:
#             a = list_tree.pop(0)
#             if pRoot.left:
#                 list_tree.append(pRoot.left)
#             elif pRoot.right:
#                 list_tree.append(pRoot.right)
#             res.append(a)
#         return a
#深度优先遍历，python中栈和队列都可以用list实现，list.pop弹出最后一个元素 list.pop(0)弹出第一个元素
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        if pRoot.left == None and pRoot.right == None:
            return 1
        else:
            return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))+1
