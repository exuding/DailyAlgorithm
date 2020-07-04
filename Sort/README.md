# 排序
    
## 56. 合并区间
    描述：
        给出一个区间的集合，请合并所有重叠的区间。
    示例 1:
        输入: [[1,3],[2,6],[8,10],[15,18]]
        输出: [[1,6],[8,10],[15,18]]
        解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    示例 2:
        输入: [[1,4],[4,5]]
        输出: [[1,5]]
        解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
    题解：
        按每个元素第一个元素排序后 插入到空list中，边插入边合并
        class Solution:
            def merge(self, intervals: List[List[int]]) -> List[List[int]]:
                res = []
                intervals.sort()
                for i in intervals:
                    if not res or res[-1][1] < i[0]:
                        res.append(i)
                    else:
                        res[-1][1] = max(i[1],res[-1][1])
                return res
                
## 1305. 两棵二叉搜索树中的所有元素
    描述：
        给你 root1 和 root2 这两棵二叉搜索树。
        请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.
    示例 1：  
        输入：root1 = [2,1,4], root2 = [1,0,3]
        输出：[0,1,1,2,3,4]
    示例 2：
        输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
        输出：[-10,0,0,1,2,5,7,10]
    题解：
        利用二叉搜索树的性质：
        对二叉搜索树进行中序遍历，就可以直接得到树中所有元素升序排序后的结果
        对两棵树分别进行中序遍历，得到数组 v1 和 v2，它们分别存放了两棵树中的所有元素，且均已有序。
        在这之后，我们通过归并排序的方法对 v1 和 v2 进行排序
        
        时间复杂度：O(M + N)O(M+N)，其中 MM 和 NN 是两棵树中的节点个数。
        中序遍历的时间复杂度为 O(M + N)O(M+N)，归并排序的时间复杂度同样为 O(M + N)O(M+N)。
        空间复杂度：O(M + N)O(M+N)。我们需要使用额外的空间存储数组 v1 和 v2。
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
        ################################################   
        class Tree(object):
            def __init__(self, root):
                self.stack = []
                while root:
                    self.stack.append(root)
                    root = root.left
            
            def next(self):
                cur = self.stack.pop()
                val = cur.val
                cur = cur.right
                while cur:
                    self.stack.append(cur)
                    cur = cur.left
                return val
            
            def top(self):
                return self.stack[-1].val
            
            def empty(self):
                return not bool(self.stack)

        class Solution(object):
            def getAllElements(self, root1, root2):
                """
                :type root1: TreeNode
                :type root2: TreeNode
                :rtype: List[int]
                """
                result = []
                t1 = Tree(root1)
                t2 = Tree(root2)
        
               while not t1.empty() and not t2.empty():
                    t1_val = t1.top()
                    t2_val = t2.top()
                    if t1_val < t2_val:
                        result.append(t1_val)
                        t1.next()
                    else:
                        result.append(t2_val)
                        t2.next()
                while not t1.empty():
                    result.append(t1.next())
                while not t2.empty():
                    result.append(t2.next())
                return result
                
## 853. 车队
    描述：
        N  辆车沿着一条车道驶向位于 target 英里之外的共同目的地。
        每辆车 i 以恒定的速度 speed[i] （英里/小时），从初始位置 position[i] （英里） 沿车道驶向目的地。
        一辆车永远不会超过前面的另一辆车，但它可以追上去，并与前车以相同的速度紧接着行驶。
        此时，我们会忽略这两辆车之间的距离，也就是说，它们被假定处于相同的位置。
        车队 是一些由行驶在相同位置、具有相同速度的车组成的非空集合。注意，一辆车也可以是一个车队。
        即便一辆车在目的地才赶上了一个车队，它们仍然会被视作是同一个车队。
        会有多少车队到达目的地？
    示例：
        输入：target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        输出：3
        解释：
        从 10 和 8 开始的车会组成一个车队，它们在 12 处相遇。
        从 0 处开始的车无法追上其它车，所以它自己就是一个车队。
        从 5 和 3 开始的车会组成一个车队，它们在 6 处相遇。
        请注意，在到达目的地之前没有其它车会遇到这些车队，所以答案是 3。

    题解：
        [(1.0, 8), (1.0, 10), (3.0, 3), (7.0, 5), (12.0, 0)]
        通过下面的dp数组来解决。因为时间已经有序，从后往前找位置，如果当前的大于后面的说明追不上，
        当前的小于后面的，例如(3.0, 3), (7.0, 5)说明能追上，能追上两车的时间就依据最大的来定
        dp = [None] * n
        dp[-1] = reach_target[-1][1]
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i+1],reach_target[i][1])
                    
        class Solution:
            def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
                if not position:
                    return 0
                n = len(position)
                reach_target = []
                for i in range(n):
                    reach_target.append(((target - position[i]) / speed[i], position[i]))
                reach_target.sort()
                print(reach_target)
                dp = [None] * n
                dp[-1] = reach_target[-1][1]
                for i in range(n - 2, -1, -1):
                    dp[i] = max(dp[i+1],reach_target[i][1])
                return len(set(dp))

                
        


            

