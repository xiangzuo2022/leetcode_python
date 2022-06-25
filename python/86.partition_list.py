# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
    	head1 = ListNode(0)
    	head2 = ListNode(0)
    	p1 = head1
    	p2 = head2
    	tmp = head
    	while tmp:
    		if tmp.val < x:
    			p1.next = tmp
    			tmp = tmp.next
    			p1 = p1.next
    			p1.next = None
    		else:
    			p2.next = tmp
    			tmp = tmp.next
    			p2 = p2.next
    			p2.next = None
    	p1.next = head2.next
    	head = head1.next
    	return head




# ******** The Second Time ********
"""
# 解题思路：解决链表问题时，最好加一个头结点，问题会比较好解决。对这道题来说，创建两个头结点head1和head2，
# head1这条链表是小于x值的节点的链表，head2链表是大于等于x值的节点的链表，然后将head2链表链接到head链表
# 的尾部即可。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        head1 = ListNode(0); head2 = ListNode(0) # 没有另开空间新建链表， 只是新建两个节点
        tmp = head
        p1 = head1; p2 = head2
        while tmp:
            if tmp.val < x:
                p1.next = tmp
                tmp = tmp.next
                p1 = p1.next
                p1.next = None # if no this line then it is not an independent linkedlist
            else:
                p2.next = tmp
                tmp = tmp.next
                p2 = p2.next
                p2.next = None # if no this line then it is not an independent linkedlist
        p1.next = head2.next
        head = head1.next
        return head
 # 这个题其实蛮有意思的



####################  The third time  ###################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1 = ListNode(0); head2 = ListNode(0)
        tmp = head
        p1 = head1; p2 = head2
        while tmp:
            if tmp.val < x:
                p1.next = tmp
                tmp = tmp.next
                p1 = p1.next
                p1.next = None
            else:
                p2.next = head2
                tmp = tmp.next
                p2 = p2.next
                p2.next = None
        p1.next = head2.next
        head = head1.next
        return head



"""
我自己的写法更简洁
"""
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:return head
        dummy1 = ListNode(0); dummy2 = ListNode(0)
        p1 = dummy1; p2 = dummy2
        while head:
            if head.val < x:
                p1.next = head
                head = head.next
                p1 = p1.next
                p1.next = None
            else:
                p2.next = head
                head = head.next
                p2 = p2.next
                p2.next = None       
        p1.next = dummy2.next
        return dummy1.next


"""
九章solution， 思路很清晰
"""
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        mid = self.findMiddle(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge(left,right)
        
    def merge(self,head1,head2):
        dummy = ListNode(0);p = dummy
        while head1 and head2:
            if head1.val < head2.val:
                p.next = head1
                head1 = head1.next
                p = p.next
            else:
                p.next = head2
                head2 = head2.next
                p = p.next
        if head1:
            p.next = head1
        if head2:
            p.next = head2
        return dummy.next
        
    def findMiddle(self,head):
        slow = head;fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow






















