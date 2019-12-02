#-*- coding:utf-8 -*-
'''
@project: leetcode
@author: taoxudong
@time: 2019-11-27 15:20:16 
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #为新链表插入做准备，要学习
        head = None  # 链表头
        tail = None  # 链表尾部，方便插入的时候不需要遍历
        carry = 0
        while l1 or l2:#这样不用判断谁最长，只考虑节点是否为空
            l1_v = l1.val if l1 else 0 #没了就赋值为0，否则取节点的值
            l2_v = l2.val if l2 else 0 #没了就赋值为0，否则取节点的值
            val = l1_v + l2_v + carry
            carry = val // 10#这种方式要学习 不需要if>10判断
            val = val % 10

            node = ListNode(val)#链表赋值和c不太一样
            ###根绝指针操作逐渐添加链表节点
            if not head:
                head = node
                tail = head
            else:
                tail.next = node
                tail = node
            #一直以节点有无作为判断，有就指向下一个节点
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        #考虑同长度最后进一位情况，容易忘
        if carry > 0:
            tail.next = ListNode(1)
        return head

