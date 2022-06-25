    
#*********** The Second Time *************
"""
# 解题思路：在这道题里，平衡二叉树的定义是二叉树的任意节点的两颗子树之间的高度差小于等于1。这实际上是AVL树的定义。
# 首先要写一个计算二叉树高度的函数，二叉树的高度定义为：树为空时，高度为0。然后递归求解：树的高度 = max(左子树
# 高度，右子树高度)+1(根节点要算上)。高度计算函数实现后，递归求解每个节点的左右子树的高度差，如果有大于1的，
# 则return False。如果高度差小于等于1，则继续递归求解。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def level(self,root):
        if not root:
            return 0
        else:
            return max(self.level(root.right),self.level(root.left)) + 1
            
    def isBalanced(self, root):
        if not root:
            return True
        if abs(self.level(root.left) - self.level(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False


"""
九章的答案
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        balanced, _ = self.validate(root)
        return balanced
        
    def validate(self, root):
        if root is None:
            return True, 0
            
        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False, 0
            
        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1












