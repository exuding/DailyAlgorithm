# 树
    
## 623. 在二叉树中增加一行
    描述：
        给定一个二叉树，根节点为第1层，深度为 1。在其第 d 层追加一行值为 v 的节点。
        添加规则：给定一个深度值 d （正整数），针对深度为 d-1 层的每一非空节点 N，为 N 创建两个值为 v 的左子树和右子树。
        将 N 原先的左子树，连接为新节点 v 的左子树；将 N 原先的右子树，连接为新节点 v 的右子树。
        如果 d 的值为 1，深度 d - 1 不存在，则创建一个新的根节点 v，原先的整棵树将作为 v 的左子树。
    示例 
        1:
        输入: 
            二叉树如下所示:
                   4
                 /   \
                2     6
               / \   / 
              3   1 5   
            
            v = 1
            
            d = 2  
        输出: 
                   4
                  / \
                 1   1
                /     \
               2       6
              / \     / 
             3   1   5  

    题解：
        class Solution:
            def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
                add_v_node = TreeNode(v)
                count = 1
                if d == 1:
                    add_v_node.left = root
                    return add_v_node
        
                cur_level = [root]
                while cur_level:
                    if count != d-1:
                        next_level = []
                        for node in cur_level:
                            if node.left:
                                next_level.append(node.left)
                            if node.right:
                                next_level.append(node.right)
                        cur_level = next_level
                        count+=1
                    else:
                        for node in cur_level:
                            add_v_node2 = TreeNode(v)
                            add_v_node1 = TreeNode(v)
                            if node.left:
                                temp = node.left
                                node.left = add_v_node1
                                add_v_node1.left = temp
                            else:
                                node.left = add_v_node1
                            if node.right:
                                temp = node.right
                                node.right = add_v_node2
                                add_v_node2.right = temp
                            else:
                                node.right = add_v_node2
                        break
                return root
        
## 863. 二叉树中所有距离为 K 的结点
    描述：
        给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
        返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
    例子：
        示例 1：
            输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
            输出：[7,4,1]
            解释：
            所求结点为与目标结点（值为 5）距离为 2 的结点，
            值分别为 7，4，以及 1
    提示：
        给定的树是非空的，且最多有 K 个结点。
        树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
        目标结点 target 是树上的结点。
        0 <= K <= 1000.
    题解：
        class Solution:
            def distance(self,x0,y0,x1,y1):# 根据两个节点的坐标计算距离
                res = 0
                # 如果两个节点不在同一层 # 首先让layer较大的节点,即较低的节点上移，变成其父节点
                # 对于任意节点，x,y 其父节点坐标为 x-1,y//2
                # 相应地，距离+1
                while x0 > x1:                                
                    x0 -= 1
                    y0 //= 2
                    res += 1
                while x0 < x1:
                    x1 -= 1
                    y1 //= 2
                    res += 1
                while y0 != y1:
                # 当两节点处于同一层时 需要比较其pos
                # 当pos相等时，两节点即重合 否则两个节点同步上移
                # 由于其layer相等，只需考虑pos
                # 对于任意 pos=y 的节点而言
                # 其父节点pos = y//2
                # 每次上移，距离+2
                    y0 //= 2
                    y1 //= 2
                    res += 2
                return res
        
            def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
                node_val = {}                                # 用于记录节点的坐标和值的对应关系
                cur_level = [(0,0,root)]                         # 层序遍历的队列，（0,0）为根的坐标
                x,y = 0,0                                    # 记录目标值所对应坐标
                while cur_level:
                    nex_level = []
                    for item in cur_level:
                        layer,pos,node = item            # 队列弹出的值分别为层数、位置和节点
                        node_val[(layer,pos)] = node.val # 记录节点的坐标和值的对应关系# 即二叉树的坐标化
                        if node == target:           # 找到并记录target对应的节点坐标
                            x = layer
                            y = pos
                        if node.left:   # 如果节点有左节点 # layer = layer + 1 # pos = pos * 2
                            nex_level.append((layer+1,pos*2,node.left))
                        if node.right: # 如果节点有右节点  # layer = layer + 1 # pos = pos * 2 + 1       
                            nex_level.append((layer+1,pos*2+1,node.right))
                    cur_level = nex_level
                #利用distance函数 # 计算所有节点与target节点的距离 # 并返回距离为K的节点值
                return [node_val[p] for p in node_val if self.distance(p[0],p[1],x,y)==K]
                
## 894. 所有可能的满二叉树
    描述：
        满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。
        返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。
        答案中每个树的每个结点都必须有 node.val=0。
        你可以按任何顺序返回树的最终列表。
    示例：
        输入：7
        输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

    题解：
        思路
        如果你要构造一颗有 N 个节点的二叉树，你会怎么做？
        首先，你肯定会先 new 一个根结点对象 root，然后为它构造左子树，再为它构造右子树。
        那么对它的左子树 root.left 而言，它同样需要构造左子树和右子树。右子树 root.right 亦然。
        因此，你的所有子树都是一棵满二叉树。
        
        「给你一个整数 N，构造出一棵包含 N 个节点的满二叉树」。这句话是题目本身，也是无数个被拆分出的子问题。
        满二叉树如何构造？
        满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。
        如果你要为某节点分配一个左节点，那么一定也要为它分配一个右节点。因此，如果 N 为偶数，那一定无法构成一棵满二叉树。
        ####关键######
        为了列出所有满二叉树的排列，我们可以为左子树分配 x 节点，为右子树分配 N - 1 - x（其中减 1 减去的是根节点）节点，然后递归地构造左右子树。
        x 的数目从 1 开始，每次循环递增数目 2（多增加 2 个节点，等于多增加 1 层）。

        递归过程
        递归最关心的两个问题是：
        
        结束条件
        自身调用
        对于这个问题来说，结束条件为：
        
        当 N 为偶数时：无法构造满二叉树，返回空数组
        当 N == 1 时：树只有一个节点，直接返回包含这个节点的数组
        当完成 N 个节点满二叉树构造时：返回结果数组
        当需要构造左右子树时，就进行自身调用。具体的看代码吧~

    class Solution:
        # 子问题：构造一棵满二叉树
        def allPossibleFBT(self, N: int) -> List[TreeNode]:
            res = []
            if N == 1:
                return [TreeNode(0)]
            # 结点个数必须是奇数
            if N % 2 == 0:
                return []
            
            # 左子树分配一个节点
            left_num = 1
            # 右子树可以分配到 N - 1 - 1 = N - 2 个节点
            right_num = N - 2
            
            while right_num > 0:
                # 递归构造左子树
                left_tree = self.allPossibleFBT(left_num)
                # 递归构造右子树
                right_tree = self.allPossibleFBT(right_num)
                # 具体构造过程
                for i in range(len(left_tree)):
                    for j in range(len(right_tree)):
                        root = TreeNode(0)
                        root.left = left_tree[i]
                        root.right = right_tree[j]
                        res.append(root)
                left_num += 2
                right_num -= 2
            return res  
## 257. 二叉树的所有路径
    描述：
        给定一个二叉树，返回所有从根节点到叶子节点的路径。
    示例：
        输入:
        
           1
         /   \
        2     3
         \
          5
        
        输出: ["1->2->5", "1->3"]
    解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
    题解：递归实现
        class Solution:
            def binaryTreePaths(self, root):
                """
                :type root: TreeNode
                :rtype: List[str]
                """
                def construct_paths(root, path):
                    if root:
                        path += str(root.val)
                        if not root.left and not root.right:  # 当前节点是叶子节点
                            paths.append(path)  # 把路径加入到答案中
                        else:
                            path += '->'  # 当前节点不是叶子节点，继续递归遍历
                            construct_paths(root.left, path)
                            construct_paths(root.right, path)
        
                paths = []
                construct_paths(root, '')
                return paths
        BFS实现：依靠队列或者栈都可以  # pop最后一个元素（实现栈）后进先出  pop(0)第一个元素（实现队列）先进先出
        class Solution:
            def binaryTreePaths(self, root):
                """
                :type root: TreeNode
                :rtype: List[str]
                """
                if not root:
                    return []
                paths = []
                cur_level = [(root,str(root.val))]
                while cur_level:
                    node,path = cur_level.pop()
                    if not node.left and not node.right:
                        paths.append(path)
                    if node.left:
                        cur_level.append((node.left,path+'->'+str(node.left.val)))
                    if node.right:
                        cur_level.append((node.right,path+'->'+str(node.right.val)))
                return paths
        DFS实现：依靠栈
        
## 110. 平衡二叉树
    描述：
        给定一个二叉树，判断它是否是高度平衡的二叉树。
        本题中，一棵高度平衡二叉树定义为：
        一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
    示例 1:
        给定二叉树 [3,9,20,null,null,15,7]
        
            3
           / \
          9  20
            /  \
           15   7
        返回 true 。
    题解：递归实现
    class Solution:
        def isBalanced(self, root: TreeNode) -> bool:
            self.res = True
            def helper(root):
                if not root:
                    return 0
                left = helper(root.left) + 1
                right = helper(root.right) + 1
                #print(right, left)
                if abs(right - left) > 1: 
                    self.res = False
                return max(left, right)
            helper(root)
            return self.res
## 1305. 两棵二叉搜索树中的所有元素
    描述：
        给你 root1 和 root2 这两棵二叉搜索树。
        请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.
    示例 1：
        输入：root1 = [2,1,4], root2 = [1,0,3]
        输出：[0,1,1,2,3,4]

    题解：
        二叉搜索树，则中序遍历就是顺序数组，两个数组插入排序
        class Solution:
            def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
                def dfs(node, v):
                    if not node:
                        return
                    dfs(node.left, v)
                    v.append(node.val)
                    dfs(node.right, v)
                
                v1, v2 = list(), list()
                dfs(root1, v1)
                dfs(root2, v2)
                ans, i, j = list(), 0, 0
                while i < len(v1) or j < len(v2):
                    if i < len(v1) and (j == len(v2) or v1[i] <= v2[j]):
                        ans.append(v1[i])
                        i += 1
                    else:
                        ans.append(v2[j])
                        j += 1
                return ans