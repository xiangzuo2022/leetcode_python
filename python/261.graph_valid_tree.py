# https://www.youtube.com/watch?v=bXsUuownnoQ
# DFS + visit + prev
# two conditions to detect no loop in a graph: n == len(visit) and DFS return True
# no loop and all nodes are connected
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True
        adj = {i:[] for i in range(n)}
        visit = set()
        # build adjcent list
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j == prev: # if no prev, it is easy to incorrectly detect a graph with loop. because j's neighbors include the prev
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)