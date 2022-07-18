"""
# 解题思路：看到二叉树，我们首先想到递归。
# 此题求和为sum=124+125+136+137，我们可以使用一个preSum变量来记录从根节点到节点父亲的路径，比如当
# 我们递归的4时，preSum=12，递归到6时，preSum=13，这样就可以了。
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
    def sum(self,root,presum):
    	if not root:
    		return 0
    	presum = presum*10 + root.val
    	if root.left == None and root.right == None:
    		return presum
    	return self.sum(root.left,presum) + self.sum(root.right,presum)


    def sumNumbers(self, root):
    	return self.sum(root,0)


"""
我自己的解法， 代码不够清晰
"""
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def path(root,s):
            s = s*10 + root.val
            print s
            if root.left:
                path(root.left,s)
            if root.right:
                path(root.right,s)
            if root and not root.right and not root.left:
                ans.append(s)
                s = 0  # 清零
            return ans
            
        if not root:return 0
        s = 0; ans = []
        path(root,s)
        return sum(ans)

"""
直观的解法是DFS
"""
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, prevSum):
            if not node:
                return 0
            total = prevSum * 10 + node.val 
            if not node.left and not node.right:
                return total
            else:
                return dfs(node.left, total) + dfs(node.right, total)
        return dfs(root, 0)






























