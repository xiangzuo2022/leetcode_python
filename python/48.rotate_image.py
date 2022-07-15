"""
# 90度翻转， 行成为列， 列成为行，新的行里面top的变成了bottom
# 解题思路：先将矩阵转置，然后将矩阵的每一行翻转 (列不用)，就可以得到所要求的矩阵了。
# 次解法比较好理解，画个图就很清楚了
"""
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
    	m = len(matrix) 
    	for i in range(m):
    		for j in range(i+1,m):  # 注意这个范围是为了避免重复置换
    			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    	for i in range(m): # 转完以后每一列内的顺序是颠倒的
    		matrix[i].reverse()
    	

"""
# 解题思路2：首先沿着副对角线翻转一次，然后沿着水平中线翻转一次，就可以得到所要求的矩阵了。
# 时间复杂度O(n^2)，空间复杂度O(1)
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        #思路1，时间复杂度O(n^2)，空间复杂度O(1)
        n = len(matrix)
        for i in range(n):
            for j in range(n-i): #沿着副对角线反转
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
        for i in range(n/2):     #沿着水平中线反转
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
        return matrix



