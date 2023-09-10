# https://www.youtube.com/watch?v=Kkmv2h48ekw
# hashmap: O(n)
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        countGap = {0:0} # mapping pos: count of brick gaps
        for r in wall:
            total = 0
            for b in r[:-1]: # not inincluding the last one
                total += b
                countGap[total] = 1 + countGap.get(total, 0)
        return len(wall) - max(countGap.values())