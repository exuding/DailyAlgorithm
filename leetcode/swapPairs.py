#_*_coding:utf-8_*_
'''
@project: DailyAlgorithm
@author: exudingtao
@time: 2019/12/21 3:47 下午
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#原地转换解法，一个第三方节点，两个指针
class Solution:
    def swapPairs(head):
        if not head or not head.next:
            return head
        end = ListNode(0)    # end初始化为头结点
        res = head.next    # 返回结果首节点
        pre, cur = head, head.next    # 当前要交换的前节点，后节点
        while cur:
            tmp = cur.next
            end.next = cur
            cur.next = pre
            end = pre#两个要交换的节点的前一个节点又作为了头节点
            if not tmp:    # 节点数为偶数的结束条件
                end.next = None
                break
            pre = tmp
            cur = tmp.next
        if not cur:    # 节点数为奇数的处理
            end.next = pre#end作为第三方势力周璇
        return res

#递归
    def swapPairs1(head):
        if not head or not head.next:
            return head
        p = head.next
        head.next = swapPairs(p.next)
        p.next = head
        return p  # p 才是新的头
