# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    

    def preOrder(self,root,level): # 遍历得到层
        if level in Solution.d:
            Solution.d[level].append(root.val)
        else:
            Solution.d[level] = [root.val]
        if root.left:
            self.preOrder(root.left,level+1)
        if root.right:
            self.preOrder(root.right,level+1)
        return

    def levelOrderBottom(self, root):
        res = []
        if not root:
            return res
        Solution.d = {}
        self.preOrder(root,0)
        for i in sorted(Solution.d.keys(),reverse=True):  # 按层输出
            res.append(Solution.d[i])
        return res

# ********* The third time ********
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def preOrder(root,level):
            if level not in d:
                d[level] = [root.val]
            else:
                d[level].append(root.val)
            if root.left:
                preOrder(root.left,level+1)
            if root.right:
                preOrder(root.right,level+1)
            
        d = dict()
        ans = []
        if not root:return ans
        preOrder(root,0)
        for i in sorted(d.keys(),reverse=True):
            ans.append(d[i])
        return ans



"""
the same as NO. 102
"""
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        queue = [root]
        ans = []
        while queue:
            tmp = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.insert(0,tmp)
        return ans
        
