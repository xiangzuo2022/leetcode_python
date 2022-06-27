"""
similar Leetcode 160
this one has a parent pointer
O(logN) time complexity and storage complexty
store all of p's paths to a set and to see whether q's path is in it. 
"""
class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        path = set()
        while p:
            path.add(p)
            p = p.parent
        while q not in path:
            q = q.parent 
        return q
        
"""
solution 2
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
            
        return p1