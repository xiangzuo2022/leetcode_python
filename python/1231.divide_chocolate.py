# good explain

class Solution(object):
    def maximizeSweetness(self, sweetness, k):
        """
        :type sweetness: List[int]
        :type k: int
        :rtype: int
        """
        def countPieces(minSweetness):
            total = 0
            pieces = 0
            
            for s in sweetness:
                total += s
                if total >= minSweetness:
                    pieces += 1
                    total = 0
            
            return pieces
    
        left = min(sweetness)
        right = sum(sweetness) /(k+1)
        
        while left < right:
            mid = (left + right + 1) // 2
            if countPieces(mid) >=  k + 1:
                left = mid
            else:
                right = mid - 1
        
        return left