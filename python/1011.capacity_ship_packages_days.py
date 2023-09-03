class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def is_possible(capacity):
            count = 1
            current_weight = 0
            for w in weights:
                if current_weight + w > capacity:
                    count += 1
                    current_weight = 0
                current_weight += w
            return count <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right -left)//2
            if is_possible(mid):
                right = mid
            else:
                left = mid + 1
        return left
 # simiar to 1231 and 410