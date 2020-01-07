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
