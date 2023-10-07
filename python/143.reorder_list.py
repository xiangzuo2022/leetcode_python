"""
# 解题思路：
# 1，先将链表截断为两个相等长度的链表，如果链表长度为奇数，则第一条链表长度多1。如原链表为
#   L={1,2,3,4,5}，那么拆分结果为L1={1,2,3}；L2={4,5}。拆分的技巧还是快慢指针的技巧。
# 2，将第二条链表L2翻转，如将L2={4,5}翻转为L2={5,4}。
# 3，按照题意归并链表。
# 解题思路：
# 1. 利用快慢指针找到链表中点mid，将链表分为左右两半
# 2. 将链表的右半部分就地逆置
# 3. 合并链表的左右两部分
第一个解法比较容易懂
这题考察了3个链表的操作
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):

        if head==None or head.next==None or head.next.next==None: 
        	return head
        
        # break linked list into two equal length
        slow = fast = head                              #快慢指针技巧
        while fast and fast.next:                       #需要熟练掌握
            slow = slow.next                            #链表操作中常用
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # reverse linked list head2
        dummy=ListNode(0); dummy.next=head2             #翻转前加一个头结点
        p=head2.next; head2.next=None                   #将p指向的节点一个一个插入到dummy后面
        while p:                                        #就完成了链表的翻转
            tmp=p; p=p.next                             #运行时注意去掉中文注释
            tmp.next=dummy.next
            dummy.next=tmp
        head2=dummy.next

        # merge two linked list head1 and head2
        p1 = head1; p2 = head2
        while p2:
            tmp1 = p1.next; tmp2 = p2.next
            p1.next = p2; p2.next = tmp1
            p1 = tmp1; p2 = tmp2


# ******** The Second Time *********
"""
# 解题思路：
# 1，先将链表截断为两个相等长度的链表，如果链表长度为奇数，则第一条链表长度多1。如原链表为
#   L={1,2,3,4,5}，那么拆分结果为L1={1,2,3}；L2={4,5}。拆分的技巧还是快慢指针的技巧。
# 2，将第二条链表L2翻转，如将L2={4,5}翻转为L2={5,4}。
# 3，按照题意归并链表。
# 解题思路：
# 1. 利用快慢指针找到链表中点mid，将链表分为左右两半
# 2. 将链表的右半部分就地逆置
# 3. 合并链表的左右两部分

"""




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorder(self,head):
        if head == None:
            return 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        begin = head
        end = mid
        pre = None

        while end :
            tmp = end.next
            end.next = pre
            pre = end
            end = tmp
        while pre and begin:
            a = pre.next
            b = begin.next
            begin.next = pre
            pre.next = b
            begin = b
            pre = a 
        return 




"""
九章solution 思路清晰
"""
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:return
        mid = self.findMiddle(head)
        t = mid.next
        mid.next = None
        head2 = self.reverse(t)
        self.merge(head,head2)
        
        
    
    
    def findMiddle(self,head):
        slow = head; fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def reverse(self,head):
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre
    
    def merge(self,head1,head2):
        i = 0;dummy = ListNode(0);p = dummy
        while head1 and head2:
            if i % 2 == 0:
                p.next = head1
                p = p.next
                head1 = head1.next
            else:
                p.next = head2
                p = p.next
                head2 = head2.next
            i += 1
        if head1:
            p.next = head1
        if head2:
            p.next = head2
        return dummy.next
                

# https://www.youtube.com/watch?v=S5bfdUTrKLM
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2































            
