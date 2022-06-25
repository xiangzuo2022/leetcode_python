"""
解题思路
这题要求求出所有二叉树子树中，元素都相同的子树的个数。给出的例子中，以5为值得子树个数是4个，以1为值得子树个数是0，所以答案是4。
如果一个子树是满足条件的元素相同的子树，那以它的子节点为根的子树也一定是满足条件的元素相同的子树。因此，我们可以从叶子节点从下往上（
bottom-up）判断。如果两个以叶子节点为根的子树都是元素相同的子树，并且它们的值与父节点的值相同，则以父节点为根的子树也是满足条件的子树。
但是节点没有父节点，无法往上判断，所以可以采用递归的方法从上往下调用判断。在代码的实现过程中，这里我们用计数器self.count记录满足条件的
子树个数，用一个辅助函数checkUni帮助我们从下往上查找UnivalSubTree.
"""

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.helper(root)
        return self.count
    
    def helper(self, root):
        if not root: return True
        l, r = self.helper(root.left), self.helper(root.right)
        if l and r and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
            self.count += 1
            return True
        return False