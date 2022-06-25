"""
# 本题要求的“最大路径和”，不一定经过了root，起点和终点可以是同一个点（即整个路径只有一个点）。
# 注意用一个类成员变量max来记录搜索过程中出现过的最大路径和，最后需要返回的就是这个max值。
# 此外还有一点容易搞错，当一棵子树计算完退栈时，向上一层返回的应该是该子树左路径、右路径中的最大值，
# 而不是该子树中的“最大路径和”，因为从父节点搜索进入该子树时，只能选择其左分支或者右分治进入。
# 这里需要注意的一点是：节点值有可能为负值。
# 解决这道二叉树的题目还是来使用递归.
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
    def __init__(self):
    	self.max = None
    def doMaxPathSum(self,root):
    	if root == None: return 0
    	left_sum = self.doMaxPathSum(root.left)
    	right_sum = self.doMaxPathSum(root.right)
    	max_left_sum = max(left_sum,0)
    	max_right_sum = max(right_sum,0)
    	cur_max = max_left_sum + max_right_sum + root.val
    	if self.max == None or cur_max > self.max:
    		self.max = cur_max
    	return max(max_left_sum + root.val,max_right_sum + root.val)


    def maxPathSum(self, root):
    	self.doMaxPathSum(root)
    	return self.max


"""
论坛里高手的解法； 九章解法不好
"""
import sys
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxValue = -sys.maxint
        self.helper(root)
        return self.maxValue
        
    def helper(self,root):
        if not root:return 0
        left = max(0,self.helper(root.left)) # if node is null, the minimum value is zero
        right = max(0,self.helper(root.right))
        self.maxValue = max(self.maxValue, left+right+root.val)
        return max(left,right) + root.val










    	

