class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        counter = 0
        results = sorted(heights)
        for i in range(len(results)):
            if heights[i] != results[i]:
                counter += 1
        return counter