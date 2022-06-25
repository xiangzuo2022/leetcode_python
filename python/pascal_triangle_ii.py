"""based on the solution of 118
"""

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        a = [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(2,rowIndex+1):
            for j in range(1,i):
                a[i][j] = a[i-1][j-1] + a[i-1][j]
                
        return a[rowIndex]
    	


# ********* The third time ***********
# 注意一下index的范围
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(1,i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans[rowIndex]