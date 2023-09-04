# https://www.youtube.com/watch?v=t4J-Sp3BWh4
# chatgpt
class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
    
        # Calculate the prefix sum matrix
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = mat[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

        def get_sum(i, j, k):
            return prefix_sum[i][j] - prefix_sum[i - k][j] - prefix_sum[i][j - k] + prefix_sum[i - k][j - k]

        max_side_length = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left, right = 1, min(m - i + 1, n - j + 1)
                while left <= right:
                    mid = left + (right - left) // 2
                    if get_sum(i + mid - 1, j + mid - 1, mid) <= threshold:
                        max_side_length = max(max_side_length, mid)
                        left = mid + 1
                    else:
                        right = mid - 1
        
        return max_side_length