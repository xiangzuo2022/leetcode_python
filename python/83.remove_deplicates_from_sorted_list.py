# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):

    	if not head:
    		return None
    	p1 = p2 = head
    	p2 = p2.next
    	while p2:
    		if p1.val == p2.val:
    			p2 = p2.next
    			p1.next = p2
    		else:
    			p1 = p1.next
    			p2 = p2.next
    			
    	return head

# *************** The Second Time **************
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Solution: Two pointers
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):  
        if not head: return []       
        p1 = p2 = head
        p2 = p2.next
        while p2:
            if p1.val == p2.val:
                p2 = p2.next
                p1.next = p2
            else:
                p1 = p1.next
                p2 = p2.next
        return head


"""
九章的解法：head 不会被删所以不用dummy， 但是head要保存一下， 以便返回用
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head             
          










