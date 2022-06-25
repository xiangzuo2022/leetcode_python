"""
 running time O(n)
"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for letter in letters:
            if ord(letter) > ord(target):
                return letter
        return letters[0]

"""
binary search, running time O(logn)
"""


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters[0] > target:
            return letters[0]
        if letters[len(letters)-1] <= target:
            return letters[0]
        left, right = 0, len(letters)-1
        while left <= right:
            mid = left + (right - left)/2
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return letters[left]
