# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
    	if not root:
    		return 
    	self.flatten(root.left)
    	self.flatten(root.right)
    	p = root
    	if p.left == None:
    		return
    	p = p.left
    	while p.right:
    		p = p.right
    	p.right = root.right
    	root.right = root.left
    	root.left = None  # finally no node is on left



# ******** The Second Time ************
"""
# 这道题的意思是将一颗二叉树平化（flatten）为一条链表，而链表的顺序为二叉树的先序遍历。
# 解题思路：首先将左右子树分别平化为链表，这两条链表的顺序分别为左子树的先序遍历和右子树的先序遍历。
# 然后将左子树链表插入到根节点和右子树链表之间，就可以了。左右子树的平化则使用递归实现。
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
    def flatten(self, root):
        if not root: return        
        self.flatten(root.left)
        self.flatten(root.right)
        p = root
        if p.left == None:
            return
        p = p.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None

"""
# 解法2：不断消灭每一层的左子树
不太好想， 仔细想想是对的
latest updates:次解法更容易懂
"""

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        while root:
            if root.left:
                p = root.left
                while p.right:
                    p = p.right
                p.right = root.right
                root.right = root.left
                root.left = None
            root = root.right







