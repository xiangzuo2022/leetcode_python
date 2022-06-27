"""
a simple solution with stack
"""
class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        ans = []
        for index, val in enumerate(heights):            
            while ans and heights[ans[-1]] <= val:
                ans.pop()
            ans.append(index)
        return ans

"""
improve the time complexity to O(N)
use maxVal to record the max value and update it when loop the array
need to begin from the end of the array
"""
class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        ans = [n-1]
        maxVal = heights[n-1]
        for i in range(n-1, -1, -1):
            if heights[i] > maxVal:
                ans.append(i)
                maxVal = heights[i]
        return ans[::-1]