"""
O(n) running time
using hash table
"""


class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = {}
        n = len(A)
        res = []
        for j in range(n):
            d[B[j]] = j
        for a in A:
            res.append(d[a])
        return res