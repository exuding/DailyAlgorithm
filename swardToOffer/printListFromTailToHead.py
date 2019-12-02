#-*- coding:utf-8 -*-
'''
@project: Exuding
@author: taoxudong
@time: 2019-08-02 09:40:40 
'''
#输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        res = []
        if listNode:
            #链表不为空，并且当前节点有子节点
            while listNode.next:
                res.append(listNode.val)
                listNode = listNode.next
            res.append(listNode.val)
        else:
            return []
        #return res.pop()
        return res[::-1]