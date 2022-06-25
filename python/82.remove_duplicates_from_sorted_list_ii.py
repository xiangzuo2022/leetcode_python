"""
# 基本链表题， 用两个指针， 一个dummy (因为head可能去掉所以用dummy)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
    	if head==None or head.next==None : return head
    	dummy = ListNode(0); dummy.next = head  # 学会这种方法
    	p1 = dummy; p2 = dummy.next   # 两个指针相邻 	
    	while p1.next:
    		while p2.next and p2.next.val == p1.next.val: #技巧在比较的是next， 这样就不需要pre了 (精妙！！)
    			p2 = p2.next  # 相等时， p2移动， p1不动
    		if p2 == p1.next:
    			p1 = p1.next
    			p2 = p2.next
    		else:
    			p1.next = p2.next
    	return dummy.next


###### The third time ##################
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        dummy = ListNode(0); dummy.next = head
        p1 = dummy; p2 = dummy.next
        while p1.next:
            while p2.next and p2.next.val == p1.next.val:
                p2 = p2.next
            if p2 == p1.next:
                p1 = p1.next
                p2 = p2.next
            else:
                p1.next = p2.next
        return dummy.next


"""
更好懂得解法：但是判断为空老是写不对
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        dummy.next = head
        
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val: #重复一遍条件是要保证每次循环这些条件都满足
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next

"""
技巧在比较的是next，如果是比较next则判断条件是p.next 不要为空
思想简单，代码细节复杂
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        dummy = ListNode(0);dummy.next = head;p=dummy
        while p.next and head.next:
            if p.next.val == head.next.val:
                while p and head.next and p.next.val == head.next.val: # p不动,head动所以判断p和head.next
                    head = head.next
                head = head.next #这两个的顺序容易错,完了之后两个指针都要挪动
                p.next = head
            else: 
                head = head.next
                p = p.next
        return dummy.next


"""
一个指针的做法：边删除边比较的方法， 只用一个指针
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        dummy = ListNode(0);dummy.next = head;head = dummy #head又指回去了， 这样一个指针就够了
        while head.next and head.next.next:
            if head.next.val == head.next.next.val:
                tmp = head.next.val
                while head.next and head.next.val == tmp:
                    head.next = head.next.next
            else:
                head = head.next
        return dummy.next


































