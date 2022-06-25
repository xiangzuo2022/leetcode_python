# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}

    def pathSum(self, root, sum):
    	def dfs(root,currsum,valulist):
    		if root.left == None and root.right == None:
    			if currsum == sum:
    				res.append(valulist)
    		if root.left:
    			dfs(root.left, currsum+root.left.val,valulist+[root.left.val])
    		if root.right:
    			dfs(root.right, currsum+root.right.val,valulist+[root.right.val])



    	if not root:
    		return []
    	res = []
    	dfs(root,root.val,[root.val])
    	return res


# ********* The Second Time *********
"""
# 解题思路：这题需要将根到叶子的路径和为sum的路径都枚举出来。一样是使用递归。
最后是以value值的形式输出的，所以递归的时候要用value
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        def dfs(root,currsum,value):
            if root.left == None and root.right == None:
                if currsum == sum:
                    res.append(value)
            if root.left:
                dfs(root.left,currsum+root.left.val,value+[root.left.val])
            if root.right:
                dfs(root.right, currsum+root.right.val,value+[root.right.val])
        if not root: return []
        res = []
        dfs(root,root.val,[root.val])
        return res



"""
另外一种写法， 思路是一样的
"""
class Solution(object):
    def pathSum(self, root, sums):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root,sums,value):
            if not root.left and not root.right and sums == 0:
                ans.append(value)
                    
            if root.left:
                dfs(root.left,sums-root.left.val,value+[root.left.val])
            if root.right:
                dfs(root.right,sums-root.right.val,value+[root.right.val])
            
        if not root:return []
        ans = []
        dfs(root,sums-root.val,[root.val]) #递归里面没有对root采取措施， 这里要处理root
        return ans
















