# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root: return 0
        else:
            return 1 + self.countNodes(root.left)  +  self.countNodes(root.right)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_height, right_height = 0, 0
        left_node, right_node = root, root
        while left_node:
            left_height += 1
            left_node = left_node.left
        while right_node:
            right_height += 1
            right_node = right_node.right
        if left_height == right_height:
            return pow(2, left_height) -1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        https://leetcode-cn.com/problems/count-complete-tree-nodes/solution/wan-quan-er-cha-shu-by-powcai/
        
        
"""
安层遍历没有利用完全二叉树的性质
"""
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        queue = [root]
        total = 0
        while queue:
            size = len(queue)           
            for i in range(size):
                node = queue.pop(0)                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            total += size
        return total