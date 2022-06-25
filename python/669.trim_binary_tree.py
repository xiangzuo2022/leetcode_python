方法：递归
思路

令 trim(node) 作为该节点上的子树的理想答案。我们可以递归地构建该答案。

算法

当 node.val > R}node.val > R，那么修剪后的二叉树必定出现在节点的左边。

类似地，当 node.val < L}node.val < L，那么修剪后的二叉树出现在节点的右边。否则，我们将会修剪树的两边。

JavaPython


作者：LeetCode
链接：https://leetcode-cn.com/problems/trim-a-binary-search-tree/solution/xiu-jian-er-cha-sou-suo-shu-by-leetcode/
class Solution(object):
    def trimBST(self, root, L, R):
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
      
      
"""
递归
"""
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < low:
            root = root.right 
            root = self.trimBST(root, low, high)
        elif root.val > high:
            root = root.left 
            root = self.trimBST(root, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root

