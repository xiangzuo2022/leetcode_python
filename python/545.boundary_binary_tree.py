"""
Don't add the same node twice. 
A video: https://www.youtube.com/watch?v=F76LIKzluKE
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs_leftmost(node):
            if not node.left and not node.right:
                return
            result.append(node.val)
            if node.left:
                dfs_leftmost(node.left)
            elif node.right:
                dfs_leftmost(node.right)
                
            
        def dfs_leaves(node):
            if not node:return
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                result.append(node.val)
            dfs_leaves(node.right)
            
        def dfs_rightmost(node):
            if not node.left and not node.right:
                return
            
            if node.right:
                dfs_rightmost(node.right)
            elif node.left:
                dfs_rightmost(node.left)
            result.append(node.val)
                
        if not root:return []  
        result = [root.val]
        if root.left:
            dfs_leftmost(root.left)
        dfs_leaves(root)
        if root.right:
            dfs_rightmost(root.right)
            
        return result
        