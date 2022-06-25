"""
要明白如何推到出来的
"""

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        f = [0] * n
        for i in range(m):
            g = [0] * n
            best = float("-inf")
            # 正序遍历
            for j in range(n):
                best = max(best, f[j] + j)
                g[j] = max(g[j], best + points[i][j] - j)
            
            best = float("-inf")
            # 倒序遍历
            for j in range(n - 1, -1, -1):
                best = max(best, f[j] - j)
                g[j] = max(g[j], best + points[i][j] + j)
            
            f = g
        
        return max(f)

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/maximum-number-of-points-with-cost/solution/kou-fen-hou-de-zui-da-de-fen-by-leetcode-60zl/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。