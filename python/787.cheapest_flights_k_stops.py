# https://www.youtube.com/watch?v=5eIK3zUdYmE
# Bellman-Ford algorithm find shortest path. It is more efficient than Dikastrj
# O(E * K)
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = copy.deepcopy(prices)
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]