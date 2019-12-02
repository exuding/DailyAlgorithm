#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-18 15:48:23 
'''
'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# class Solution:
#     #1111解决不了 为了解决这个1233445设计的思路
#     def deleteDuplication(self, pHead):
#         # write code here
#         pre =pHead
#         cur = pHead.next
#         flag = 0
#         #1
#         if cur==None:
#             return pHead
#         #1,1,1,1,1,1,2
#         if pre.val == cur.val:
#             flag1 = 1
#         else:
#             flag1 = 0
#         while cur.next:
#             if cur.val != cur.next.val and flag == 0:
#                 pre = pre.next
#                 cur = cur.next
#             else:
#                 if cur.val == cur.next.val:
#                     cur = cur.next
#                     flag = 1
#                 else:
#                     flag = 0
#                     pre.next = cur.next
#                     cur = pre.next
#         if flag1==1:
#             pHead = pHead.next
#             return pHead
#         else:
#             return pHead
class Solution:
    #1111解决不了 设置头节点
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        head = ListNode(0)
        head.next = pHead
        pre =head
        cur = head.next

        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val==cur.next.val:
                    cur = cur.next
                pre.next = cur.next
                cur = pre.next
            else:
                pre = pre.next
                cur = cur.next
        return head.next

s = ListNode(1)
s.next= ListNode(1)
s.next.next = ListNode(1)
ss = Solution()
a = ss.deleteDuplication(s)
print(a)
