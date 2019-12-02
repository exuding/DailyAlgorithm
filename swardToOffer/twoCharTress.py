'''
定义二叉树节点，以及二叉树的前序，中序，后序遍历
'''
class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class Tree(object):
    #python的构造方法
    #构造方法类似于类似init()这种初始化方法，来初始化新创建对象的状态，在一个对象呗创建以后会立即调用，比如像实例化一个类：
    # f = FooBar()
    # f.init()
    # 使用构造方法就能让它简化成如下形式：
    # f = FooBar()
    def __init__(self):
        self.root = None
    #普通二叉树构造
    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)
    #二叉排序树，平衡二叉树构造
    def bstinsert(self,root,item):
        if root == None:
            return False
        elif item < root.item:
            root.left = self.bstinsert(root.left,item)
        elif item > root.item:
            root.right = self.bstinsert(root.right,item)
        return root
    #层次遍历
    def traverse(self):
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.item)

            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.item)
        return res
    #先序遍历
    def preorder(self,root):
        if root is None:
            return []
        res = [root.item]
        left_item = self.preorder(root.left)
        right_item = self.preorder(root.right)
        return res + left_item + right_item
    #中序遍历
    def inorder(self,root):
        if root is None:
            return []
        res = [root.item]
        left_item = self.inorder(root.left)
        right_item = self.inorder(root.right)
        return left_item + res + right_item
    #后序遍历
    def postorder(self,root):
        if root is None:
            return []
        res = [root.item]
        left_item = self.postorder(root.left)
        right_item = self.postorder(root.right)
        return  left_item + right_item + res

if __name__ == '__main__':
    t = Tree()
    for i in range(10):
        t.add(i)
    print('层序遍历:',t.traverse())
    print('先序遍历:',t.preorder(t.root))
    print('中序遍历:',t.inorder(t.root))
    print('后序遍历:',t.postorder(t.root))

