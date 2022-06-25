"""
# Solution: 分别记录两个向量x, y，保存行和列是否有0，再次遍历数组时查询对应的行和列然后修改值。
# 给一个矩阵，若某格为0，该格所在行及所在列全部改为0，要求常数空间复杂度。
# 显然先扫一遍Mark的话空间复杂度是O(M+N)，这个Mark是必不可少的，不能用额外空间的话，就只能用原数组的
# 某一行及某一列来记录了。最后再扫一遍数组，根据标记行及标记列的值来判断某格是否要置0。需要注意的是，
# 该行及该列其它的格子要最后再置0。
以下做法用了额外的空间不是最优解
"""
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
    	m = len(matrix)
    	n = len(matrix[0])
    	row = [False for i in range(m)]
    	col = [False for i in range(n)]
    	for i in range(m):
    		for j in range(n):
    			if matrix[i][j] == 0:
    				row[i] = True
    				col[j] = True
    	for i in range(m):
    		for j in range(n):
    			if row[i]==True or col[j]==True:
    				matrix[i][j] = 0


"""
水中的鱼：解题点就在于清空标志位存在哪里的问题。可以创建O(m+n)的数组来存储，但此题是希望复用已有资源。
这里可以选择第一行和第一列来存储标志位。
以下写法比较容易懂
"""

class Solution:
# @param {integer[][]} matrix
# @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        m,n = len(matrix),len(matrix[0])
        row_zero, col_zero = False,False
        # Does first row have zero?
        for i in range(m):
            if matrix[i][0] == 0:
                row_zero = True

        # Does first column have zero?
        for j in range(n):
            if matrix[0][j] == 0:
                col_zero = True

        # find zeroes and store the info in first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # set zeroes except the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # set zeroes for first row and column if needed
        if col_zero:
            for j in range(n):
                matrix[0][j] = 0
        if row_zero:
            for i in range(m):
                matrix[i][0] = 0






