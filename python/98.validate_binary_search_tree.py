# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def ValidBST(self,root,min,max):
    	if not root:
    		return True
    	if root.val <= min or root.val >= max:
    		return False
    	return self.ValidBST(root.left,min,root.val) and self.ValidBST(root.right,root.val,max)

    def isValidBST(self, root):
    	return self.ValidBST(root,-3147483648, 3147483647)


"""
比较直接的解法: 中序遍历tree， 得到的array是递增的就是否则不是， 要注意排除相同的情况
iterative
"""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder(root):
            if root:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)
        ans = []
        inorder(root)
        if not root:return True
        for i in range(len(ans)-1):  # 不能用 ans == sorted(ans) 来判断， 因为[1,1] 相等的case错误
            if ans[i+1] <= ans[i]:
                return False
        return True


"""
九章solution
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        self.lastVal = None
        self.isBST = True
        self.validate(root)
        return self.isBST

    def validate(self, root):
        if root is None:
            return
        self.validate(root.left)
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isBST = False
            return
        self.lastVal = root.val
        self.validate(root.right)


"""
recursive, 九章的思想， discussion里有人实现了
divided and conquer
"""
def isValidBST1(self, root):
    Min, Max = -(1<<31)-1, (1<<31)
    return self.helper(root, Min, Max)

def helper(self, root, Min, Max):
    if not root: # root is None
        return True
    if not root.left and not root.right: # root has no leaf
        if Min < root.val < Max:
            return True
        else:
            return False
    if not root.left and root.right: # root only has right leaf
        return root.val < root.right.val and self.helper(root.right, root.val, Max)
    elif root.left and not root.right: # root only has left leaf
        return root.val > root.left.val and self.helper(root.left, Min, root.val)
    else: # root has both left and right leaves
        return root.left.val < root.val < root.right.val and self.helper(root.left, Min, root.val) and self.helper(root.right, root.val, Max)


"""
A good solution
"""
import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root,-sys.maxint, sys.maxint)
    
    def valid(self,root,min,max):
        if not root:return True
        if root.val <= min or root.val >= max:
            return False
        return self.valid(root.left,min,root.val) and self.valid(root.right,root.val,max)

# similar solution but different implementation
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def valid(node, min, max):
            if not node:
                return True
            if min < node.val < max:
                return valid(node.left, min, node.val) and valid(node.right, node.val, max)
            else:
                return False
        
        return valid(root, -sys.maxint, sys.maxint)





        

        