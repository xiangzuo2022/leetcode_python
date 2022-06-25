# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
    	ans = []
    	if not root:
    		return ans
    	queue = [root]
    	while queue:
    		for i in range(len(queue)):
    			top = queue.pop(0)
    			if i == 0:  # root
    				ans.append(top.val)
    			if top.right:
    				ans.append(top.right)
    			if top.left:
    				ans.append(top.left)
    	return ans


"""
 # 解题思路：二叉树的层次遍历，每层按照从右向左的顺序依次访问节点
"""
 # ******** The Second Time *********

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
本质使用BFS来解题， 有点巧妙
"""

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        ans = []
        if root == None:
            return ans
        queue = [root]
        while queue:
            for i in range(len(queue)): # finish one level
                top = queue.pop(0):  # pop(0)从头部弹出一个元素
                if i == 0: #这一步判断很重要，如果不加判读会把左边的点也放入ans，queue最前面的点总是右边的， 除非右边的点没有了
                    ans.append(top.val) # only the first element in the queue will be added into the results 
                if top.right:  # 巧妙的地方在这里, 先right后left导致left不会输出
                    queue.append(top.right)
                if top.left:
                    queue.append(top.left)
        return ans
































