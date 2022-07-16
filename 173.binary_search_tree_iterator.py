# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
    	self.stack = []
    	self.pushLeft(root)

    def pushLeft(self,node):
    	while node: 
    		self.stack.append(node)
    		node = node.left

    def hasNext(self):
    	return self.stack

    def next(self):
    	top = self.stack.pop()
    	self.pushLeft(top.right)
    	return top.val


#  http://bookshadow.com/weblog/2014/12/31/leetcode-binary-search-tree-iterator/

#******** The Second Time *************
"""
# 解题思路：
# 维护一个栈，从根节点开始，每次迭代地将根节点的左孩子压入栈，直到左孩子为空为止。
# 调用next()方法时，弹出栈顶，如果被弹出的元素拥有右孩子，则以右孩子为根，将其左孩子迭代压栈。
根据上面的遍历顺序，我们得出迭代的思路：

构造方法：一路到底，把根节点和它的所有左节点放到栈中；
调用 next() 方法：弹出栈顶的节点；
如果它有右子树，则对右子树一路到底，把它和它的所有左节点放到栈中。

作者：fuxuemingzhu
链接：https://leetcode.cn/problems/binary-search-tree-iterator/solution/fu-xue-ming-zhu-dan-diao-zhan-die-dai-la-dkrm/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack
        

    # @return an integer, the next smallest number
    def next(self):
        top = self.stack.pop()
        self.pushLeft(top.right) # 要赶紧压入top.right,因为pushLeft只压入了左边的结点
        return top.val

    def pushLeft(self,node):
        while node:
            self.stack.append(node)
            node = node.left
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


"""
discussion里的解法， good！
"""
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
        

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val

class BSTIterator:

    def __init__(self, root: TreeNode):
        
        # Array containing all the nodes in the sorted order
        self.nodes_sorted = []
        
        # Pointer to the next smallest element in the BST
        self.index = -1
        
        # Call to flatten the input binary search tree
        self._inorder(root)
        
    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.nodes_sorted)

作者：LeetCode
链接：https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/er-cha-sou-suo-shu-die-dai-qi-by-leetcode/


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.inorder = []
        if not root:return None
        while root or self.stack:
            if root:
                self.stack.append(root)
                root = root.left
            else:
                root = self.stack.pop()
                self.inorder.append(root.val)
                root = root.right        
            
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.inorder.pop(0)
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.inorder) > 0
        























