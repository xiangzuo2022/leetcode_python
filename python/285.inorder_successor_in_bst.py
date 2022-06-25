class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
    
        successor = None
        while root != None and root.val != p.val:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        
        # 原本的root = None 或者 p不存在与BST中，此刻root = None
        if root == None:
            return None
                
        # 找到p之后，如果p没有右儿子，则第一个比它大的数字就是刚刚记录的successor
        if root.right == None:
            return successor
        
        # 找到p之后，如果有右儿子，则找到右子树中的最左边的值（最小值）
        root = root.right
        while root.left != None:
            root = root.left
        
        return root

    class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = None
        while root and root.val != p.val:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        if not root: return None
        if root.right == None:
            return successor
        root = root.right
        while root.left:
            root = root.left
        return root