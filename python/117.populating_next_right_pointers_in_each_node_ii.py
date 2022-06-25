# 解题思路：和"Populating Next Right Pointers in Each Node"这道题不同的一点是，
# 这道题的二叉树不是满的二叉树，有些节点是没有的。但是也可以按照递归的思路来完成。在编写递归的基准情况时
# 需要将细节都考虑清楚：

#这道是之前那道 Populating Next Right Pointers in Each Node 的延续，原本的完全二叉树的条件不再满足，
#但是整体的思路还是很相似，仍然有递归和非递归的解法。我们先来看递归的解法，这里由于子树有可能残缺，
#故需要平行扫描父节点同层的节点，找到他们的左右子节点。

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
    	if root:
    		if root.left and root.right:
    			root.left.next = root.right
    			tmp = root.next
    		while tmp:
    			if tmp.left:
    				root.right.next = tmp.left
    				break
    			if tmp.right:
    				root.right.next = tmp.right
    				break
    			tmp = tmp.next
    		elif root.left:
    			tmp = root.next
    			while tmp:
    				if tmp.left:
    					root.left.next = tmp.left
    					break
    				if tmp.right:
    					root.left.next = tmp.right
    					break
    				tmp = tmp.next
    		elif root.right:
    			while tmp:
    				if tmp.left: 
    					root.right.next = tmp.left
    					break
    				if tmp.right:
    					root.right.next = tmp.right
    					break
    				tmp = tmp.next
    		self.connect(root.right)
    		self.connect(root.left)


#  没看懂以下写法？？？？？？
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
    	if root:
            p = root; q = None; nextNode = None
            while p:
                if p.left:
                    if q: 
                    	q.next = p.left
                    q = p.left
                    if nextNode == None: 
                    	nextNode = q
                if p.right:
                    if q: 
                    	q.next = p.right
                    q = p.right
                    if nextNode == None: 
                    	nextNode = q
                p = p.next
            self.connect(nextNode)


"""
下面这个做法没满足题目中的常数空间的要求，不过是个非递归的好做法，对完全二叉树也完全试用。
做法就是把每层的节点放到一个队列里，把队列的每个元素进行弹出的时候，如果它不是该层的最后一个元素，
那么把它指向队列中的后面的元素（不把后面的这个弹出）。
"""
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)



"""
copy code from 116
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





















