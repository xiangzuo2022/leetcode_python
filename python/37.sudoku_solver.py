# 数独的目标是以数字填充一个9×9网格，而使每行，每列和每个宫（即3×3的大格）包含所有1至9的数字。
# 解题思路：使用dfs来解决问题。
# similar to valid sudoku
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def check(self,x,y,board): # check的同时也赋值
    	tmp = board[x][y]
    	board[x][y] == '.'
    	for row in range(9):
    		if board[row][y] == tmp:
    			return False
    	for col in range(9):
    		if board[x][col] == tmp:
    			return False
    	for row in range(3):
    		for col in range(3):
    			if board[(x/3)*3+row][(y/3)*3+col] == tmp:
    				return False
    	board[x][y] = tmp
    	return True

    def dfs(self,board):
    	for row in range(9):
    		for col in range(9):
    			if board[row][col] == '.':
    				for char in '123456789':
    					board[row][col] = char
    					if self.check(row,col,board) and self.dfs(board): #当check is true, 加入新char后board变了，所以要递归dfs(board), 
    						return True
    					else:
    						board[row][col] = '.'
    				return False
    	return True



    def solveSudoku(self, board):
    	self.dfs(board)



"""
backtracking template 
"""
def backtrack(board):
            for i in range(len(board)):  #遍历行
                for j in range(len(board[0])):  #遍历列
                    if board[i][j] != ".": continue
                    for k in range(1,10):  #(i, j) 这个位置放k是否合适
                        if isValid(i,j,k,board):
                            board[i][j] = str(k)  #放置k
                            if backtrack(board): return True  #如果找到合适一组立刻返回
                            board[i][j] = "."  #回溯，撤销k
                    return False  #9个数都试完了，都不行，那么就返回false
            return True  #遍历完没有返回false，说明找到了合适棋盘位置了
        def isValid(row,col,val,board):
            for i in range(9):  #判断行里是否重复
                if board[row][i] == str(val):
                    return False
            for j in range(9):  #判断列里是否重复
                if board[j][col] == str(val):
                    return False
            startRow = (row // 3) * 3
            startcol = (col // 3) * 3
            for i in range(startRow,startRow + 3):  #判断9方格里是否重复
                for j in range(startcol,startcol + 3):
                    if board[i][j] == str(val):
                        return False
            return True
        backtrack(board)


