"""
官方题解的精髓："对于一个陆地格子的每条边，它被算作岛屿的周长当且仅当这条边为网格的边界或者相邻的另一个格子为水域"。
对于单独的格子而言，周长是4，但是当两个格子相邻时，会各自损失1的周长。
所以问题转化为 找出 岛屿格子 之间的 相邻边。
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        n,m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: # 遇到陆地,周长加4
                    res += 4
                    if i-1>=0 and grid[i-1][j] == 1: # 跟正上方陆地相邻, 减去重复的2条边
                        res -= 2
                    if j-1>= 0 and grid[i][j-1] == 1: # 跟正左方陆地相邻, 减去重复的2条边
                        res -= 2
        return res