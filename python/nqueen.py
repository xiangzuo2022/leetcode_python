class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        def check(k, j):  # check if the kth queen can be put in column j!
            for i in range(k): #前面已有k-1个queens
                if board[i] == j or abs(k - i) == abs(board[i] - j):  #对角线都是(2,2),(3,3)...
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
        return len(res)


# ********* The Second Time ********
# 规则是两个queen不能再同一个行，列或者diagnal 
# 使用递归来求解, 从网上看到一种很好的棋盘表示方法, N = 4时, 棋盘为[1, 3, 0, 2], 即第1行的queen放在
# 第2列, 第2行的queen放在第4列。Queen逐行放入棋盘, 每放入一个新的queen, 只需要检查她跟之前的queen是
# 否列冲突和对角线冲突就可以了。如果两个queen的坐标为(i1, j1)和(i2, j2), 
# 当abs(i1 - i2) = abs(j1 - j2)时就对角线冲突。
# 枚举想到dfs

class Solution:
    # @param {integer} n
    # @return {string[][]}
    def check(self,k,j): # check whether the kth queen can be placed at the jthe coloum
        
        
        for i in range(k): #前面已有k-1个queens
            if board[i] == j or abs(k - i) == abs(board[i] - j):  #对角线都是(2,2),(3,3)...
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
    return len(res)


# tips: 当有很多变量要使用时， 最好在函数里面直接定义函数， 否则要定义全局变量，很麻烦





























