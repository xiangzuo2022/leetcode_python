# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
    	if root and root.left:
    		root.left.next = root.right
    		if root.next:
    			root.right.next = root.next.left
    		else:
    			root.right.next = None
            self.connect(root.left)
            self.connect(root.right)


# ********* The Second Time **********
"""
# 解题思路：看到二叉树我们就想到需要使用递归的思路了
# 一下代码很简洁
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
    	if root and root.left:
    		root.left.next = root.right
    		if root.next:
    			root.right.next = root.next.left
    		else:
    			root.right.next = None
    		self.connect(root.left)
    		self.connect(root.right)
      
      
"""
本题依然是层序遍历，只不过在单层遍历的时候记录一下本层的头部节点，然后在遍历的时候让前一个节点指向本节点就可以了
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == size-1:
                    break
                node.next = queue[0]
        return root



























