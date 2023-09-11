"""
# 解题思路：这道题和层序遍历那道题差不多，区别只是在于奇数层的节点要翻转过来存入数组。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def preorder(self,root,level,res):
    	if root:
    		if len(res) < level + 1:
    			res.append([])  # because of returning [][]
    		if level % 2==0:  # even level
    			res[level].append(root.val) # 因为总是在首位插入， 所以是先right后left
    		else:
    			res[level].insert(0,root.val)  # level说明在哪个位置插入
    		self.preorder(root.left,level+1,res)
    		self.preorder(root.right,level+1,res)

    def zigzagLevelOrder(self, root):
    	res = []
    	self.preorder(root,0,res)
    	return res

"""
另一种写法
"""
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def bfs(root,level):
            if root:
                if len(ans) < level + 1:
                    ans.append([])
                if level % 2 == 0:
                    ans[level].append(root.val)
                else:
                    ans[level].insert(0,root.val)
                
                bfs(root.left,level+1)
                bfs(root.right,level+1)
            
        ans = []
        if not root: return []
        bfs(root,0)
        return ans
      
# non-recursive solution
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        queue = [root]
        level = 0
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if level % 2 == 0:
                    temp.append(node.val) 
                else:
                    temp.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)           
            ans.append(temp)
            level += 1
        return ans
    

# the  wrong solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        q = collections.deque([root])
        res = []
        level = 1
        while q:
            qLen = len(q)
            temp = []            
            for i in range(qLen):
                node = q.popleft()
                if node:
                    temp.append(node.val)
                    if level % 2 != 0:
                        if node.right:
                            q.append(node.right) # we should append value in oppsite order not the node itself. Otherwise, later the node's left and right push in the queue will be a choas. 
                        if node.left:
                            q.append(node.left)
                    else:
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
            level += 1
            res.append(temp)
        return res
            

 # https://www.youtube.com/watch?v=igbboQbiwqw
 # BFS 
 # # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        q = collections.deque([root])
        res = []
        level = 1
        while q:
            qLen = len(q)
            temp = []            
            for i in range(qLen):
                node = q.popleft()
                temp.append(node.val)                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level % 2 == 0:
                res.append(reversed(temp))
            else:
                res.append(temp)
            level += 1            
        return res                   