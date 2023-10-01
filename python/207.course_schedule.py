 """
# 此问题等价于判断有向图中是否有环。如果存在环路，无法完成拓扑排序，也就不可能修完所有的课程。
# 表示图的方法有几种。例如，输入中的先修课程就是用一组边的方式表示图。这种图的表示方法合适吗？
# 通过DFS实现的拓扑排序—Cousera的一段21分钟的视频教程很好的解释了拓扑排序的基本概念。拓扑排序也可以通过BFS完成。
# 解题思路：拓扑排序，如果可以完成拓扑排序，返回True，否则返回False
# O (V + E)
# DAG is a directed graph without a cycle, topological sort is only for DAG
"""

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def dfs(self,v,visit,gr):    	
    	visit[v] = -1  # mark temperately,denoting v is being searching currently.
    	for i in gr[v]:  # i is gr[v]'s prerequisites
    		if visit[i] == -1 or not self.dfs(i,visit,gr): # if the searching v appears here, then there is a circle.
    			return False
    	visit[v] = 1
    	return True

    def canFinish(self,numCourses,prerequisites):
    	gr = [[] for x in range(numCourses)]
    	visit = [0 for x in range(numCourses)]

    	for p in prerequisites:
    		if p[0] not in gr[p[1]]:
    			gr[p[1]].append(p[0])

    	for v in range(numCourses):
    		if visit[v] != 1: # not visited
    			if not self.dfs(v,visit,gr):
    				return False
    	return True


"""
Solution 2:
1.检测出所有无依赖的课程；
2.删除这些无依赖的课程，以及所有设计这些课程的依赖关系；
3.如果所有依赖关系均被删除， So it is possible；如果这次循环没有删除一门课程，So it is impossible；
如果是其他情况，继续执行1。
"""
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        if numCourses < 2 or len(prerequisites) < 2:
            return True
        while True:
            count = 0
            mark = [True]*numCourses
            for pre in prerequisites:
                mark[pre[0]] = False  #非独立的课
            for pre in prerequisites:
                if mark[pre[1]]:  # 独立的课
                    count += 1
                    prerequisites.remove(pre)
            if prerequisites == []:
                return True
            elif count == 0:
                return False

"""
删除法:思路简单
"""
from collections import deque
class Solution(object):
    def canFinish(self, n, pres):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        indegree = [[] for i in xrange(n)]  # indegree
        oudegree = [0] * n  # outdegree
        for p in pres:
            oudegree[p[0]] += 1
            indegree[p[1]].append(p[0])
        dq = deque()
        for i in xrange(n):
            if oudegree[i] == 0:
                dq.append(i)
        k = 0
        while dq:
            x = dq.popleft()
            k += 1
            for i in indegree[x]:
                oudegree[i] -= 1
                if oudegree[i] == 0:
                    dq.append(i) 
        
        return k == n # 不能用len(dq)==0来判断， 因为dp必然删空但不代表说有n都压入dp了

# 不要一味的套用书上算法里的indegree outdegree， 具体根据题意来定义

"""
自己的写法 O(m+n)
"""
def canFinish(self, numCourses, prerequisites):
        n = numCourses; indegree = [0]*n; childs = [[] for i in range(n)] # 这种数据结构比字典方便操作
        if not prerequisites: return True
        
        # 类似于在建graph
        for e in prerequisites:
            indegree[e[0]] += 1
            childs[e[1]].append(e[0])
            
        k = 0; stack = []
        for i in range(n):
            if indegree[i] == 0:
                stack.append(i)

        while stack:
            tmp = stack.pop()
            k += 1
            for ee in childs[tmp]:
                indegree[ee] -= 1
                if indegree[ee] == 0:
                    stack.append(ee)
        return [False,True][len(courses)==k] # =k return False

# https://www.youtube.com/watch?v=EgI5nU9etnU
# DFS + adjacent list
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        # build up a graph
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # visitSet = all courses along the curr DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        # the graph could be not fully connected
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


















