"""
greedy:coding techqniues are used
"""
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n == 0: return 0
        points.sort(key=lambda x:x[0])
        result = 1
        for i in range(1, n):
            if points[i][0] > points[i-1][1]:
                result += 1
            else:
                points[i][1] = min(points[i-1][1], points[i][1])
        return result