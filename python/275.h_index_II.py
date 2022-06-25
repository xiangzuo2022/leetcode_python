class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        h = 0
        for i in range(n):
            currentH = min(citations[i], n-i)
            h = max(h, currentH)
        return h
