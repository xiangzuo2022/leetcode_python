# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
    	if not root:
    		return True
    	return self.isSymmetricTree(root.left,root.right)

    def isSymmetricTree(self,node1,node2):
    	if node1 and node2:
    		return node1.val == node2.val and self.isSymmetricTree(node1.left,node2.right) and self.isSymmetricTree(node1.right,node2.left)
    	else:
    		return node1 == node2

"""
递归
"""
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
            
        def compare(node1,node2):
    	    if node1 and node2:
    		    return node1.val == node2.val and compare(node1.left,node2.right) and compare(node1.right,node2.left)
    	    else:
    		    return node1 == node2
            
        if not root:
    	    return True
        return compare(root.left,root.right)
	

# https://www.youtube.com/watch?v=Mao9uzxwvmc
# DFS + recursion
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return (left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))
        return dfs(root.left, root.right)
                

        