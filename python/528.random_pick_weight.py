class Solution:

    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i
              
"""
Solution 2 
"""
    def __init__(self, w):
        """
        :type w: List[int]
        """
        n = len(w)
        self.prefix_sum = [0] * n
        self.prefix_sum[0] = w[0]

        # åįžå
        for i in range(1, n):
            self.prefix_sum[i] = self.prefix_sum[i-1] + w[i]
        print(self.prefix_sum)


        

    def pickIndex(self):
        """
        :rtype: int
        """
        #seed = random.randint(1, self.prefix_sum[-1])
        seed = self.prefix_sum[-1] * random.random()
        #print(target, seed)
        #index = bisect_left(self.prefix_sum, seed)
        for index, prefix_sum in enumerate(self.prefix_sum):
            if seed <= prefix_sum:
                return index
