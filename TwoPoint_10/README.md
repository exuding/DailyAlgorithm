# 双指针法解题
    
## 206. 反转链表
    描述：
        反转单链表
    题解：
        class Solution(object):
            def reverseList(self, head):
                """
                :type head: ListNode
                :rtype: ListNode
                """
                # 申请两个节点，pre和 cur，pre指向None
                pre = None
                cur = head
                # 遍历链表，while循环里面的内容其实可以写成一行
                while cur:
                    # 记录当前节点的下一个节点
                    tmp = cur.next
                    # 然后将当前节点指向pre     这句话很牛逼 让后面的指向前面  链表操作不是是有a = b.next 直接 b.next = a
                    cur.next = pre
                    # pre和cur节点都前进一位
                    pre = cur
                    cur = tmp
                return pre	
                
## 面试题 10.01. 合并排序的数组
    描述：
        给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
        初始化 A 和 B 的元素数量分别为 m 和 n。
    示例:
        输入:
        A = [1,2,3,0,0,0], m = 3
        B = [2,5,6],       n = 3
        输出: [1,2,2,3,5,6]
    题解：
        从后往前插入   注意-1是啥意思
        class Solution:
            def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
                """
                Do not return anything, modify A in-place instead.
                """
                pa = m-1
                pb = n-1
                tail = n+m-1
                while pa >= 0 or pb >= 0:
                    if pa == -1 :
                        A[tail] = B[pb]
                        pb = pb - 1
                    elif pb == -1:
                        A[tail] = A[pa]
                        pa = pa - 1
                    elif A[pa] < B[pb]:
                        A[tail] = B[pb]
                        pb = pb - 1
                    else:
                        A[tail] = A[pa]
                        pa = pa - 1
                    tail = tail - 1
