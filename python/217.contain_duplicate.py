"""此题要注意从1开始， 从0开始会出问题
"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = dict()
        for i in range(len(nums)):
            index = d.get(nums[i])
            if index >= 0 and abs(i - index) <= k:
                return True
            d[nums[i]] = i 
        return False


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for e in nums:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
        for key in d:
            if d[key] > 1:
                return True
        return False


"""
one solution
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

"""
Another solution
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


"""
one more solution
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = 1
        return False


if __name__ == '__main__':
	a = Solution()
	print a.containsDuplicate([3,3])

# https://www.youtube.com/watch?v=3OamzN90kPg&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=3
# multiple solutions
# sorting, hashset, hashmap
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
