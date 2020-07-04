#_*_coding:utf-8_*_
'''
@project: DailyAlgorithm
@author: exudingtao
@time: 2019/12/19 10:26 上午
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeKLists(self,lists):
        if not lists: return
        n = len(lists)
        return self.merge(lists, 0, n - 1)


    def merge(self, lists, left, right):
        if left == right:#递归停止
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)



    def mergeTwoLists(l1, l2):
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