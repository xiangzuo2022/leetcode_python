"""
54 & 59 是一个思路
"""
def generateMatrix(self, n):
        if n == 0: return []
        matrix = [[0 for i in range(n)] for j in range(n)]
        up = 0; down = len(matrix)-1
        left = 0; right = len(matrix[0])-1
        direct = 0; count = 0
        while True:
            if direct == 0: # go left
                for i in range(left, right+1):
                    count += 1; matrix[up][i] = count
                up += 1
            if direct == 1: # go down
                for i in range(up, down+1):
                    count += 1; matrix[i][right] = count
                right -= 1
            if direct == 2:  # got left
                for i in range(right, left-1, -1):
                    count += 1; matrix[down][i] = count
                down -= 1
            if direct == 3: # go up
                for i in range(down, up-1, -1):
                    count += 1; matrix[i][left] = count
                left += 1
            if count == n*n: return matrix
            direct = (direct+1) % 4
            
            
"""
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        left, right, up, down = 0, n-1, 0, n-1
        matrix = [ [0]*n for _ in range(n)]
        num = 1
        while left<=right and up<=down:
            # 填充左到右
            for i in range(left, right+1):
                matrix[up][i] = num
                num += 1
            up += 1
            # 填充上到下
            for i in range(up, down+1):
                matrix[i][right] = num
                num += 1
            right -= 1
            # 填充右到左
            for i in range(right, left-1, -1):
                matrix[down][i] = num
                num += 1
            down -= 1
            # 填充下到上
            for i in range(down, up-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix