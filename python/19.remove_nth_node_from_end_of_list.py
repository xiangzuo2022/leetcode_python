# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
    	dummyHead = ListNode(0)   # what does ListNode(0) mean?
        dummyHead.next = head
        slow = fast = dummyHead

        for i in range(n):  # move to the deletion position
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummyHead.next


# ********************** The Second Time ***************
"""
# solution: using two pointers, one moves n steps first and then two move together. 
# When the first pointer reaches the end of the list, the position of the second pointer
# is where we need to delete the element.
"""

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        for i in range(n):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next



# ************ My own solution *************
# two pointers
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: return head
        if not head.next and n ==1:return []
        dummy = ListNode(0); p = dummy; dummy.next = head
        
        while p:
            p1 = p
            for i in range(n):
                p1 = p1.next
            if p1.next == None:
                p.next = p.next.next
                return dummy.next
            else:
                p = p.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head_dummy = ListNode()
        head_dummy.next = head

        slow, fast = head_dummy, head_dummy
        while(n!=0): #fast先往前走n步
            fast = fast.next
            n -= 1
        while(fast.next!=None):
            slow = slow.next
            fast = fast.next
        #fast 走到结尾后，slow的下一个节点为倒数第N个节点
        slow.next = slow.next.next #删除
        return head_dummy.next


















