"""
O(m+n):有个规律凡是左边上面的都小于当前值， 右边下面的都大于当前值
jiuzhang视频讲解有binary search 
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix); m = len(matrix[0])
        # from bottom left to top right
        x = n - 1; y = 0
        while x >= 0 and y < m:
            if matrix[x][y] < target:
                y += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                return True
        return False