"""
思路是遍历链表，找到右起第一个不为9的数字，如果找不到这样的数字，说明所有数字均为9，那么在表头新建一个值为0的新节点，进行加1处理，然后把右边所有的数字都置为0即可。
举例来说：

比如1->2->3，那么第一个不为9的数字为3，对3进行加1，变成4，右边没有节点了，所以不做处理，返回1->2->4。

再比如说8->9->9，找第一个不为9的数字为8，进行加1处理变成了9，然后把后面的数字都置0，得到结果9->0->0。

再来看9->9->9的情况，找不到不为9的数字，那么再前面新建一个值为0的节点，进行加1处理变成了1，把后面的数字都置0，得到1->0->0->0。
"""
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        start = end = dummy
        
        # start stops at the last non-9 digit, end loops over all
        while end.next:
            end = end.next
            if end.val != 9:
                start = end
                
        start.val += 1 # Plus One to start and set the rest 0
        while start.next:
            start = start.next
            start.val = 0
        
        return dummy if dummy.val == 1 else dummy.next