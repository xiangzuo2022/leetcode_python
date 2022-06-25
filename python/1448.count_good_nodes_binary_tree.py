# dfs quesitons and need to check whether the left or right node exists

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, value):
            if node.val >= value:
                self.counter += 1
            if node.left:
                dfs(node.left, max(node.val, value))
            if node.right:
                dfs(node.right, max(node.val, value))
        
        if not root:
            return 0
        self.counter = 0
        dfs(root, root.val)
        return self.counter