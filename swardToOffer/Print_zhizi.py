#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-20 15:14:14 
'''
'''
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
解法：
利用一个标志变量flag来标记从左往右还是从右往走
如果从左往右，那就从头到尾遍历当前层的节点current_nodes，然后将左孩子和右孩子分别append到一个list new_nodes中
如果从右往前，那就从尾到头遍历当前层的节点current_nodes，然后将右孩子和左孩子分别insert到一个list new_nodes中
这样得到的new_nodes还是从左到右有序的
'''
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        falg = 0 # 0表示从左往右，1表示从右往左
        node_list = [[pRoot]]
        result = []
        while node_list:
            current_nodes = node_list[0] # 当前层的节点
            node_list = node_list[1:]
            new_nodes = [] # 下一层的节点，按照从左往右的顺序存储
            res = [] # 当前层得到的输出
            while len(current_nodes) > 0:
                # 从左往右
                if falg == 0:
                    res.append(current_nodes[0].val)
                    if current_nodes[0].left != None:
                        new_nodes.append(current_nodes[0].left)
                    if current_nodes[0].right != None:
                        new_nodes.append(current_nodes[0].right)
                    current_nodes = current_nodes[1:]
                # 从右往左
                else:
                    res.append(current_nodes[-1].val)
                    if current_nodes[-1].right != None:
                        new_nodes.insert(0, current_nodes[-1].right)
                    if current_nodes[-1].left != None:
                        new_nodes.insert(0, current_nodes[-1].left)
                    current_nodes = current_nodes[:-1]
            result.append(res)
            falg = 1 - falg
            if new_nodes:
                node_list.append(new_nodes)
        return result