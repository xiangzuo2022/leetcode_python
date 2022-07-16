"""
a video explains https://www.youtube.com/watch?v=S8ZjuH_sFT0
"""

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
		# case 1:
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        # prev ans succ
        prev = head
        succ = head.next 
        
        while True:
            
            # case2: 1-->3 insert 2, 1 -->2 -->3
            if prev.val <= insertVal <=succ.val:
                break            
            
            # case 3: 5-->1 insert 7, 5-->7-->1
            if prev.val > succ.val and (insertVal > prev.val or insertVal < succ.val):
                break
                
            prev, succ = succ, succ.next
            # case 4: else 3-->3-->3 insert 4, 3-->3-->3-->4
            if prev == head:
                break
        new_node = Node(insertVal)
        new_node.next = succ
        prev.next = new_node
        return head