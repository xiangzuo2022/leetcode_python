# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
    	if k == 0 or not head:
    		return head
    	dummy = ListNode(0)
    	dummy.next = head
    	p = dummy
    	count = 0
    	while p.next:
    		p = p.next
    		count += 1
    	p.next = dummy.next
    	step = count - (k%count)
    	for i in range(step):
    		p = p.next
    	head = p.next
    	p.next = None
    	return head



"""
# ***************** The Second Time **************
# 解题思路：循环右移一条链表，比如k=2，（1，2，3，4，5）循环右移两位变为（4，5，1，2，3）。
# 由于k值有可能比链表长度大很多，所以先要用一个count变量求出链表的长度。而k%count就是循环右移的步数。
水中的鱼的思路：
首先从head开始跑，直到最后一个节点，这时可以得出链表长度len。然后将尾指针指向头指针，将整个圈连起来，
接着往前跑len – k%len，从这里断开，就是要求的结果了。
这个思路很清楚的解决了我以前的困惑;k可以大于链表长度
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if k == 0 or head == None: return head
        dummy = ListNode(0); dummy.next = head
        p = dummy
        count = 0
        while p.next:
            p = p.next
            count += 1
        p.next = dummy.next (p.next = head)  # 这里不是重新回到起点而是将为指针指向头指针， 将整个圈起来
        step = count - k % count # 右移 k 位 means p has to be in the position of count - k
        for i in range(0,step):  # because the next position will be the head
            p = p.next
        head = p.next   # 用dummy的原因是方便处理head
        p.next = None
        return head






























