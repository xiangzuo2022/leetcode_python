# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    

    def buildTree(self, preorder, inorder):
    	if not inorder:return None
    	root = TreeNode(preorder[0])
    	rootPos = inorder.index(preorder[0])    	
    	root.left = self.buildTree(preorder[1:1+rootPos],inorder[:rootPos])
    	root.right = self.buildTree(preorder[rootPos+1:],inorder[rootPos+1:])
    	return root

# 答案都是内存错误
# 解题思路：http://fisherlei.blogspot.com/2013/01/leetcode-construct-binary-tree-from.html

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        # using dictionary for index lookup improves the performance of algorithm from O(N^2) to O(N), where N = |preorder|
        lookup = {}
        for i in range(len(inorder)):
            lookup[inorder[i]] = i 
        return self.buildTreeRecur(lookup, preorder, inorder, 0, len(preorder) - 1, 0)
        
    def buildTreeRecur(self, lookup, preorder, inorder, in_start, in_end, pre_start):
        if in_start > in_end:
            return None
        current = TreeNode(preorder[pre_start])
        i = lookup[preorder[pre_start]]
        current.left = self.buildTreeRecur(lookup, preorder, inorder, in_start, i - 1, pre_start + 1)
        current.right = self.buildTreeRecur(lookup, preorder, inorder, i + 1, in_end, pre_start + i - in_start + 1)
        return current

"""
上个很吊的解法， 秒杀上面所有解法， 很clever的递归
""" 

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:return None
        root = TreeNode(preorder.pop(0))
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder,inorder[:index])
        root.right = self.buildTree(preorder,inorder[index+1:]) #当左边执行完了后才会执行右边
        return root

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
        mid = inorder.index(preorder[0])
        # 构建左子树
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # 构建右子树
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root









