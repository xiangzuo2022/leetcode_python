"""
BFS: total needs to multiply 1.0 otherwise the results are wrong
"""
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        if not root:
            return res
        q = [root]
        while q:
            total, size = 0, len(q)
            for _ in xrange(size):
                node = q.pop(0)
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(total * 1.0 / cnt)
        return res