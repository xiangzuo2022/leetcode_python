"""
jiuzhang solution
不给parent指针 or root，此题没法做
divide and conquer 
遇到这个题目首先想的是要是能自底向上查找就好了，这样就可以找到公共祖先了。
那么二叉树如何可以自底向上查找呢？
回溯啊，二叉树回溯的过程就是从低到上。
后序遍历就是天然的回溯过程，最先处理的一定是叶子节点。
接下来就看如何判断一个节点是节点q和节点p的公共公共祖先呢。
如果找到一个节点，发现左子树出现结点p，右子树出现节点q，或者 左子树出现结点q，右子树出现节点p，那么该节点就是节点p和q的最近公共祖先。
使用后序遍历，回溯的过程，就是从低向上遍历节点，一旦发现如何这个条件的节点，就是最近公共节点了。
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:return None
        if root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:return root
        if left:return left
        if right:return right
        return None
        