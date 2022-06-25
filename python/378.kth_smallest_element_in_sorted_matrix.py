"""
用最小heap但不是最优解
这道题让我们求有序矩阵中第K小的元素，这道题的难点在于数组并不是蛇形有序的，意思是当前行的最后一个元素并不一定会小
于下一行的首元素，所以我们并不能直接定位第K小的元素，所以只能另辟蹊径。先来看一种利用堆的方法，我们使用一个最大堆，
然后遍历数组每一个元素，将其加入堆，根据最大堆的性质，大的元素会排到最前面，然后我们看当前堆中的元素个数是否大于k，
大于的话就将首元素去掉，循环结束后我们返回堆中的首元素即为所求:
"""
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        nums = []
        for line in matrix:
            nums.extend(line)
        heapq.heapify(nums)
        res = 0
        for i in range(k):
            res = heapq.heappop(nums)
        return res

"""
改进的基于heap的算法
根据堆的算法，可以实现改进，不用把每个元素都进堆，只需要把“最可能是最小值”的进堆即可。也就是说我们每次进堆的元素只要包括
下一个最小的元素即可。我们把左上角最小的元素和其索引进堆，然后把堆里的元素进行一个遍历，每次把元素的右边的元素进堆。
当是第一列元素的时候，把这个元素下面的元素也进堆。
"""
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        ans = 0
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if j == 0 and i + 1 < m:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans