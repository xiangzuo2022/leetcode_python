#https://www.youtube.com/watch?v=EaphyqKU4PQ
# Dijkstra algorithm shortest path graph algorithm
# BFS E * log V^2 = O(E*logV)
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        minHeap = [(0, k)]
        # build a graph adjacent list
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        visit = set()
        res = 0
        # BFS to visit each node and its neighbors
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            res = max(res, w1)
            # neighbors
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2+w1, n2))
        return res if len(visit) == n else -1



