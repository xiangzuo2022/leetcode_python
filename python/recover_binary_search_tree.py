# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def inorder(self,root,list,listp):
    	if root:
    		self.inorder(root.left,list,listp)
    		list.append(root.val);listp.append(root)
    		self.inorder(root.right,list,listp)

    def recoverTree(self, root):
    	list = []; listp = []
    	self.inorder(root,list,listp)
    	list.sort()
    	for i in range(len(list)):
    		listp[i].val = list[i]
    	#return root # must remove the return otherwise you will get "Do not return anything, modify root in-place instead."


   

#  ****** The Second Time *******
"""
# 解题思路：这题是说一颗二叉查找树中的某两个节点被错误的交换了，需要恢复成原来的正确的二叉查找树。
# 算法一：思路很简单，一颗二叉查找树的中序遍历应该是升序的，而两个节点被交换了，那么对这个错误的二叉查
# 找树中序遍历，肯定不是升序的。那我们只需把顺序恢复过来然后进行重新赋值就可以了。开辟两个列表，list用
# 来存储被破坏的二叉查找树的节点值，listp用来存储二叉查找树的节点的指针。然后将list排序，再使用listp
# 里面存储的节点指针赋值就可以了。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        list = []; listp = []
        self.inorder(root,list,listp)
        list.sort()
        for i in range(len(list)):
            listp[i].val = list[i]


    def inorder(self,root,list,listp):
        if root:
            self.inorder(root.left,list,listp)
            list.append(root.val)
            listp.append(root)
            self.inorder(root.right,list,listp)

算法二：
题目有一个附加要求就是要求空间复杂度为常数空间。而算法一的空间复杂度为O(N)，还不够省空间。以下的解法也是
中序遍历的写法，只是非常巧妙，使用了一个prev指针。例如一颗被破坏的二叉查找树如下：

　　　　　　　　4

　　　　　　　/     \

　　       2        6

         /   \    /   \

         1    5  3    7

很明显3和5颠倒了。那么在中序遍历时：当碰到第一个逆序时：为5->4，那么将n1指向5，n2指向4，注意，此时n1已
经确定下来了。然后prev和root一直向后遍历，直到碰到第二个逆序时：4->3，此时将n2指向3，那么n1和n2都已经
确定，只需要交换节点的值即可。prev指针用来比较中序遍历中相邻两个值的大小关系，很巧妙。 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        self.n1 = self.n2 = None
        self.prev = None
        self.FindTwoNodes(root)
        self.n1.val,self.n2.val = self.n2.val, self.n1.val


    def FindTwoNodes(self,root):
        if root:
            self.FindTwoNodes(root.left)
            if self.prev and self.prev.val > root.val:
                self.n2 = root
                if self.n1 == None:
                    self.n1 = self.prev
            self.prev = root
            self.FindTwoNodes(root.right)

        

























