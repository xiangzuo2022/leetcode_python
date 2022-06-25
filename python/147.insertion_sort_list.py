# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
把逻辑想清楚是关键；就是insertion sort的思想
"""
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
    	if not head:
    		return head
    	dummy = ListNode(0)
    	dummy.next = head
    	curr = head
    	while curr.next:
    		if curr.next.val < curr.val:
    			pre = dummy
    			while pre.next.val < curr.next.val:
    				pre = pre.next # find insertion position,从头开始loop找插入的位置
    			tmp = curr.next
    			curr.next = tmp.next
    			tmp.next = pre.next
    			pre.next = tmp
    		else:
    			curr = curr.next
    	return dummy.next


# http://www.cnblogs.com/zuoyuan/p/3700105.html





















