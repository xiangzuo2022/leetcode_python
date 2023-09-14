# https://www.youtube.com/watch?v=amvrKlMLuGY&t=17s
# Dijkstra algorithm 
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        minHeap = [[grid[0][0], 0, 0]]
        visit = set()
        direct = [[0,1],[1,0],[0,-1],[-1,0]]
        N = len(grid)

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1: # reach the dst node
                return t
            for dr, dc in direct:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or neiR == N or neiC == N or (neiR, neiC) in visit):
                    continue
                heapq.heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])
                visit.add((neiR, neiC))