"""
# 典型的使用heap数据结构的题目
# 解题思路：归并k个已经排好序的链表。使用堆这一数据结构，首先将每条链表的头节点进入堆中，
# 然后将最小的弹出，并将最小的节点这条链表的下一个节点入堆，依次类推，最终形成的链表就是归并好的链表。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node: 
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0); curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next: 
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next
"""
# 用最小堆, 每个list有一个指针, k个指针放入堆中, 每次pop出最小的, 然后指向相应list的下一个node, 再push入堆。
# 最小堆是一个数组, 所有元素满足heap[k] <= heap[2*k+1]和heap[k] <= heap[2*k+2], heap[0]即堆顶最小。
# Python堆操作真方便:
# heapq.heapify(a) 把list a中元素调换顺序使其成为最小堆, a还是list
# heapq.heappush(a, (10, sth_else))  把(10, sth_else)插入堆a中, a仍为最小堆, 也可以只插入数10
# heapq.heappop(a) 弹出堆顶元素, a中的最小值
# heapq.heappushpop(a, (10, sth_else)) 先push再pop, 效率比依次调用heappush()和heappop()高 
"""















