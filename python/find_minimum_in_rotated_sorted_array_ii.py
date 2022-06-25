# binary search

class Solution:
    # @param {integer[]} nums
    # @return {integer}

    def findMin(self, num):
	    ans = num[0]
	    size = len(num)
	    low, high = 0, size - 1
	    while low <= high:
	      mid = (low + high) / 2
	      ans = min(ans, num[mid])
	      if num[mid] < num[high]: #min位于上升沿左侧
	        high = mid - 1
	      elif num[mid] > num[high]: #min位于左侧上升沿与右侧上升沿之间
	        low = mid + 1
	      else: #num[mid] == num[high]
	        if low < mid:
	          ans = min(ans, self.findMin( num[low : mid + 1] ))
	        if mid + 1 < high:
	          ans = min(ans, self.findMin( num[mid + 1 : high + 1] ))
	        break
	    return ans

