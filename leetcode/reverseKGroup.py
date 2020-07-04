#_*_coding:utf-8_*_
'''
@project: DailyAlgorithm
@author: exudingtao
@time: 2019/12/21 5:57 下午
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#递归详解的
#https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/di-gui-si-wei-ru-he-tiao-chu-xi-jie-by-labuladong/
#反转以a为链表头的节点
def reverse(a):
    pre = ListNode(0)
    cur = a
    while cur:
        nxt = cur.next
        #逐个结点反转
        cur.next = pre
        #更新指针位置
        pre = cur
        cur = nxt
    #返回反转后的头结点
    return pre
#反转以 a 为头结点的链表」其实就是「反转 a 到 null 之间的结点」，那么如何「反转 a 到 b 之间的结点」？
#反转区间 [a, b) 的元素，注意是左闭右开
def reverse(a,b):
    pre = ListNode(0)
    cur = a
    while cur != b:#把节点改为b即可
        nxt = cur.next
        #逐个结点反转
        cur.next = pre
        #更新指针位置
        pre = cur
        cur = nxt
    #返回反转后的头结点
    return pre
####递归
class Solution:
    def reverseKGroup(self, head, k):
        if not head:
            return None
        #区间 [a, b) 包含 k 个待反转元素
        a = b = head
        for i in range(k):
            #不足 k 个，不需要反转，base case
            if b == None:
                return head
            b = b.next
        #反转前 k 个元素
        newHead = self.reverse(a, b)
        #递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k)
        return newHead

    def reverse(self,a,b):
        pre = ListNode(0)
        cur = a
        while cur != b:#把节点改为b即可
            nxt = cur.next
            #逐个结点反转
            cur.next = pre
            #更新指针位置
            pre = cur
            cur = nxt
        #返回反转后的头结点
        return pre

