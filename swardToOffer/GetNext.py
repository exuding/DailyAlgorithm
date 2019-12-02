#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-19 09:01:16 
'''
'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
# class Solution:
#     def GetNext(self, pNode):
#         #整棵树的跟节点
#         if pNode.next == None:
#             tempNode = pNode.right
#             while tempNode.left:
#                 tempNode = tempNode.left
#
#             nextNode = tempNode
#             return  nextNode
#         else:
#             ####子节点情况
#             # 左右都不为空
#             if pNode.left != None and pNode.right != None:
#                 nextNode = pNode.right
#             #左为空，右不为空
#             if pNode.left == None and pNode.right != None:
#                 nextNode = pNode.right
#             #左不为空，右为空
#             if pNode.left != None and pNode.right == None:
#                 nextNode = pNode.next
#             #左右都为空
#             if pNode.left == None and pNode.right == None:
#                 if pNode.next.left == pNode:
#                     nextNode = pNode.next
#                 else:
#                     nextNode = pNode.next.next
#
#             return  nextNode
'''
分成两大类  1、有右子树的，那么下个结点就是右子树最左边的点；
           2、没有右子树的，也可以分成两类，
           a)是父节点左孩子 ，那么父节点就是下一个节点 ； 
           b)是父节点的右孩子找他的父节点的父节点的父节点...
             直到当前结点是其父节点的左孩子位置。如果没有eg：M，那么他就是尾节点。
'''
class Solution:
    def GetNext(self, pNode):
        if pNode == None:
            return None
        #有右边子树的   如果有右子树，则找右子树的最左节点
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return  pNode
        #没右子树，则找第一个当前节点是父节点左孩子的节点
        while pNode.next:
            if pNode.next.left == pNode:
                return pNode.next
            else:
                pNode = pNode.next
        #退到了根节点仍没找到，说明是最右端的结点  则返回None
        return None
