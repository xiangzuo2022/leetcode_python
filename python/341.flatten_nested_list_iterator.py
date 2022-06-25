class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::]
        
    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[0]
            if top.isInteger():
                return True
            self.stack = top.getList() + self.stack[1:] # remember to add the previous stack
        return False

"""
DFS solution
"""
class NestedIterator(object):
    def dfs(self, nests):
        for nest in nests:
            if nest.isInteger():
                self.queue.append(nest.getInteger())
            else:
                self.dfs(nest.getList())
                    
    def __init__(self, nestedList):
        self.queue = collections.deque()
        self.dfs(nestedList)

    def next(self):
        return self.queue.popleft()

    def hasNext(self):
        return len(self.queue)

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/flatten-nested-list-iterator/solution/fu-xue-ming-zhu-xiang-jie-ti-yi-shu-li-d-n4qa/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
use stack
"""
class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])
        

    def next(self):
        cur = self.stack.pop()
        return cur.getInteger()

    def hasNext(self):
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            self.stack.pop()
            for i in range(len(cur.getList()) - 1, -1, -1):
                self.stack.append(cur.getList()[i])
        return False

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/flatten-nested-list-iterator/solution/fu-xue-ming-zhu-xiang-jie-ti-yi-shu-li-d-n4qa/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
My solution with queue operation from the beginning
"""

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        n = len(nestedList)
        self.stack = []
        for i in range(n):
            self.stack.append(nestedList[i])

    def next(self):
        """
        :rtype: int
        """
        cur = self.stack.pop(0)
        return cur.getInteger()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            cur = self.stack[0]
            if cur.isInteger():
                return True
            self.stack.pop(0)
            for i in range(len(cur.getList())):
                self.stack.insert(i, cur.getList()[i])
        return False
        