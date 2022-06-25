"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
"""

#*********** Solution One: not good to use the built-in function bin()*************

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1  # Convert an integer number to a binary string.


#*********** Solution Two: time limit exceeded *************

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        counter = 0
        for i in range(32):
            counter += (z>>i) & 1
        return counter
