"""
For each move, we -1 for each player 1's move and +1 for player 2's move.
similr to 1275
"""

class TicTacToe(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.rows, self.cols = [0] * n, [0] * n
        self.diag = self.anti_diag = 0
        self.n = n
        

    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        offset = player * 2 - 3
        self.rows[row] += offset
        self.cols[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.anti_diag += offset
        if any(line == self.n for line in (self.rows[row], self.cols[col], self.diag, self.anti_diag)):
            return 2
        if any(line == -self.n for line in (self.rows[row], self.cols[col], self.diag, self.anti_diag)):
            return 1
        else:
            return 0
        