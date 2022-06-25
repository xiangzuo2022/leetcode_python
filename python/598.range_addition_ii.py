"""
原数组初始化均为0，那么如果ops为空，没有任何操作，那么直接返回m*n即可，我们可以用一个优先队列来保存最大数字
矩阵的横纵坐标，我们可以通过举些例子发现，只有最小数字组成的边界中的数字才会被每次更新
"""
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return n*m
        minx = min([x[0] for x in ops])
        miny = min([y[1] for y in ops])
        
        return minx*miny