# DFS和递归
    递归，通常来说一个问题可以分为多个子问题去解决&&问题和求解过程和子问题的求解过程一致&&存在递归终止条件，满足这三个条件就适合用递归
## 101. 对称二叉树
    描述：给定一个二叉树，检查它是否是镜像对称的。
 
    题解：
        左子树和右子相等，也就是说要递归的比较左子树和右子树。
        我们将根节点的左子树记做left，右子树记做right。比较left是否等于right，不等的话直接返回就可以了。
        如果相等，比较left的左节点和right的右节点，再比较left的右节点和right的左节点
        算法的时间复杂度是O(n)，因为要遍历n个节点
        空间复杂度是O(n)，空间复杂度是递归的深度，也就是跟树高度有关，最坏情况下树变成一个链表结构，高度是n。
    class Solution(object):
	    def isSymmetric(self, root):
            if not root:return True
            def dfs(left,right):
                # 递归的终止条件是两个节点都为空
			    # 或者两个节点中有一个为空
			    # 或者两个节点的值不相等
			    if not (left or right):
				    return True
			    if not (left and right):
				    return False
			    if left.val!=right.val:
				    return False
			    return dfs(left.left,right.right) and dfs(left.right,right.left)
            # 用递归函数，比较左节点，右节点
		    return dfs(root.left,root.right)
## 95. 不同的二叉搜索树 II
    描述：
        给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
    示例：
        输入: 3
        输出:
        [
          [1,null,3,2],
          [3,2,null,1],
          [3,1,null,null,2],
          [2,1,3],
          [1,null,2,null,3]
        ]
        解释:
        以上的输出对应以下 5 种不同结构的二叉搜索树：
        
           1         3     3      2      1
            \       /     /      / \      \
             3     2     1      1   3      2
            /     /       \                 \
           2     1         2                 3
    题解：二叉搜索树, 一节点大于左子树节点, 小于右子树节点
        所以我们节点是从1到n,当一个节点为val那么它的左边是<= val,右边是>=val,
        用递归解决
        class Solution:
            def generateTrees(self, n: int) -> List[TreeNode]:
                if n == 0: return []
                def helper(start, end):
                    res = []
                    if start > end:
                        res.append(None)
                    for val in range(start, end + 1):
                        for left in helper(start, val - 1):
                            for right in helper(val + 1, end):
                                root = TreeNode(val)
                                root.left = left
                                root.right = right
                                res.append(root)
                    return res
                return helper(1, n)

## 100. 相同的树
    描述：
        给定两个二叉树，编写一个函数来检验它们是否相同。如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
    题解：
        class Solution:
            def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
                if not p and not q:return True
                def dfs(left,right):
                    # 递归的终止条件是两个节点都为空
                    # 或者两个节点中有一个为空
                    # 或者两个节点的值不相等
                    if not (left or right):
                        return True
                    if not (left and right):
                        return False
                    if left.val!=right.val:
                        return False
                    return dfs(left.left,right.left) and dfs(left.right,right.right)
                return dfs(p,q)
## 104. 二叉树的最大深度
    描述：
        给定一个二叉树，找出其最大深度。二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
    题解：
        递归
        class Solution:
            def maxDepth(self, root: TreeNode) -> int:
                if not root:
                    return 0
                else: 
                    left_height = self.maxDepth(root.left) 
                    right_height = self.maxDepth(root.right) 
                    return max(left_height, right_height) + 1 
        DFS:
        def maxDepth(self, root):
            if(not root):
                return 0
            stack = [(1,root)]
            depth = 0
            # 将(1,root)加入栈后不断遍历栈
            while stack:
                # 首先从栈中弹出元素
                cur_depth,node = stack.pop()
                # 如果弹出的节点不为空
                if node:
                    # 比较这个节点的深度和depth的大小
                    depth = max(cur_depth,depth)
                    # 将 (当前深度+1，left)放入栈中
                    stack.append((cur_depth+1,node.left))
                    # 同理将(当前深度+1,right)放入栈中
                    stack.append((cur_depth+1,node.right))
            return depth
## 687. 最长同值路径
    描述：
        给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
        注意：两个节点之间的路径长度由它们之间的边数表示。
    示例：
        示例 1:
        输入:
        
                      5
                     / \
                    4   5
                   / \   \
                  1   1   5
        输出:2
        示例 2:
        输入:
        
                      1
                     / \
                    4   5
                   / \   \
                  4   4   5
        输出:2
    题解：
        最长的路径可能有三种情况：
        1.在左子树内部
        2.在右子树内部
        3.在穿过左子树，根节点，右子树的一条路径中
        
        class Solution(object):
            def longestUnivaluePath(self, root):
                self.ans = 0
            
                def arrow_length(node):
                    if not node: return 0
                    left_length = arrow_length(node.left)
                    right_length = arrow_length(node.right)
                    left_arrow = right_arrow = 0
                    if node.left and node.left.val == node.val:
                        left_arrow = left_length + 1
                    if node.right and node.right.val == node.val:
                        right_arrow = right_length + 1
                    self.ans = max(self.ans, left_arrow + right_arrow)
                    return max(left_arrow, right_arrow)
            
                arrow_length(root)
                return self.ans
                
## 206. 反转链表
    描述：
        反转单链表
    题解：
        归的条件：
        head.next == None
        说明到尾部了。
        head == None, 是为了处理特殊情况：输入空列表，直接返回
        
        递的操作：
        1.得到尾部节点:p = self.reverseList(head.next)
        2.翻转当前节点：head.next.next = head
        3.拆掉当前节点的next：head.next = None
        class Solution:
            def reverseList(self, head: ListNode) -> ListNode:
                # 归
                if head == None or head.next == None: return head
                # 递
                p = self.reverseList(head.next)
                # 交换当前head 和 head.next
                head.next.next = head
                head.next = None
                return p
    
