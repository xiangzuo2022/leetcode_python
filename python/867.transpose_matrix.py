"""
The main idea is making a copy of the original matrix and need to be careful about 2D matrix definition.
"""

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        M, N = len(A), len(A[0])
        B = [[0 for x in range(M)] for y in range(N)]
        for i in range(N):
            for j in range(M):
                B[i][j] = A[j][i]
        return B