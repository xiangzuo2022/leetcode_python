"""
首先，比较直观的是，先使用Linked List Cycle I的办法，判断是否有cycle。如果有，则从头遍历节点，对于每一个节点，
查询是否在环里面，是个O(n^2)的法子。但是仔细想一想，发现这是个数学题。
"""
class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
    	if not head or head.next:
    		return False
    	slow = fast = head
    	while fast and fast.next:
    		slow = slow.next
    		fast = fast.next.next
    		if slow == fast:
    			break
    	if slow == fast:
    		slow = head
    		while slow != fast:
    			slow = slow.next
    			fast = fast.next
    		return slow
    	return None


"""
思路： 相遇后把slow拉回到head;两个指针相遇以后，再往下走X步就回到Cycle的起点了
# a good exploration: http://www.cnblogs.com/zuoyuan/p/3701877.html
# 链表中存在环路的同时还可以有其他非环路存在
水中的鱼的讲解：http://fisherlei.blogspot.com/2013/11/leetcode-linked-list-cycle-ii-solution.html
"""

#  ************ The Second Time ************
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: break
        if fast == slow:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None
      
      
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果相遇
            if slow == fast:
                p = head
                q = slow
                while p!=q:
                    p = p.next
                    q = q.next
                #你也可以return q
                return p

        return None















