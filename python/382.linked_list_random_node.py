class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res = None
        node = self.head
        index = 0
        while node:
            if random.randint(0, index) == 0:
                res = node.val
            node = node.next
            index += 1
        return res

        水池抽样算法