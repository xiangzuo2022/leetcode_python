class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        def longestPath(node):
            if not node:
                return 0
            
            left_path = longestPath(node.left)
            right_path = longestPath(node.right)
            self.diameter = max(self.diameter, left_path + right_path)
            return max(left_path, right_path) + 1
        
        longestPath(root)
        return self.diameter
      
Official Solution: 
In the midst of DFS, we also need to take the following two cases into account:
the current node's both left and right branches might be a part of the longest path;
one of the current node's left/right branches might be a part of the longest path.