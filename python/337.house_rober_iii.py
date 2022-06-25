"""
递归解法
记忆化搜索（DFS + Memoization）

记当前房间为root，如果偷窃当前房间，则其左右孩子left和right均不能偷窃；而其4个孙子节点（ll，lr，rl，rr）不受影响。

因此最大收益为：

maxBenifit = max(rob(left) + rob(right), root.val + rob(ll) + rob(lr) + rob(rl) + rob(rr))
使用字典valMap记录每一个访问过的节点，可以避免重复运算。
"""
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        valMap = dict()
        def solve(root, path):
            if root is None: return 0
            if path not in valMap:
                left, right = root.left, root.right
                ll = lr = rl = rr = None
                if left:  ll, lr = left.left, left.right
                if right: rl, rr = right.left, right.right
                passup = solve(left, path + 'l') + solve(right, path + 'r')
                grabit = root.val + solve(ll, path + 'll') + solve(lr, path + 'lr') \
                         + solve(rl, path + 'rl') + solve(rr, path + 'rr')
                valMap[path] = max(passup, grabit)
            return valMap[path]
        return solve(root, '')
      
  """
  DP解法
  所以dp数组（dp table）以及下标的含义：下标为0记录不偷该节点所得到的的最大金钱，下标为1记录偷该节点所得到的的最大金钱。
  """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        result = self.rob_tree(root)
        return max(result[0], result[1])
    
    def rob_tree(self, node):
        if node is None:
            return (0, 0) # (偷当前节点金额，不偷当前节点金额)
        left = self.rob_tree(node.left)
        right = self.rob_tree(node.right)
        val1 = node.val + left[1] + right[1] # 偷当前节点，不能偷子节点
        val2 = max(left[0], left[1]) + max(right[0], right[1]) # 不偷当前节点，可偷可不偷子节点
        return (val1, val2)
      
"""
记忆化递归
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memory = {}
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right  is None:
            return root.val
        if self.memory.get(root) is not None:
            return self.memory[root]
        # 偷父节点
        val1 = root.val
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)
        # 不偷父节点
        val2 = self.rob(root.left) + self.rob(root.right)
        self.memory[root] = max(val1, val2)
        return max(val1, val2)