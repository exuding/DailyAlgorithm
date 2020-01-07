# BFS和拓扑排序

## 102. 二叉树的层次遍历
    描述：给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）
    例子：给定二叉树: [3,9,20,null,null,15,7] 返回其层次遍历结果：
    [
      [3],
      [9,20],
      [15,7]
    ]
    题解：BFS-注意用cur_level和next_level  其实就是用cur_level代替以前的pop()最后一个 list代替节点
    class Solution:
        def levelOrder(self, root: TreeNode) -> List[List[int]]:
            if not root:return []
            res = []
            cur_level = [root]
            while cur_level:
                temp = []
                next_level = []
                for node in cur_level:#遍历一层的节点
                    temp.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                cur_level = next_level
                res.append(temp)
            return res
## 103. 二叉树的锯齿形层次遍历
    描述：给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）
    例子：给定二叉树 [3,9,20,null,null,15,7],返回锯齿形层次遍历如下：
    [
      [3],
      [20,9],
      [15,7]
    ]
    题解：判断是奇数行还是偶数行 和102几乎一样
    class Solution:
        def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
            if not root: return []
            res = []
            cur_level = [root]
            count = 1
            while cur_level:
                temp = []
                next_level = []
                for node in cur_level:
                    temp.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                if count%2 ==1:#奇数行
                    res.append(temp)
                else:
                    res.append(temp[::-1])
                count+=1
                cur_level = next_level
            return res
## 101. 对称二叉树
    描述：给定一个二叉树，检查它是否是镜像对称的。
 
    题解：
        首先从队列中拿出两个节点(left和right)比较
        将left的left节点和right的right节点放入队列
        将left的right节点和right的left节点放入队列
        时间复杂度是O(n)，空间复杂度是O(n)

    class Solution(object):
        def isSymmetric(self, root):
            if not root or not (root.left,root.right):
                return True
            #用队列保存节点
            queue = [root.left,root.right]
            while queue:
                # 从队列中取出两个节点，再比较这两个节点
                left = queue.pop()
                right = queue.pop()
                # 如果两个节点都为空就继续循环，两者有一个为空就返回false
                if not (left or right):
                    continue
                if not (left and right):
                    return False
                if left.val!=right.val:
                    return False
                # 将左节点的左孩子， 右节点的右孩子放入队列
                queue.append(left.left)
                queue.append(right.right)
                # 将左节点的右孩子，右节点的左孩子放入队列
                queue.append(left.right)
                queue.append(right.left)
            return True
## 107.二叉树的层次遍历2
    描述：
        给定一个二叉树，返回其节点值自底向上的层次遍历。（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
    题解：
    class Solution:
        def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
            if not root:return []
            cur_level = [root]
            res = []
            while cur_level:
                temp = []
                next_level = []
                for node in cur_level:
                    temp.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                cur_level = next_level
                res.append(temp)
            return res[::-1]
## 111. 二叉树的最小深度
    描述：给定一个二叉树，找出其最小深度，最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
    题解：当前层和下一层的用法，但是要格外注意判断左右子树是否存在时的if elif的使用
    class Solution:
        def minDepth(self, root: TreeNode) -> int:
            if not root:return 0
            cur_level = [root]
            count = 0
            while cur_level:
                count+=1
                next_level = []
                for node in cur_level:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                    if not (node.left or node.right):
                        return count
                cur_level = next_level
            
                    