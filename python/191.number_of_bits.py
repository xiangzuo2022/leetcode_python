# https://www.youtube.com/watch?v=5Km3utixwZs
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n :
            res += n % 2
            n = n >> 1
        return res
    
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n :
            n= n &(n-1)
            res += 1           
        return res
    
