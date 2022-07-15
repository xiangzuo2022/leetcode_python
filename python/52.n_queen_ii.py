class Solution:
    # @param {integer} n
    # @return {integer}

    def totalNQueens(self, n):
    	def check(k,j):
    		for i in range(k):
    			if board[i] == j or abs(i-k) == abs(board[i]-j):
    				return False
    		return True

    	def dfs(depth,value):
    		if depth == n:
    			ans.append(value)
    			return
    		for i in range(n):
    			if check(depth,i):
    				board[depth] = i
    				s = '.' * n
    				dfs(depth+1,value+[s[:i]+'Q'+s[i+1:]])
    	ans = []
    	board = [-1 for i in range(n)]
    	dfs(0,[])
    	return len(ans)
