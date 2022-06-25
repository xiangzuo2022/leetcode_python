"""
O(nlgn)的排序算法没几个，无非就是quick sort， heap sort和merge sort. 对于链表排序来说，
难点之一就是如何O(1)定位节点。如果是数组，那么可以通过下标直接找到节点，但是对于链表，很明显没有下标这个东西可以用，
如果需要定位到第k个元素，只能从节点头部顺序的访问K次，但是，如果排序中每一个定位操作都要这样做的话，就太慢了。
所以，问题其实就是，如何能够节省链表节点的定位时间。如果采用merge sort的话，就可以通过递归的特性来避免这个时间损耗
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    
	def merge(self, head1, head2):
		if head1 == None: return head2
		if head2 == None: return head1
		dummy = ListNode(0)                             #归并时，新建一个链表头结点
		p = dummy
		while head1 and head2:
		    if head1.val <= head2.val:
		        p.next = head1
		        head1 = head1.next
		        p = p.next
		    else:
		        p.next = head2
		        head2 = head2.next
		        p = p.next
		if head1 == None:
		    p.next = head2
		if head2 == None:
		    p.next = head1
		return dummy.next
        
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        slow = head 
        fast = head                        #快慢指针技巧的运用，用来截断链表。
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None                                #head1和head2为截为两条链表的表头
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)
        return head



# ************* The Second Time ***********
"""
# 解题思路：由于题目对时间复杂度和空间复杂度要求比较高，所以查看了各种解法，最好的解法就是归并排序，
# 由于链表在归并操作时并不需要像数组的归并操作那样分配一个临时数组空间，所以这样就是常数空间复杂度了，
# 当然这里不考虑递归所产生的系统调用的栈。这里涉及到一个链表常用的操作，即快慢指针的技巧。设置
# slow和fast指针，开始它们都指向表头，fast每次走两步，slow每次走一步，fast到链表尾部时，
# slow正好到中间，这样就将链表截为两段。
# 时间复杂度O(nlogn)，空间复杂度O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def merge(self,head1,head2):
        if head1 == None: return head2
        if head2 == None: return head1
        dummy = ListNode(0)
        p = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                p.next = head1
                head1 = head1.next
                p = p.next
            else:
                p.next = head2
                head2 = head2.next
                p = p.next
        if head1 == None:
            p.next = head2
        if head2 == None:
            p.next = head1
        return dummy.next


    def sortList(self, head):
        if head == None or head.next == None: return head
        slow = head; fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None  # 容易忘记这一步
        head1 = self.sortList(head1)  # key step recursive
        head2 = self.sortList(head2)
        head = self.merge(head1,head2)
        return head














