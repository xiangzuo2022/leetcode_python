"""
递归is the point of tree-based problems
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isSame(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return isSame(a.left, b.left) and isSame(a.right, b.right)
        
        if not root:
            return False
        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
# https://www.youtube.com/watch?v=E36O5SWp-LE
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subRoot: return True
        if not root: return False
        if self.sameTree(root, subRoot): 
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        

    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1 and not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
        
    