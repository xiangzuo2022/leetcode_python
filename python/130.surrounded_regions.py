"""
# 思路：目标是要找到由X包围起来的O的区域。
# 首先，外围一圈上的O肯定会保留下来。然后，从外围的O能达到的O也要保留。剩下其他的O就是内部的O。
# 所以方法就是从外围的一圈进行DFS算法：依次对外圈的“O”做DFS，将其可以到达O临时设置为#。
# 特殊用例：只有外围轮廓没有内部。比如长或者宽小于2，此时不存在被包围的'X'。
# 南郭的解题思路：这道题可以使用BFS和DFS两种方法来解决。DFS会超时。BFS可以AC。从边上开始搜索，如果是'O'，
# 那么搜索'O'周围的元素，并将'O'置换为'D'，这样每条边都DFS或者BFS一遍。而内部的'O'是不会改变的。
# 这样下来，没有被围住的'O'全都被置换成了'D'，被围住的'O'还是'O'，没有改变。然后遍历一遍，
# 将'O'置换为'X'，将'D'置换为'O'。
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def fill(x, y):
            if x<0 or x>m-1 or y<0 or y>n-1 or board[x][y] != 'O': return
            queue.append((x,y))
            board[x][y]='D'

        def bfs(x, y):
            if board[x][y]=='O':
				queue.append((x,y))
				fill(x,y)
            for i, j in queue:               
                fill(i+1,j)
                fill(i-1,j)
                fill(i,j+1)
                fill(i,j-1)

        if len(board)==0: return
        m=len(board); n=len(board[0]); queue=[]
		# 从四边开始找 0
        for i in range(n):
            bfs(0,i)  # first row
            bfs(m-1,i) # bottom row
        for j in range(1, m-1): # begins from 1 as 0 was checked by the above 
            bfs(j,0) 
            bfs(j,n-1)

		# 最后进行置换， 内部 0 换位 1， D --> 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D': board[i][j] = 'O'
                elif board[i][j] == 'O': board[i][j] = 'X'







