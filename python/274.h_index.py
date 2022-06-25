"""
discussion solution: O(nlogn) mainly used for sorting.
O(n * logn) 排序 + 遍历
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        for i, c in enumerate(sorted(citations)):
            if N - i <= c: # <= can get the maximum value
                return N-i
        return 0


"""
cannot use sorted(citations) as the original values are not changed
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations.sort()
        hindex = 0
        for i in range(n):
            currentH = min(n-i, citations[i])
            if currentH > hindex:
                hindex = currentH
        return hindex
