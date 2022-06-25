class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        def check(k, j):  # check if the kth queen can be put in column j!
            for i in range(k):
                if board[i] == j or abs(k - i) == abs(board[i] - j):
                    return False
            return True

        def dfs(depth, valuelist):
            if depth == n:
                res.append(valuelist)
                return
            for i in range(n):
                if check(depth, i):
                    board[depth] = i
                    s = '.' * n
                    dfs(depth + 1, valuelist + [s[:i] + 'Q' + s[i + 1:]])
        board = [-1 for i in range(n)]
        res = []
        dfs(0, [])
        return res
      
      
"""
apply backtracking template
"""
      class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n: return []
        board = [['.']*n for i in range(n)]
        ans = []
        def isValid(board, row, col):
            # conflict at the same column
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False
            # left up corner
            i = row -1;
            j = col -1;
            while i >=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j-= 1
            # right up corner
            i = row-1
            j = col +1 
            while i >=0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True
        
        def backtracking(board, row, n):
            if row == n:
                path = []
                for temp in board:
                    path.append("".join(temp))
                ans.append(path)
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtracking(board, row+1, n)
                board[row][col] = '.'
                
        backtracking(board, 0, n)
        return ans













































