"""
# 解题思路：BST具有如下性质：
# 左子树中所有元素的值均小于根节点的值
# 右子树中所有元素的值均大于根节点的值
# 适合follow-up questions
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
    	stack = []
    	node = root
    	while node:
    		stack.append(node)  # append 的不是节点值是节点
    		node = node.left
    	i = 1
    	while stack and i <= k:
    		node = stack.pop()
    		i += 1
    		right = node.right
    		while right:
    			stack.append(right)
    			right = right.left
    	return node.val


"""
my own method, which is straightforward
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        ans = []
        if not root: return ans
        self.inorder(root,ans)
        return ans[k-1]
    
    def inorder(self,root,ans):
        if root:
            self.inorder(root.left,ans)
            ans.append(root.val)
            self.inorder(root.right,ans)



"""
可以控制的更好点
# 解题思路：BST具有如下性质：
# 左子树中所有元素的值均小于根节点的值
# 右子树中所有元素的值均大于根节点的值
# 因此采用中序遍历（左 -> 根 -> 右）即可以递增顺序访问BST中的节点，从而得到第k小的元素，时间复杂度O(k).
""" 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        ans = []
        if not root: return ans
        self.inorder(root,ans,k)
        return ans[k-1]
    
    def inorder(self,root,ans,k):
        if root and len(ans) < k:
            self.inorder(root.left,ans,k)
            ans.append(root.val)
            self.inorder(root.right,ans,k) 


# https://www.youtube.com/watch?v=5LUXSvjmGCw&t=28s
# iterative
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right































    	 
    	

