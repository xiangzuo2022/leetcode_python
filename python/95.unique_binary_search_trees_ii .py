"""
# 题意：接上一题，这题要求返回的是所有符合条件的二叉查找树，而上一题要求的是符合条件的二叉查找树的棵数，
# 我们上一题提过，求个数一般思路是动态规划，而枚举的话，我们就考虑dfs了。dfs(start, end)函数返回以
# start，start+1，...，end为根的二叉查找树。
# 递归是关键
递归, 对于[start, end]范围内的每个节点, 产生所有可能的左、右子树, 再产生(#左子树 x #右子树)棵树,
返回所有的root nodes。gen函数返回一个list of root nodes, 每个root node所表示的树是由
[start, end]这个范围内的数构成的BST。
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = Nones

class Solution:
    # @return a list of tree node
    def dfs(self, start, end):
        if start > end:
            return [None]
        res = []
        for rootval in range(start, end+1):　　　　　　　　#rootval为根节点的值，从start遍历到end
            LeftTree = self.dfs(start, rootval-1)
            RightTree = self.dfs(rootval+1, end)
            for i in LeftTree:　　　　　　　　　　　　　　　　#i遍历符合条件的左子树
                for j in RightTree:　　　　　　　　　　　　  #j遍历符合条件的右子树
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
    def generateTrees(self, n):
        if n == 0:return []
        return self.dfs(1, n)







#  ********* The Second Time ********



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        def dfs(start,end):
            if start > end: return [None]
            for rootval in range(start,end+1):
                left = dfs(start,rootval-1)
                right = dfs(rootval+1,end)
                for i in left:
                    for j in right:
                        root = TreeNode(rootval)
                        root.left = i
                        root.right = j
                        res.append(root)

        res = []
        dfs(1,n)
        return res

# 不知道为何以上程序不能通过
