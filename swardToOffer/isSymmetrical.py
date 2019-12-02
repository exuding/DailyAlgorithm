#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-20 14:33:13 
'''
'''
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot is None:
            return True
        if pRoot.left is None and pRoot.right is None:
            return True
        # 不止一个根节点

        return self.judge(pRoot.left, pRoot.right)

    def judge(self, right, left):
        # 同时为空
        if right == None and left == None:
            return True
        # 一个为空，另一个不为空，则认为不对称
        if right == None or left == None:
            return False
        # 对称结点不相等，认为错误
        if right.val != left.val:
            return False
        # 对称结点相等，考虑它们的下一层结点，注意（右结点的右孩子——左结点的左孩子，右结点的左孩子——左结点的右孩子）
        if right.val == left.val:
            return self.judge(right.right, left.left) and self.judge(right.left, left.right)

