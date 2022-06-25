"""
DFS:
当 xxx 号房间中有 yyy 号房间的钥匙时，我们就可以从 xxx 号房间去往 yyy 号房间。如果我们将这 nnn 个房间看成有向图中的 nnn 个节点，
那么上述关系就可以看作是图中的 xxx 号点到 yyy 号点的一条有向边。
这样一来，问题就变成了给定一张有向图，询问从 000 号节点出发是否能够到达所有的节点。
思路及解法
我们可以使用深度优先搜索的方式遍历整张图，统计可以到达的节点个数，并利用数组 vis\textit{vis}vis 标记当前节点是否访问过，以防止重复访问。
"""
class Solution:
    def canVisitAllRooms(self, rooms):
        def dfs(x: int):
            vis.add(x)
            for it in rooms[x]:
                if it not in vis:
                    dfs(it)
        
        n = len(rooms)
        vis = set()
        dfs(0)
        return len(vis) == n
      
      
"""
BFS
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        num = 0
        vis = {0}
        que = collections.deque([0])

        while que:
            x = que.popleft()
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    vis.add(it)
                    que.append(it)
        
        return num == n
      
      
"""
my own BFS
"""
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        visit = set()
        
        queue = [0]
        while queue:
            x = queue.pop(0)
            visit.add(x)
            for it in rooms[x]:
                if it not in visit:
                    visit.add(it)
                    queue.append(it)
      
        return len(visit) == n

