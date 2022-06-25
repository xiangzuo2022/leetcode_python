"""
只要按照二叉搜索树的规则去遍历，遇到空节点就插入节点就可以了。不需要调整树 
"""
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return TreeNode(val)           
   
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root
            