"""
Approach 1: non-efficient array
"""
class SparseVector:
    def __init__(self, nums):
        self.array = nums

    def dotProduct(self, vec):
        result = 0
        for num1, num2 in zip(self.array, vec.array):
            result += num1 * num2
        return result

"""
Approach 2: only calcualte non-zero elements to save some calculation
"""
class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nonzeros = {}
        for index, val in enumerate(nums):
            if val != 0:
                self.nonzeros[index] = val
            
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        result = 0
        for i, v in self.nonzeros.items():
            if i in vec.nonzeros:
                result += v * vec.nonzeros[i]
        return result