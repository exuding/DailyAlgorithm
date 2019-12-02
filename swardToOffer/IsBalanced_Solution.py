#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-13 10:49:13 
'''
#输入一棵二叉树，判断该二叉树是否是平衡二叉树。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树
'''
使用获取二叉树深度的方法来获取左右子树的深度
左右深度相减，若大于1返回False
通过递归对每个节点进行判断，若全部均未返回False，则返回True
'''
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        right = self.getDepth(pRoot.right)
        left = self.getDepth(pRoot.left)
        if abs(right-left)>1:
            return False
        return self.IsBalanced_Solution(pRoot.right) and self.IsBalanced_Solution(pRoot.right)
    #返回节点的最大深度
    def getDepth(self,Root):
        if Root is None:
            return 0
        nright = self.getDepth(Root.right)
        nleft = self.getDepth(Root.left)
        return max(nright,nleft)+1

