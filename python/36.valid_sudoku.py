class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        def isValid(x, y, tmp):
            for i in range(9):
                if board[i][y]==tmp:return False
            for i in range(9):
                if board[x][i]==tmp:return False
            for i in range(3):
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j]==tmp: # this will make replicate checks
                    	return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                	continue
                tmp=board[i][j]
                board[i][j]='D'  # why do we need this?
                if isValid(i,j,tmp)==False: 
                	return False
                else:
                    board[i][j]=tmp
        return True





"""
# 验证已经填好的数独是否合符规则。
# 思路：
# 行，列和小九宫分别检查就可以了。
# 有填好数字的就检查，没填写的可以不管。
# 但是也可以一起同时检查，时间效率稍微快一点，不过需要额外空间。
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        line_set = [set([]) for j in range(9)]
        row_set = [set([]) for j in range(9)]
        square_set = [set([]) for j in range(9)]

        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item == '.':
                    continue
                if item in line_set[i] or item in row_set[j] or item in square_set[i/3 * 3 + j/3]:
                    return False
                else:
                    line_set[i].add(item)
                    row_set[j].add(item)
                    square_set[i/3 * 3 + j/3].add(item)
        return True

"""
可以记录所有出现过的行、列、块的数字及相应位置，最后判断是否有重复。用set操作精简代码
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j),(i,c),(i/3,j/3,c)]
        return len(seen) == len(set(seen))





























