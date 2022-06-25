# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Solution 递归
class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
    	if not root:
    		return None
    	tmp = TreeNode(0) # must first generate a tree structure
    	tmp = root.left
    	root.left = self.invertTree(root.right)
    	root.right = self.invertTree(tmp)
    	
    	return root

"""
Python handles exchange in special
"""
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(
                root.right), self.invertTree(root.left)
        return root
      

"""
Another implementation-- down to the end 
"""
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None      
        
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

"""
iterative solution -- using stack
"""

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
