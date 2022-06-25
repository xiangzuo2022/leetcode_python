# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        pa,pb = headA, headB

        while pa != pb:
        	if pa is None:
        		pa = headB
        	else:
        		pa = pa.next
        	if pb is None:
        		pb = headA
        	else:
        		pb = pb.next
      	return pa # return pa or pb either one is fine.


# *************** The Second Time ***************
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
# 双指针解法 (O(n+m) 时间, O(1) 空间):
# 维护两个指针pA和pB，初始分别指向A和B。然后让它们分别遍历整个链表，每步一个节点。
# 当pA到达链表末尾时，让它指向B的头节点（没错，是B）；类似的当pB到达链表末尾时，重新指向A的头节点。
# 如果pA在某一点与pB相遇，则pA/pB就是交点。
# 下面来看下为什么这个算法可行，考虑两个链表：A = {1,3,5,7,9,11} B = {2,4,9,11}，它们的交点是节点'9'。
# 由于B的长度是4 小于 A的长度6，pB会首先到达链表的末尾，由于pB比pA恰好少走2个节点。通过把pB指向A的头，
# 把pA指向B的头，我们现在让pB比pA恰好多走2个节点。所以在第二轮，它们可以保证同时在交点相遇。
# 如果两个链表有交点，则它们的最后一个节点一定是同一个节点。所以当pA/pB到达链表末尾时，分别记录下A和B的
# 最后一个节点。如果两个链表的末尾节点不一致，说明两个链表没有交点。
# This solution is smart. 
# http://bookshadow.com/weblog/2014/12/04/leetcode-intersection-two-linked-lists/
"""



class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):       
        p1 = headA
        p2 = headB 
        while p1 != p2:
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next
        return p1     
        

"""
# Solution 2: 哈希表解法（O(n+m) 时间, O(n) or O(m) 空间）
# 遍历链表A并将每个节点的地址/引用存储在哈希表中。然后检查链表B中的每个节点bi：
# 如果bi出现在哈希表中，则bi就是交点。
"""

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        d = {}
        while headA:
            d[headA.val] = 1
            headA = headA.next
        while headB:
            if headB.val in d:
                return headB
            else:
                headB = headB.next








        


if __name__ == '__main__':
	headA = ListNode(1)
	headB = ListNode(1)
	a = Solution()
	print a.getIntersectionNode(headA,headB)

   
  


