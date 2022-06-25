# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head): 
    	if not head or not head.next:
    		return head
    	dummy = ListNode(0); dummy.next = head
    	p = dummy
    	while p.next and p.next.next:
    		tmp = p.next.next
    		p.next.next = tmp.next
    		tmp.next = p.next
    		p.next = tmp
    		p = p.next.next
    	return dummy.next	
    	
    	
"""
My own solution, swap values instead of pointers
"""
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        p = head
        while p and p.next:
            p.val, p.next.val = p.next.val, p.val
            p = p.next.next
        return 
      
"""
The figure is more clear to demo the process
https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/dai-ma-sui-xiang-lu-24-liang-liang-jiao-xzkrz/
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0) #设置一个虚拟头结点
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next: 
            tmp = cur.next #记录临时节点
            tmp1 = cur.next.next.next #记录临时节点
            
            cur.next = cur.next.next          #步骤一
            cur.next.next = tmp               #步骤二
            cur.next.next.next = tmp1         #步骤三
            
            cur = cur.next.next #cur移动两位，准备下一轮交换
        return dummy.next