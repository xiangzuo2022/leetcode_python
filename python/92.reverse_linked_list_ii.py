"""
# 题目大意：将链表的[m,n]段就地逆置，一趟遍历完成。
# 解题思路：题目主要考察链表的“就地逆置”操作（不改变链表的值，只操作指针）。
# 在上述代码的基础上，将原链表经过逆置部分及其前后的链表片段拼接即可。
使用“哑节点”（dummy node），可以使代码简化。
水中的鱼的解题思路： 
分三步走
1. 找到m节点的前一个指针pre（加个safe guard可避免头指针的问题）
2. 从m节点开始往后reverse N个节点（双指针，cur，post）
3. 合并pre链表，cur链表及post链表。
这题难就难在繁琐上，要考虑各种边界条件，比如
{1,2,3}, 3,3
{1,2,3}, 1,1
{1,2,3}, 1,3
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = p = ListNode(0)
        dummy.next = head
        for _ in xrange(m-1):# 取到m前面一个是m-1，但是从0开始所以是m-2
            p = p.next
        cur= p.next
        # reverse the defined part 
        pre = None
        for _ in xrange(n-m+1):
            after = cur.next
            cur.next = pre
            pre = cur
            cur= after
        # connect three parts
        p.next.next= cur  # cur是n+1个元素， pre是第n个
        p.next = pre
       
        return dummy.next



class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0); p = dummy; dummy.next = head
        for i in range(m-1):
            p = p.next
        cur = p.next
        pre = None
        for i in range(m,n+1):
            after = cur.next
            cur.next = pre
            pre = cur
            cur = after
        p.next.next = cur
        p.next = pre
        return dummy.next


"""
九章solution
"""
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:return head
        dummy = ListNode(0);dummy.next = head; head = dummy
        for i in range(1,m):
            if not head:return None
            head = head.next
        preNode = head
        mNode = head.next
        nNode = mNode
        postNode = mNode.next
        for i in range(m,n):
            if postNode is None:return None
            tmp = postNode.next
            postNode.next = nNode
            nNode = postNode
            postNode = tmp
        mNode.next = postNode
        preNode.next = nNode
        return dummy.next


"""""""""
A more clear solution
code is very complex. I don't like it
"""""""""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m >= n or not head:return head
        dummy = ListNode(0); dummy.next = head
        m_prev = self.findKth(dummy,m-1)
        mth = m_prev.next
        nth = self.findKth(dummy,n)
        nth_next = nth.next
        nth.next = None
        m_prev.next = self.reverse(mth)
        mth.next = nth_next
        return dummy.next
        
        
    def findKth(self,head,k):
        for i in range(1,k+1):
            if not head:return None
            head = head.next
        return head
        
        
    def reverse(self,head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
    

# https://www.youtube.com/watch?v=RF_M9tX4Eag

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        leftPrev = dummy
        cur = head
        for i in range(left-1):
            leftPrev = cur
            cur = cur.next

        prev = None
        for i in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        leftPrev.next.next = cur
        leftPrev.next = prev
        return dummy.next
    
























