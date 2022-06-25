class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m = len(grid); n = len(grid[0])
        row = []; col = []; result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)
        col.sort()
        median_row = row[len(row)/2]
        median_col = col[len(col)/2]
        
        for i in row:
            result += abs(i-median_row)
        for i in col:
            result += abs(i-median_col)
        return result