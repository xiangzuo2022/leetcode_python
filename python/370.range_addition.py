
"""
在这题中没必要每次把区间的每一个值都更新, 只需要更新起点和终点后的一点即可. 也就是说把增加的值放在起点, 
终点后的一点减去增加的值, 这样再扫描的时候把之前累加的和作为最终值即可. 
数学题
"""
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for update in updates:
            start, end, inc = update
            res[start] += inc
            
            if end + 1 <= length - 1:
                res[end+1] -= inc

        sum = 0
        for i in range(length):
            sum += res[i]
            res[i] = sum
        return res