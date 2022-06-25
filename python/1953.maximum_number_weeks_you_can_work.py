"""
math problem
"""
class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        longest = max(milestones)
        rest = sum(milestones) - longest
        if longest < rest + 1:
            return longest + rest
        else:
            return 2*rest + 1
        