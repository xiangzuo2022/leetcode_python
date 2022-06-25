"""
BFS
"""
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.depthPartialSum(nestedList, 0)
        
    def depthPartialSum(self, List, depth):
        sum = 0
        for i in List:
            if i.isInteger():
                sum += i.getInteger() * (depth + 1)
            else:
                sum += self.depthPartialSum(i.getList(), depth + 1)
        return sum