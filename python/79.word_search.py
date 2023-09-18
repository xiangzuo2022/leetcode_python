"""
# 使用DFS, 不要再开一个新的棋盘或其他很大的变量来记录状态，不然容易超时。
# 使用dfs来搜索，为了避免已经用到的字母被重复搜索，将已经用到的字母临时替换为'#'就可以了
# 多练习几遍
"""

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        self.totalRow, self.totalCol = len(board),len(board[0])
        for i in xrange(self.totalRow):
            for j in xrange(self.totalCol):
                if board[i][j] == word[0]: # 首先要找到第一个开始的点
                    if self.dfs(board,i,j,word[1:]): return True
        return False

    def dfs(self,board,r,c,word):
        if len(word) == 0 : return True
        # Up
        if (r > 0 and board[r-1][c] == word[0]):
            ch, board[r][c] = board[r][c],'#'  # 临时替换为#
            if self.dfs(board,r-1,c,word[1:]): return True
            board[r][c] = ch

        # Down
        if (r < self.totalRow-1 and board[r+1][c]==word[0]):
            ch,board[r][c] = board[r][c],'#'
            if self.dfs(board,r+1,c,word[1:]): return True
            board[r][c] = ch

        # left
        if (c > 0 and board[r][c-1]==word[0]):
            ch, board[r][c] = board[r][c],'#'
            if self.dfs(board,r,c-1,word[1:]): return True
            board[r][c] = ch

        # right
        if (c < self.totalCol-1 and board[r][c+1] == word[0]):
            ch, board[r][c] = board[r][c],'#'
            if self.dfs(board,r,c+1,word[1:]): return True
            board[r][c] = ch
        return False


"""
official solution
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            
            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        
        return False

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/word-search/solution/dan-ci-sou-suo-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# https://www.youtube.com/watch?v=pfiQ_PS1g8E&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo
# backtracking O(n * m * dfs) call stack of dfs is len(word) and we call it 4 ^len(word)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path:
                return False
            path.add((r, c))
            res =(dfs(r+1, c, i+1) or
                 dfs(r-1, c, i+1) or
                 dfs(r, c+1, i+1) or
                 dfs(r, c-1, i+1) )
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

















    		


