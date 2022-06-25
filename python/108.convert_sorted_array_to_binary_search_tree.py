# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
    	length = len(nums)
    	if length == 0 :
    		return None
    	if length == 1:
    		return TreeNode(nums[0])
    	root = TreeNode(nums[length/2])
    	root.left = self.sortedArrayToBST(nums[:length/2])
    	root.right = self.sortedArrayToBST(nums[length/2+1:])
    	return root

# 解题思路：两个思路：一，可以使用快慢指针来找到中间的那个节点，然后将这个节点作为树根，并分别递归这个节
# 点左右两边的链表产生左右子树，这样的好处是不需要使用额外的空间，坏处是代码不够整洁。二，将排序好的链表
# 的每个节点的值存入一个数组中，这样就和http://www.cnblogs.com/zuoyuan/p/3722103.html这道题一样
# 了，代码也比较整洁。

# 一下代码 Time Limit Exceed
# 已经是排序了的arrary还用的着这么费劲吗？？？
class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        length = len(nums)
        if length == 0 :
            return None
        if length == 1:
            return TreeNode(nums[0])
        left = 0 ; right = len(nums)
        mid = (left + right)/2
        self.root = TreeNode(nums[mid])
        self.search(left,right,nums)
        return self.root

    def search(self,left,right,nums):
        while left < right:
            mid = (left + right)/2
            #root = TreeNode(nums[mid])
            self.root.left = self.search(left,mid-1,nums)
            self.root.right = self.search(mid+1,right,nums)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # inorder traversal: left -> node -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        
        return helper(0, len(nums) - 1)

作者：LeetCode
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/jiang-you-xu-shu-zu-zhuan-huan-wei-er-cha-sou-s-15/


















