# 链表
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
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
                # 这里只做演示，就不搞那么骚气的写法了
                while cur:
                    # 记录当前节点的下一个节点
                    tmp = cur.next
                    # 然后将当前节点指向pre
                    cur.next = pre
                    # pre和cur节点都前进一位
                    pre = cur
                    cur = tmp
                return pre
## 109. 有序链表转换二叉搜索树
    描述：
        给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
        本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
    示例:
        给定的有序链表： [-10, -3, 0, 5, 9],
        一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
              0
             / \
           -3   9
           /   /
         -10  5
    题解：
        快慢指针找中间节点，然后递归生成树：
        class Solution:
            def sortedListToBST(self, head: ListNode) -> TreeNode:
                def findmid(head, tail):
                    slow = head
                    fast = head
                    while fast != tail and fast.next!= tail :
                        slow = slow.next
                        fast = fast.next.next
                    return slow
                
                def helper(head, tail):
                    if  head == tail: return 
                    node = findmid(head, tail)
                    root = TreeNode(node.val)
                    root.left = helper(head, node)
                    root.right = helper(node.next, tail)
                    return root
                    
                return helper(head, None)

        思路一：递归解决：
            当前方法和下一个方法的主要思路是：
            给定列表中的中间元素将会作为二叉搜索树的根，该点左侧的所有元素递归的去构造左子树，
            同理右侧的元素构造右子树。这必然能够保证最后构造出的二叉搜索树是平衡的。
        算法
            由于我们得到的是一个有序链表而不是数组，我们不能直接使用下标来访问元素。我们需要知道链表中的中间元素。
            我们可以利用两个指针来访问链表中的中间元素。假设我们有两个指针 slow_ptr 和 fast_ptr。slow_ptr 每次向后移动一个节点而 fast_ptr 每次移动两个节点。当 fast_ptr 到链表的末尾时 slow_ptr 就访问到链表的中间元素。对于一个偶数长度的数组，中间两个元素都可用来作二叉搜索树的根。
            当找到链表中的中间元素后，我们将链表从中间元素的左侧断开，做法是使用一个 prev_ptr 的指针记录 slow_ptr 之前的元素，也就是满足 prev_ptr.next = slow_ptr。断开左侧部分就是让 prev_ptr.next = None。
            我们只需要将链表的头指针传递给转换函数，进行高度平衡二叉搜索树的转换。所以递归调用的时候，左半部分我们传递原始的头指针；右半部分传递 slow_ptr.next 作为头指针。
      
        class Solution:
            def findMiddle(self, head):
        
                # The pointer used to disconnect the left half from the mid node.
                prevPtr = None
                slowPtr = head
                fastPtr = head
        
                # Iterate until fastPr doesn't reach the end of the linked list.
                while fastPtr and fastPtr.next:
                    prevPtr = slowPtr
                    slowPtr = slowPtr.next
                    fastPtr = fastPtr.next.next
        
                # Handling the case when slowPtr was equal to head.
                if prevPtr:
                    prevPtr.next = None
        
                return slowPtr
        
            def sortedListToBST(self, head):
                """
                :type head: ListNode
                :rtype: TreeNode
                """
        
                # If the head doesn't exist, then the linked list is empty
                if not head:
                    return None
        
                # Find the middle element for the list.
                mid = self.findMiddle(head)
        
                # The mid becomes the root of the BST.
                node = TreeNode(mid.val)
        
                # Base case when there is just one element in the linked list
                if head == mid:
                    return node
        
                # Recursively form balanced BSTs using the left and right halves of the original list.
                node.left = self.sortedListToBST(head)
                node.right = self.sortedListToBST(mid.next)
                return node

        当前做法的主要问题是找到中间元素，由于链表的数据结构导致花费了很多额外时间，下面的方法可以尝试解决这一问题。
        方法 2：递归 + 转成数组
            这个方法是空间换时间的经典案例。
            你可以通过使用更多空间来降低时间复杂度。
            在这个方法中，我们将给定的链表转成数组并利用数组来构建二叉搜索树。
            数组找中间元素只需要 O(1)O(1) 的时间，所以会降低整个算法的时间复杂度开销。
        算法：
            将给定链表转成数组，将数组的头和尾记成 left 和 right 。
            找到中间元素 (left + right) / 2，记为 mid。这需要 O(1)O(1) 时间开销，也是与上面算法主要改进的地方。
            将中间元素作为二叉搜索树的根。
            递归构造二叉搜索树的左右两棵子树，两个子数组分别是 (left, mid - 1) 和 (mid + 1, right)。

        class Solution:
            # Convert the given linked list to an array
            def mapListToValues(self, head):
                vals = []
                while head:
                    vals.append(head.val)
                    head = head.next
                return vals    
        
            def sortedListToBST(self, head):
                """
                :type head: ListNode
                :rtype: TreeNode
                """
        
                # Form an array out of the given linked list and then
                # use the array to form the BST.
                values = self.mapListToValues(head)
        
                # l and r represent the start and end of the given array
                def convertListToBST(l, r):
        
                    # Invalid case
                    if l > r:
                        return None
        
                    # Middle element forms the root.
                    mid = (l + r) // 2
                    node = TreeNode(values[mid])
        
                    # Base case for when there is only one element left in the array
                    if l == r:
                        return node
        
                    # Recursively form BST on the two halves
                    node.left = convertListToBST(l, mid - 1)
                    node.right = convertListToBST(mid + 1, r)
                    return node
                return convertListToBST(0, len(values) - 1)
        方法 3：中序遍历模拟
            我们知道，二叉树有三种不同的遍历方法： 
            前序遍历 中序遍历 和 后序遍历。
            中序遍历一棵二叉搜索树会有一个非常有趣的结论。
            中序遍历一棵二叉搜索树的结果是得到一个升序序列。
            这个方法模拟了二叉搜索树的构造过程，因为我们已经获得有序的链表，所以自然的产生了这样的想法。
            在描述算法之前，先看一下中序遍历是如何获得有序值的。
            基于解决这个问题的中序遍历的思想：
            我们知道中序遍历最左边的元素一定是给定链表的头部，类似地下一个元素一定是链表的下一个元素，以此类推。
            这是肯定的因为给定的初始链表保证了升序排列。
            在了解了中序遍历二叉搜索树和有序数组的关系之后，让我们来看看算法。

            算法
            首先用伪代码来理解一下算法。
            
            ➔ function formBst(start, end)
            ➔      mid = (start + end) / 2
            ➔      formBst(start, mid - 1)
            ➔
            ➔      TreeNode(head.val)
            ➔      head = head.next
            ➔       
            ➔      formBst(mid + 1, end)
            遍历整个链表获得它的长度，我们用两个指针标记结果数组的开始和结束，记为 start 和 end，他们的初始值分别为 0 和 length - 1。
            记住，我们当前需要模拟中序遍历，找到中间元素 (start + end) / 2。注意这里并不需要在链表中找到确定的元素是哪个，只需要用一个变量告诉我们中间元素的下标。我们只需要递归调用这两侧。
            递归左半边，其中开始和结束的值分别为 start, mid - 1。
            在这个算法中，每当我们构建完二叉搜索树的左半部分时，链表中的头指针将指向根节点或中间节点（它成为根节点）。 因此，我们只需使用头指针指向的当前值作为根节点，并将指针后移一位，即 head = head.next。
            我们在递归右半部分 mid + 1, end。
            class Solution:
                def sortedListToBST(self, head: ListNode) -> TreeNode:
                    size = 0
                    p = head
                    while p:
                        size += 1
                        p = p.next
            
                    def rebuildTree(l, r):
                        #nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量
                        nonlocal head
                        if l >= r:
                            return None
                        
                        mid = (l+r)//2
            
                        left = rebuildTree(l, mid)
                        root = TreeNode(head.val)
                        root.left = left
                        
                        head = head.next
            
                        root.right = rebuildTree(mid+1, r)
            
                        return root
            
                    return rebuildTree(0 ,size)
##  160.相交链表
    描述：
        编写一个程序，找到两个单链表相交的起始节点。
    题解：
        链表中可能有重复值的节点，但是要特别注意，我们考虑节点是否相同就可以，节点还包括节点的内存地址呢。
    代码：
        法一：hash方法
        class Solution(object):
            def getIntersectionNode(self, headA, headB):
                """
                :type head1, head1: ListNode
                :rtype: ListNode
                """
                all_A = set()
                while headA:
                    all_A.add(headA)
                    headA = headA.next
                while headB and headB not in all_A:
                    headB = headB.next
                if headB: return headB
                return None
        法二：计算长度，先走差值，求是否相遇
        class Solution(object):
            def getIntersectionNode(self, headA, headB):
                """
                :type head1, head1: ListNode
                :rtype: ListNode
                """
                headA_len = 0
                headB_len = 0
                p_A = headA
                p_B = headB
                # 求出headA, headB的长度
                while p_A or p_B:
                    if p_A:
                        headA_len += 1
                        p_A = p_A.next
                    if p_B:
                        headB_len += 1
                        p_B = p_B.next
                def helper(headA, headB, headA_len, headB_len):
                    diff = headB_len - headA_len
                    p_A = headA
                    p_B = headB
                    # 长链表先走差值
                    while diff:
                        diff -= 1
                        p_B = p_B.next
                    # 连个链表一起走
                    while p_B and p_A:
                        if p_A == p_B:
                            return p_A
                        p_A = p_A.next
                        p_B = p_B.next
                    return None
                # 保持headA链表长度小于headB的链表长度
                if headB_len < headA_len :
                    return helper(headB, headA, headB_len , headA_len)
                return helper(headA, headB, headA_len, headB_len)
        法三：a+b+all = b+a+all 结尾处换路然后考虑是否相遇wwre
        class Solution(object):
            def getIntersectionNode(self, headA, headB):
                """
                :type head1, head1: ListNode
                :rtype: ListNode
                """
                if not headA or not headB: return 
                pa = headA
                pb = headB
                while pa != pb:
                    pa = pa.next if pa else headB
                    pb = pb.next if pb else headA
                return pa
        
##   1.两数相加：
    题解：
        要有一个carry计算每次进位不进位，新链表设置两个头节点和尾节点，如果要进位插入的话，node.val怎么赋予的也很有讲究
    class Solution:
        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            head = None # 链表头
            tail = None # 链表尾部，方便插入的时候不需要遍历
            carry = 0
            while l1 or l2:
                l1_v = l1.val if l1 else 0
                l2_v = l2.val if l2 else 0
                val = l1_v + l2_v + carry
                carry = val // 10
                val = val % 10

                node = ListNode(val)
                if not head:
                    head = node
                    tail = head
                else:
                    tail.next = node
                    tail = node
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next

            if carry>0:
                tail.next = ListNode(1)
            return head




