"""
递归回溯
"""
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        def dfs(root):
            if root:
                if root.left and root.left.left == None and root.left.right == None:
                    self.total += root.left.val 
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        return self.total