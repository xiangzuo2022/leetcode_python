"""
这道题是有名的康威生命游戏, 而我又是第一次听说这个东东，这是一种细胞自动机，每一个位置有两种状态，1为活细胞，0为死细胞，对于每个位置都满足如下的条件：
1. 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡;
2. 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活;
3. 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡;
4. 如果死细胞周围正好有三个活细胞，则该位置死细胞复活.
由于题目中要求我们用置换方法in-place来解题，所以我们就不能新建一个相同大小的数组，那么我们只能更新原有数组，但是题目中要求所有的位置必须被同时更新，
但是在循环程序中我们还是一个位置一个位置更新的，那么当一个位置更新了，这个位置成为其他位置的neighbor时，我们怎么知道其未更新的状态呢，我们可以使用状态机转换：
状态0： 死细胞转为死细胞  0 --> 0
状态1： 活细胞转为活细胞  1 --> 1
状态2： 活细胞转为死细胞  1 --> 0
状态3： 死细胞转为活细胞  0 --> 1
最后我们对所有状态对2取余，那么状态0和2就变成死细胞，状态1和3就是活细胞，达成目的。我们先对原数组进行逐个扫描，对于每一个位置，扫描其周围八个位置，
如果遇到状态1或2，就计数器累加1，扫完8个邻居，如果少于两个活细胞或者大于三个活细胞，而且当前位置是活细胞的话，标记状态2，如果正好有三个活细胞且当前是死细胞的话，
标记状态3。完成一遍扫描后再对数据扫描一遍，对2取余变成我们想要的结果。参见代码如下：
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                cnt = self.countLiveNeighbors(i, j, m, n, board)
                if board[i][j]:
                    if not (cnt == 2 or cnt == 3):
                        board[i][j] = 2
                else:  # temp[i][j] ==0
                    if cnt == 3:
                        board[i][j] = 3

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] = board[i][j] & 1

    def countLiveNeighbors(self, i, j, m, n, board):
        dx = [1, 1, 1, 0, 0, -1, -1, -1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]
        cnt = 0
        for k in xrange(8):
            nx, ny = i + dx[k], j + dy[k]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if board[nx][ny] == 1 or board[nx][ny] == 2:
                cnt += 1

        return cnt
      
"""
official solution:解释非常好
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # 遍历面板每一个格子里的细胞
        for row in range(rows):
            for col in range(cols):

                # 对于每一个细胞统计其八个相邻位置里的活细胞数量
                live_neighbors = 0
                for neighbor in neighbors:

                    # 相邻位置的坐标
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # 查看相邻的细胞是否是活细胞
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                # 规则 1 或规则 3 
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1 代表这个细胞过去是活的现在死了
                    board[row][col] = -1
                # 规则 4
                if board[row][col] == 0 and live_neighbors == 3:
                    # 2 代表这个细胞过去是死的现在活了
                    board[row][col] = 2

        # 遍历 board 得到一次更新后的状态
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/game-of-life/solution/sheng-ming-you-xi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。