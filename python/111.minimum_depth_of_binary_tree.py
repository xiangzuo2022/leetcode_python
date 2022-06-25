# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
    	if not root:
    		return 0
    	else:
    		if not root.left:
    			return self.minDepth(root.right) + 1
    		elif not root.right:
    			return self.minDepth(root.left) + 1
    		else:
    			return min(self.minDepth(root.left),self.minDepth(root.right)) + 1


# ********* The Second Time **********
"""
递归
# 解题思路：分几种情况考虑：1，树为空，则为0。 2，根节点如果只存在左子树或者只存在右子树，则返回值应为左子树
# 或者右子树的（最小深度+1）。 3，如果根节点的左子树和右子树都存在，则返回值为（左右子树的最小深度的较小值+1）。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:  # left is empty
            return self.minDepth(root.right) + 1
        if not root.right: # right is empty
            return self.minDepth(root.left) + 1
        if root.left and root.right:
            return min(self.minDepth(root.right),self.minDepth(root.left)) + 1














