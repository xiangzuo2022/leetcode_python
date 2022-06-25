# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedArraryToBST(self,array):  # 注意要处理length， 递归会造成None的结果
    	lengh = len(array)
    	if length == 0:
    		return None
    	if length == 1:
    		return TreeNode(array[0])
    	root = TreeNode(array[length/2])
    	root.left = self.sortedArraryToBST(array[:length/2])
    	root.right = self.sortedArraryToBST(array[length/2+1:])
    	return root

    def sortedListToBST(self, head):
    	array = []
    	p = head
    	while p:
    		array.append(p.val)
    		p = p.next
    	return self.sortedArraryToBST(array)


# ************* The Second Time *************
"""
# 先把链表转成数组，再递归。每次数组的中点元素为root, 再递归地建立左右子树。
能够想出来， 但完成写出来还有问题
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        left = 0; right = len(nums)-1
        return self.buildBST(nums,left,right)

    def buildBST(self,nums,left,right):
        if left > right: return None        
        mid = (left+right)/2        
        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums,left,mid-1)
        root.right = self.buildBST(nums,mid+1,right)
        return root



"""
My own solution: convert the linked list into an array, then process the array is much
easier. 
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        p = head; a = []
        while p:
            a.append(p.val)
            p = p.next
        if not head or not head.next: return head
        
        l = 0; r = len(a)-1
        return self.build(0,r,a)
            
    def build(self,l,r,a):
        
        if l <= r:
            mid = (l+r)/2
            root = TreeNode(a[mid])
            root.left = self.build(l,mid-1,a)
            root.right = self.build(mid+1,r,a)
            return root
        return None


"""
不用数组的解法：用快慢指针处理起来会复杂些;要清楚头和尾不是都是None
"""
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """       
       
        if not head:
            return None

        return self.generate(head,None)

    def generate(self, head,tail):
        
        slow = fast = head
        while fast!=tail and fast.next!=tail :
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)
        if head == slow:
            root.left = None
        else:
            root.left = self.generate(head,slow)
            
        if slow.next == tail:
            root.right = None
        else:
            root.right = self.generate(slow.next,tail)
        return root


"""
此题的挑战是用O(n)不是用O(nlogn)
"""
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """        
        self.current = head
        size = self.getSize(head)
        return self.helper(size)

    def getSize(self,head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size

    def helper(self,size):
        if size == 0:return None
        left = self.helper(size/2)
        root = TreeNode(self.current.val)
        self.current = self.current.next
        right = self.helper(size-1-size/2)
        root.left = left
        root.right = right
        return root


























