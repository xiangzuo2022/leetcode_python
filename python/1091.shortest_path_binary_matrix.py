"""
解题思路
典型的BFS最短路径问题，用DFS也可以求解，但是容易超时。

在二维矩阵中搜索，什么时候用BFS，什么时候用DFS？
1.如果只是要找到某一个结果是否存在，那么DFS会更高效。因为DFS会首先把一种可能的情况尝试到底，才会回溯去尝试下一种情况，只要找到一种情况，就可以返回了。但是BFS必须所有可能的情况同时尝试，在找到一种满足条件的结果的同时，也尝试了很多不必要的路径；
2.如果是要找所有可能结果中最短的，那么BFS回更高效。因为DFS是一种一种的尝试，在把所有可能情况尝试完之前，无法确定哪个是最短，所以DFS必须把所有情况都找一遍，才能确定最终答案（DFS的优化就是剪枝，不剪枝很容易超时）。而BFS从一开始就是尝试所有情况，所以只要找到第一个达到的那个点，那就是最短的路径，可以直接返回了，其他情况都可以省略了，所以这种情况下，BFS更高效。

BFS解法中的visited为什么可以全局使用？
BFS是在尝试所有的可能路径，哪个最快到达终点，哪个就是最短。那么每一条路径走过的路不同，visited（也就是这条路径上走过的点）也应该不同，那么为什么visited可以全局使用呢？
因为我们要找的是最短路径，那么如果在此之前某个点已经在visited中，也就是说有其他路径在小于或等于当前步数的情况下，到达过这个点，证明到达这个点的最短路径已经被找到。那么显然这个点没必要再尝试了，因为即便去尝试了，最终的结果也不会是最短路径了，所以直接放弃这个点即可。

"""
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        

# https://www.youtube.com/watch?v=YnxUdAO7TAo
# O(n^2) BFS
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        direct = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        q = deque([(0, 0, 1)])
        visit = set((0, 0))

        while q:
            r, c, length = q.popleft()
            if (min(r, c) < 0 or max(r, c) == N or grid[r][c]):
                continue
            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in direct:
                if (r+dr, c+dc) not in visit:
                    q.append((r+dr, c+dc, length+1))
                    visit.add((r+dr, c+dc))
        return -1