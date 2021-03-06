# Definition for singly-linked list.
class ListNode: 
    def __init__(self, x):
        self.val = x
        self.next = None
        self.head = None

    def setNext(self,thenext):
    	self.next = thenext
       

    def add(self,item):
    	temp = ListNode(item)
    	temp.setNext(self.head)
    	self.head = temp


		


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
  def reverseList(self, head, last = None):
    if not head:
        return last
    next = head.next
    head.next = last
    return self.reverseList(next, head)




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# ************************************* The Second Time **************************
# solution with iterative: 创建before, cur, after指针。Time Complexity: O(n)
# this is the best solution
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head or not head.next:
            return head
        before = None
        cur = head
        while cur:
            after = cur.next
            cur.next = before
            before = cur
            cur = after
        return before




# Recursive
# 第三次做的时候以下代码不能通过
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def __init__(self):
        self.before = None

    def reverseList(self, head):
        if not head or head.next :
            return head
        cur = head
        if cur:
            after = cur.next
            cur.next = self.before
            self.before = cur
            cur = after
            return self.reverseList(cur)


if __name__ == '__main__':
	myList = ListNode()
	c = [1,2,3,4,5]
	for ele in c:
		myList.add(ele)


	
	a = Solution()
	prev = a.reverseList(myList)
	print prev.val


# ******* The Third Time ******
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
  def reverseList(self, head, last = None):
    if head == None: return head
    next = head.next; head.next = last
    return self.reverseList(next,last)


"""
九章solution， 听懂了九章的思路很容易写代码
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
注意return prev not head

Python迭代法：#双指针
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head   
        pre = None
        while(cur!=None):
            temp = cur.next # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre #反转
            #更新pre、cur指针
            pre = cur
            cur = temp
        return pre

Python递归法：

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        def reverse(pre,cur):
            if not cur:
                return pre
                
            tmp = cur.next
            cur.next = pre

            return reverse(cur,tmp)
        
        return reverse(None,head)





































