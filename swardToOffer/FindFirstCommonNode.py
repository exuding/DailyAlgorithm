#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-11 15:12:06 
'''
'''
输入两个链表，找出它们的第一个公共结点
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#暴力解法
# class Solution:
#     def FindFirstCommonNode(self, head1, head2):
#         # write code here
#         list1 = []
#         list2 = []
#         node1 = head1
#         node2 = head2
#         while node1:
#             list1.append(node1.val)
#             node1 = node1.next
#         while node2:
#             if node2.val in list1:
#                 return node2
#             else:
#                 node2 = node2.next

#利用额外空间，利用栈结构从尾节点往前找
# class Solution:
#     def FindFirstCommonNode(self, pHead1, pHead2):
#         if not pHead1 or not pHead2:
#             return None
#
#         stack1 = []
#         stack2 = []
#
#         while pHead1:
#             stack1.append(pHead1)
#             pHead1 = pHead1.next
#
#         while pHead2:
#             stack2.append(pHead2)
#             pHead2 = pHead2.next
#
#         first = None
#         while stack1 and stack2:
#             top1 = stack1.pop()
#             top2 = stack2.pop()
#             if top1 is top2:
#                 first = top1
#             else:
#                 break
#         return first
#通过长度设定 先走后走巧妙解法
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        def GetListLength(pHead):
            length = 0
            pNode = pHead
            while pNode != None:
                length += 1
                pNode = pNode.next
            return length

        def GoStep(node, k):
            while k != 0:
                node = node.next
                k = k - 1
            return node

        length1 = GetListLength(pHead1)
        length2 = GetListLength(pHead2)
        lengthDif = abs(length1 - length2)
        if length1 >= length2:
            pHead1 = GoStep(pHead1, length1 - length2)
            pListHeadLong = pHead1
            pListHeadShort = pHead2
            # lengthDif = length1 - length2
        elif length2 > length1:
            pHead2 = GoStep(pHead2, length1 - length2)
            pListHeadLong = pHead2
            pListHeadShort = pHead1
            # lengthDif = length2 - length1
        # for i in range(lengthDif):
        #    pListHeadLong = pListHeadLong.next
        while (pListHeadLong != None) and (pListHeadShort != None) and (pListHeadLong != pListHeadShort):
            pListHeadLong = pListHeadLong.next
            pListHeadShort = pListHeadShort.next
        pFirstCommonNode = pListHeadLong
        return pFirstCommonNode

