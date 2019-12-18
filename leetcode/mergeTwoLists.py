#_*_coding:utf-8_*_
'''
@project: DailyAlgorithm
@author: exudingtao
@time: 2019/12/18 11:39 上午
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    l3 = ListNode(-1)
    temp = l3
    while l1 or l2:
        if l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        elif l1:
            temp.next = l1
            temp = temp.next
            l1 = l1.next
        else:
            temp.next = l2
            temp = temp.next
            l2 = l2.next

    return l3.next#头节点是-1 不输出
#改进一下
def mergeTwoLists1(l1, l2):
    l3 = ListNode(-1)
    temp = l3
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    temp.next = l1 if l1 is not None else l2
    return l3.next

