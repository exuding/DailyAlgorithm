#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-27 15:27:11 
'''
#请实现两个函数，分别用来序列化和反序列化二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    #序列化 将二叉树转化为字符串表示
    def Serialize(self, root):
        if not root:
            return '#'
        #先序遍历
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
    #反序列化 将字符串转化为二叉树表示
    def Deserialize(self, s):
        list = s.split(',')
        return self.deserializeTree(list)

    def deserializeTree(self, list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.deserializeTree(list)
            root.right = self.deserializeTree(list)
        return root