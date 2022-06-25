# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
    	list = []
    	self.iterative_postorder(root,list)
    	return list
    def iterative_postorder(self, root, list):
        stack = []; pre = None
        if root:
        	stack.append(root)
        	while stack:
        		cur = stack[-1] # cur is the top element
        		if (cur.left==None and cur.right==None) or (pre and (pre==cur.left or pre==cur.right)):
        			list.append(cur.val)
        			stack.pop()
        			pre = cur
        		else:
        			if cur.right:
        				stack.append(cur.right)
        			if cur.left:
        				stack.append(cur.left)
        return list


"""
# Solution 2:最优解法
# 另一种解法是使用两个栈。试着在纸上写一下代码。我认为这种解法非常的神奇而优美。你可能觉得这很不可思议，
# 但实际上它做的是反向的先序遍历。亦即遍历的顺序是：节点 -> 右子树 -> 左子树。这生成的是后根遍历的逆序输出。
# 使用第二个栈，再执行一次反向输出即可得到所要的结果。
http://bookshadow.com/weblog/2015/01/19/binary-tree-post-order-traversal/
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
    def postorderTraversal(self, root):
    	if not root: return []
    	stack = [root]
    	ans = []
    	while stack:
    		top = stack.pop()
    		ans.append(top.val)
    		if top.left:
    			stack.append(top.left)
    		if top.right:
    			stack.append(top.right)
    	return ans[::-1]


# my own solution recursive
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                ans.append(root.val)
        
        ans = []
        if not root:return ans
        postorder(root)
        return ans

"""
Use insert from left trick, then the template will be the same as inorder and preorder traverse
"""
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, ans = [], []
        while root or stack:
            if root:
                stack.append(root)
                ans.insert(0, root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        return ans

"""
后序遍历顺序 左-右-中 入栈顺序：中-左-右 出栈顺序：中-右-左， 最后翻转结果
"""
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 左孩子先入栈
            if node.left:
                stack.append(node.left)
            # 右孩子后入栈
            if node.right:
                stack.append(node.right)
        # 将最终的数组翻转
        return result[::-1]













