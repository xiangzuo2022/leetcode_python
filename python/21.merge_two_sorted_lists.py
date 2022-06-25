# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Solution: using extra space, build a new empty linklist to store merged results
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
    	if l1 == None: return l2
    	if l2 == None: return l1
    	dummy = ListNode(0)
    	tmp = dummy
    	while l1 and l2:
    		if l1.val <= l2.val:
    			tmp.next = l1
    			l1 = l1.next
    			tmp = tmp.next
    		else:
    			tmp.next = l2
    			l2 = l2.next
    			tmp = tmp.next
    	if l2 == None:
    		tmp.next = l1
    	if l1 == None:
    		tmp.next = l2
    	return dummy.next

