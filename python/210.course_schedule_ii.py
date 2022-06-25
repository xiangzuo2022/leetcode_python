"""
# 此问题等价于寻找有向图的拓扑顺序。如果存在环路，不存在拓扑顺序，也就不可能修完所有的课程。
# 通过DFS实现的拓扑排序
# 以下算法很好,实现了经典的拓扑排序
flag用来控制死循环, e.g., 2, [[0,1],[1,0]]), 没有degree == 0的， 循环就会死下去
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        degrees = [0] * numCourses
        childs = [[] for i in range(numCourses)]
        for pair in prerequisites:
            degrees[pair[0]] += 1  # in-degree
            childs[pair[1]].append(pair[0])
        courses = set(range(numCourses))  # initialize courses with the size of course; courses = set([0,1,2,3])
        flag = True  # flag is used to control finding nodes with zero in-degree. 
        ans = []
        while flag and len(courses):
            flag = False
            removeList = []
            for i in courses:
                if degrees[i] == 0:
                    for child in childs[i]:
                        degrees[child] -= 1
                    removeList.append(i)
                    flag = True
            for j in removeList:
                ans.append(j)
                courses.remove(j)
        return [[], ans][len(courses) == 0]

"""
My own solution extends from 207
"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses; indegree = [0]*n; childs = [[] for i in range(n)] 
        for e in prerequisites:
            indegree[e[0]] += 1
            childs[e[1]].append(e[0])
            
        k = 0; stack = []
        for i in range(n):
            if indegree[i] == 0:
                stack.append(i)
        ans = []
        while stack:
            tmp = stack.pop()
            k += 1
            if tmp not in ans:
                ans.append(tmp)
            for ee in childs[tmp]:
                indegree[ee] -= 1
                if indegree[ee] == 0:
                    stack.append(ee)
                    
        return [[],ans][k==n]
      
      
"""
DFS topological sort
"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int 课程门数
        :type prerequisites: List[List[int]] 课程与课程之间的关系
        :rtype: bool
        """
        # 课程的长度
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return [i for i in range(numCourses)]
        # 入度数组，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表
        adj = [set() for _ in range(numCourses)]
        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # 1 -> 0，这里要注意：不要弄反了
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)

        # print("in_degrees", in_degrees)
        # 首先遍历一遍，把所有入度为 0 的结点加入队列
        res = []
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        while queue:
            top = queue.pop(0)
            res.append(top)

            for successor in adj[top]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    queue.append(successor)
        if len(res) != numCourses:
            return []
        return res

"""
想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
1 -> 0，这里要注意：不要弄反了
"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return [i for i in range(numCourses)]
        # 入度数组，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表
        adj = [set() for _ in range(numCourses)]
        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # 1 -> 0，这里要注意：不要弄反了
        for first, second in prerequisites:
            in_degrees[first] += 1
            adj[second].add(first)

        # print("in_degrees", in_degrees)
        # 首先遍历一遍，把所有入度为 0 的结点加入队列
        res = []
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        while queue:
            top = queue.pop(0)
            res.append(top)

            for successor in adj[top]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    queue.append(successor)
        if len(res) != numCourses:
            return []
        return res
