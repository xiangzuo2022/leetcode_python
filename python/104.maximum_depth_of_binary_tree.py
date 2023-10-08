# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
这是一种分治的思想
"""
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
    	
    	if not root:
    		return 0
    	return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

# the same as balanced tree


"""
九章给的答案: divide conquer
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left) 
        right = self.maxDepth(root.right) 
        return max(left,right) + 1


# https://www.youtube.com/watch?v=hTM3phVI6YQ
# Three ways
# (1) DFS + recursive
# O(n) for time and memory complexity
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



# (2) BFS and no recrusion
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        q = collections.deque()
        q.append(root)
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:                
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


# (3) DFS without recursion Iterative DFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
    
# https://www.youtube.com/watch?v=hTM3phVI6YQ&t=57s
# BFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left :
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
    
# Iterative DFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res 