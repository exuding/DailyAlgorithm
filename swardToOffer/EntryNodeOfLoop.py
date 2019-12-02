#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-18 14:58:59 
'''
#给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#方法一
'''
第一步  找环中相汇点。分别用p1，p2指向链表头部.
       p1每次走一步，p2每次走二步，直到p1==p2找到在环中的相汇点。
第二步  找环的入口。
       接上步，当p1==p2时，p2所经过节点数为2x,p1所经过节点数为x.
       设环中有n个节点,p2比p1多走一圈有2x=n+x; n=x;  ？？不一定多走一圈？？
       可以看出p1实际走了一个环的步数，再让p2指向链表头部.
       p1位置不变，p1,p2每次走一步直到p1==p2; 此时p1指向环的入口。
'''

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow,fast=pHead,pHead
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow2=pHead
                while slow!=slow2:
                    slow=slow.next
                    slow2=slow2.next
                return slow
#方法二
'''
时间复杂度为O（n），两个指针，一个在前面，另一个紧邻着这个指针，在后面。
两个指针同时向前移动，每移动一次，前面的指针的next指向NULL。
也就是说：访问过的节点都断开，最后到达的那个节点一定是尾节点的下一个，
也就是循环的第一个。
这时候已经是第二次访问循环的第一节点了，第一次访问的时候我们已经让它指向了NULL，
所以到这结束。
*****但是破坏了链表，并且没有环的链表需要判断
'''
#方法三 运用数据结构存储的时候一些对象存储解决
#
# class Solution:
#     def EntryNodeOfLoop(self, pHead):
#         stack = []
#         while pHead:
#             stack.append(pHead)
#             pHead = pHead.next
#             if pHead in stack:
#                 return pHead
#         return

