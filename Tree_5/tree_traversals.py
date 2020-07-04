#_*_coding:utf-8_*_
'''
@project: DailyAlgorithm
@author: exudingtao
@time: 2020/3/3 10:04 下午
'''


#深度优先搜索、广度优先搜索、前序遍历、中序遍历、后序遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeTraversal:

    def __init__(self):
        pass

    def dfs(self, root):
        res = []
        if not root:
            return []
        res.append(root)

    #前序遍历 根->左->右
    #递归实现
    def inorderRe(self,root,res_list):
        if not root:
            return []
        res_list.append(root.val)
        self.inorderRe(root.left, res_list)
        self.inorderRe(root.right, res_list)
        return res_list
    #循环实现
    def preorder(self, root):
        #用一个栈来回弄，用一个新的list存储遍历的元素
        #python 定义栈和队列都可以用list
        # 栈：list.pop()   队列：list.pop(0)
        if not root:
            return
        res_list = []
        temp_queue = [root]
        while temp_queue:
            last_node = temp_queue.pop()
            res_list.append(last_node.val)
            if last_node.right:
                temp_queue.append(last_node.right)
            if last_node.left:
                temp_queue.append(last_node.left)
        return res_list
    def preorder2(self,root):
        stack = []
        res = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
        return res

    #中序遍历 左->根->右
    #递归实现
    def inorder(self, root, res_list):
        if not root:
            return []
        self.inorder(root.left, res_list)
        res_list.append(root.val)
        self.inorder(root.right, res_list)
        return res_list
    #循环实现
    def inorder_byloop(self, root):
        if not root:
            return []
        res = []
        # 左-根-右
        stack = []
        while stack or root:
            if root:  # 节点一直走，换节点，不断将子节点入栈
                stack.append(root)  # 入
                root = root.left  # 换
            else:
                temp = stack.pop()  # 最左子节点
                res.append(temp.val)  # 得到
                root = temp.right  # 右边不空找右边，右边为空找根
        return res

    #后序遍历 左-右-根
    #递归实现
    def postorderRe(self, root, res_list):  ##后序遍历
        if not root:
            return []
        self.postorder(root.left, res_list)
        self.postorder(root.right, res_list)
        res_list.append(root.val)
        return res_list
    #循环实现：先序遍历是根左右->根右左->左右根
    def postorder(self,root):
        if not root:
            return []
        stack = []
        res = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.left)
                root = root.right #往右走
            else:
                root = stack.pop()
        return res[::-1]





if __name__ == '__main__':
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    child11 = TreeNode(4)
    child12 = TreeNode(5)
    child21 = TreeNode(6)
    child22 = TreeNode(7)
    root.left = child1
    root.right = child2
    child1.left = child11
    child1.right = child12
    child2.left = child21
    child2.right = child22

    tra = TreeTraversal()
    res = tra.preorder2(root)
    print(res)

