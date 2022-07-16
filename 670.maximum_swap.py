"""
a smart solution;
"""
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """    
        num = [int(x) for x in str(num)] # convert an integer to an array
        max_idx = len(num) - 1
        xi = yi = 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] > num[max_idx]:
                max_idx = i
            elif num[i] < num[max_idx]: # store it as the candidate
                xi = i
                yi = max_idx
        num[xi], num[yi] = num[yi], num[xi]
        return int(''.join([str(x) for x in num]))