"""
unin/find经典题
https://www.youtube.com/watch?v=VJnUwsE4fWA&t=688s
"""
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nodesCount = len(edges)        
        parent = [i for i in range(nodesCount+1)]

        def find(index) : # find and compress parents paths
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1, index2):
            parent[find(index1)] = find(index2)

        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                return [node1, node2]
        
        return []