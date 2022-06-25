"""
The classic recursive problem in tree-based algorithms.
dfs
"""

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        def dfs(root):
            if root:                
                if low <= root.val <= high:
                    self.ans += root.val
                if root.val > low:
                    dfs(root.left)
                if root.val < high:
                    dfs(root.right)       
        
      
        self.ans = 0
        dfs(root)
        return self.ans