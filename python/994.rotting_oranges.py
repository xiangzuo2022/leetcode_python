"""
解题思路：广度优先搜索（BFS）
首先分别将腐烂的橘子和新鲜的橘子保存在两个集合中；

模拟广度优先搜索的过程，方法是判断在每个腐烂橘子的四个方向上是否有新鲜橘子，如果有就腐烂它。每腐烂一次时间加 11，并剔除新鲜集合里腐烂的橘子；

当橘子全部腐烂时结束循环。

作者：z1m
链接：https://leetcode-cn.com/problems/rotting-oranges/solution/yan-du-you-xian-sou-suo-python3-c-by-z1m/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] ==2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] ==1}
        time = 0
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
       
        while fresh:
            if not rotten: return -1
            rotten = {(i+di, j+dj) for i,j in rotten for di, dj in directions if (i+di, j+dj) in fresh}
            fresh -= rotten
            time += 1
        return time
    
# https://www.youtube.com/watch?v=y704fEOx0s0
# mutisource BFS is the solution; DFS cannot get the shortedst time units
# time complexity O(n*m) and memory O(n*m)
# the stopping condition is fresh oranges == 0, NOT the queue is empty. Because the fresh orange can be in the corner that no rotten
# orange can infect it.
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()        
        time, fresh = 0, 0
        direct = [[0, 1],[1, 0],[0, -1],[-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        # get number of fresh oranges and put rotten oranges in the queue
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direct:
                    row, col = r + dr, c + dc
                    # if in bounds and fresh, make rotten
                    if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    q.append([row, col])
            time += 1
        return time if fresh == 0 else -1
