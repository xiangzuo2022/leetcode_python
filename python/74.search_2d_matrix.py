class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    # from bottom to up
    """
    突然发现LeetCode很喜欢从LintCode上盗题，这是逼我去刷LintCode的节奏么?! 这道题让我们在一个二维数组中快速的搜索
    的一个数字，这个二维数组各行各列都是按递增顺序排列的，是之前那道Search a 2D Matrix 搜索一个二维矩阵的延伸，
    那道题的不同在于每行的第一个数字比上一行的最后一个数字大，是一个整体蛇形递增的数组。所以那道题可以将二维数组展开
    成一个一位数组用一次二查搜索。而这道题没法那么做，这道题有它自己的特点。如果我们观察题目中给的那个例子，我们可以
    发现有两个位置的数字很有特点，左下角和右上角的数。左下角的18，往上所有的数变小，往右所有数增加，那么我们就可以
    和目标数相比较，如果目标数大，就往右搜，如果目标数小，就往上搜。这样就可以判断目标数是否存在。当然我们也可以把
    起始数放在右上角，往左和下搜，停止条件设置正确就行.

    题解：
    在行和列排序好的二维数组中查找目标数字。这里我们用了一个很巧妙的方法，从矩阵的右上角开始找，相当于把这个元素当作mid，
    目标比mid大，则row + 1，小则col + 1，相等则返回mid。也是类似二分查找的思想。
    Time Complexity - O(m + n)， Space Complexity - O(1)
    """
    def searchMatrix(self, matrix, target):
        j = len(matrix[0]) -1;i=0
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False



"""
九章模板
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
            
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1
        while start + 1 < end:
            mid = (start + end) / 2
            x, y = mid / m, mid % m
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid
        x, y = start / m, start % m
        if matrix[x][y] == target:
            return True
        
        x, y = end / m, end % m
        if matrix[x][y] == target:
            return True
        
        return False
        
        
            
            
            
            
            
        
























