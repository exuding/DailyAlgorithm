import leetcode.twoCharTress as Node
class MyLinkedList(object):
    """单链表"""

    def __init__(self):
        self._head = None
        self.length = 0

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    # def length(self):
    #     """链表长度"""
    #     # cur初始时指向头节点
    #     cur = self._head
    #     count = 0
    #     # 尾节点指向None，当未到达尾部时
    #     while cur != None:
    #         count += 1
    #         # 将cur后移一个节点
    #         cur = cur.next
    #     return count

    def get(self, index):
        if index < 0 or index >= self.length:
            return -1
        else:

            cur = self._head
            cnt = 0
            while cur:
                if index == cnt:
                    return cur.val
                else:
                    cnt += 1
                    cur = cur.next

    def addAtHead(self, val):
        """头部添加元素"""
        # 先创建一个保存val值的节点
        node = Node(val)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node
        self.length += 1

    def addAtTail(self, val):
        """尾部添加元素"""
        node = Node(val)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.length += 1

    def addAtIndex(self, index, val):
        """指定位置添加元素"""
        # 若指定位置index为第一个元素之前，则执行头部插入
        if index <= 0:
            self.addAtHead(val)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif index > (self.length - 1):
            self.addAtTail(val)
        # 找到指定位置
        else:
            node = Node(val)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            while count < (index - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node
            self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        node = Node(0)
        if index <= 0 or index >= self.length:
            return -1
        else:
            cur = self._head
            pre = None
            cnt = 0
            while cnt < index:
                pre = cur
                cnt += 1
                cur = cur.next
            pre.next = cur.next
            self.length -= 1

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def initlist(self, data):

        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.val)
            cur = cur.next
        print("")
