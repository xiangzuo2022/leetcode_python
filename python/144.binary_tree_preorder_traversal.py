# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  # 先序遍历
    # @param {TreeNode} root
    # @return {integer[]}

    def interative_preorder(self,root,list):
    	stack = []
    	while root or stack:
    		if root:
    			list.append(root.val)
    			stack.append(root)
    			root = root.left
    		else:
    			root = stack.pop()
    			root = root.right
    	return list

    def recursive_preorder(self,root,list):
    	if root:
    		list.append(root.val)
    		self.recursive_preorder(left,list)
    		self.recursive_preorder(right,list)




    def preorderTraversal(self, root):
    	list = []
    	self.interative_preorder(root,list)
    	return list







# ******** The Second Time ********
"""
# 一下是我自己的解法， 更简洁; 递归
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        Solution.ans = []
        if not root: return Solution.ans
        self.preorder(root,Solution.ans)
        return Solution.ans


    def preorder(self,root,ans):
        if root:
            ans.append(root.val)
            self.preorder(root.left,ans)
            self.preorder(root.right,ans)



class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        ans = [];list = []
        while root or ans:
            if root:
                list.append(root.val)
                ans.append(root)
                root = root.left
            else:
                root = ans.pop()
                root = root.right
        return list



"""
非递归， 面试考非递归, 核心是stack;九章solution
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in list which contains node values.
    """
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:  #注意一定是先right进站再left， pop(0)也是这样, 一开始搞错的地方
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder


"""
divide-conquer, 用了九章的思想， 自己实现的
"""
class Solution(object):
    def preorderTraversal(self, root):
        result = []
        if not root:return result
        # divide
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        # conquer
        result.append(root.val)
        for x in left:
            result.append(x)
        for y in right:
            result.append(y)
        return result
























