#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-07-02 09:05:53 
'''
'''
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        #中序遍历极为二叉搜索树从小到大的排序
        res = []
        res_sort = self.midErgodic(pRoot,res)
        if res_sort:
            return res_sort[k-1] if 0<k<=len(res_sort) else None
        else:
            return None

    def midErgodic(self,pRoot,res):
        if not pRoot:
            return None
        if pRoot.left:
            res = self.midErgodic(pRoot.left,res)
        res.append(pRoot)
        if pRoot.right:
            res = self.midErgodic(pRoot.right,res)
        return res
        # self.midErgodic(pRoot.left)
        # self.res.append(pRoot)
        # self.midErgodic(pRoot.right)
