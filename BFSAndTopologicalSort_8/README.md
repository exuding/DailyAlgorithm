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
## 127.单词接龙
    