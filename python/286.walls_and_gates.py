"""
这道题类似一种迷宫问题，规定了-1表示墙，0表示门，让求每个点到门的最近的曼哈顿距离，这其实类似于求距离场Distance Map的
问题，那么我们先考虑用DFS来解，思路是，我们搜索0的位置，每找到一个0，以其周围四个相邻点为起点，开始DFS遍历，
并带入深度值1，如果遇到的值大于当前深度值，我们将位置值赋为当前深度值，并对当前点的四个相邻点开始DFS遍历，
注意此时深度值需要加1，这样遍历完成后，所有的位置就被正确地更新了
"""
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        h = len(rooms)
        w = len(rooms[0])
        
        q = []
        for i in range(h):
            for j in range(w):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        for row, col in q:
            dist = rooms[row][col] + 1
            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = row + dy
                c = col + dx
                if 0 <= r < h and 0 <= c < w and rooms[r][c] == 2147483647:
                    rooms[r][c] = dist
                    q.append((r,c))
