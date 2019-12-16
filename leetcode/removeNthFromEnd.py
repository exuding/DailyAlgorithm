#-*- coding:utf-8 -*-
'''
@project: DailyAlgorithm
@author: taoxudong
@time: 2019-12-16 13:46:09 
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    p = head
    count = 1
    while p.next:
        p = p.next
        count += 1
    p = head
    if count <= 1 and n == 1:
        return None
    elif count <= 1 and n == 0:
        return head
    elif count == n:
        head = head.next
        return head
    else:
        for i in range(count - n - 1):
            p = p.next
        p.next = p.next.next
    return head
print(removeNthFromEnd([1],1))


