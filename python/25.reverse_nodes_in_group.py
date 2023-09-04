# 题意：把原始链表k个k个的反转，如果最后剩余的不到k个结点，那么保持不变。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverse(self,start,end):
    	newhead = ListNode(0); newhead.next = head
    	while newhead.next != end:
    		tmp = start.next
    		start.next = tmp.next
    		tmp.next = newhead.next
    		newhead.next = tmp
    	return [end,start]



    def reverseKGroup(self, head, k):
    	if head == None: return None
    	nhead = ListNode(0); nhead.next = head; start = nhead
    	while start.next:
    		end = start
    		for i in range(k-1):
    			end = end.next
    			if end.next == None:return nhead.next
    		res = self.reverse(start.next,end.next)
    		start.next = res[0]
    		start = res[1]
    	return nhead.next
	


# https://www.youtube.com/watch?v=1UOPsfP85V4
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        groupPrev = dummy # save a node one more before the group

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next # track the node right after the group

            # reverse group
            prev = kth.next
            curr = groupPrev.next # first node in the group
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

