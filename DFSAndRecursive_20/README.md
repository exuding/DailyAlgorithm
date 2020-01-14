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


