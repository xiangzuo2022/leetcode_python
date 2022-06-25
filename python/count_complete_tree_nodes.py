"""
# 完全二叉树的定义为：
# 高度为h，有n个结点的二叉树，当前仅当其每一个结点都与高度为h的满二叉树中编号为1~n的结点一一对应时，
# 称为完全二叉树。即叶节点只可能出现在层次最大的两层上，最大层上的叶节点从左到右依次排列。
此题可以延伸为判断满binary tree 问题和求树的高度
用递归不好把握很容易超时
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
    def countNodes(self, root):
    	if self.getDepth(root,True) == self.getDepth(root,False):  # full
    		return int(2**self.getDepth(root,True)) - 1
    	else:
    		return self.countNodes(root.left) + self.countNodes(root.right) + 1 # +1 is the root

    def getDepth(self,root,isLeft):
    	level = 0
    	while root:
    		if isLeft:
    			root = root.left
    		else:
    			root = root.right
    		level += 1
    	return level



    	