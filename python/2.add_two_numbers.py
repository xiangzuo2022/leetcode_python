# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0); p = dummy
        if not l1:return l2
        if not l2:return l1
        carry = 0
        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+carry)%10)
            carry = (l1.val + l2.val + carry) / 10
            l1 = l1.next; l2 = l2.next; p = p.next
            
        if l1:
            while l1:
                p.next = ListNode((l1.val+carry)%10)
                carry = (l1.val + carry)/10
                l1 = l1.next; p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val+carry)%10)
                carry = (l2.val + carry)/10
                l2 = l2.next; p = p.next
        if carry == 1: 
            p.next = ListNode(1)
        return dummy.next


# ******** The Second Time *********
"""
# This problem's solution is straightforward
# 和大数相加思路相似，用一个变量保存进位值，对两个数的每一位分别计算和，进位值作为计算下一位和的初始值。
# 只不过这里把数值存到链表里，需要增加一些对链表的操作。时间复杂度O(M + N)，空间复杂度O(1)。
This solution cannot pass the tests on leetcode !!!!!
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        dummy = ListNode(0)
        p = dummy
        flag = 0
        while l1 and l2:
            s = (l1.val + l2.val + flag) % 10
            p.next = ListNode(s)
            l1 = l1.next
            l2 = l2.next
            p = p.next
        if l2: # len(l2) > len(l1)
            while l2:
                p.next = ListNode((l2.val + flag)%10)
                flag = (l2.val + flag) / 10
                l2 = l2.next
                p = p.next
        if l1:  # len(l1) > len(l2)
            while l1:
                p.next = ListNode((l1.val+flag)%10)
                flag = (l1.val + flag) /10
                l1 = l1.next
                p = p.next
        if flag == 1:
            p.next = ListNode(1)  # 第一个元素相加 > 10
        return dummy.next
# 我对flag的值的改变有疑问

"""
#  解法二：I like this solution
这种解法很巧妙
"""
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        carry = 0
        p = dummy
        while l1 or l2 or carry:
            if l1:
                p.val += l1.val
                l1 = l1.next
            if l2:
                p.val += l2.val
                l2 = l2.next
            carry = p.val/10
            p.val = p.val % 10
            if l1 or l2 or carry:  
                p.next = ListNode(carry) # carry 的值会和l1 and l2的值相加; if l1, l2 and carry
                p = p.next                # are empty, no need to add carry's value. 
        return dummy

























