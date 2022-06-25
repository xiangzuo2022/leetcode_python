"""
O(nk) is not the best solution
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
    	if k > len(nums) or nums == []: return []
    	res = []
    	for i in range(len(nums)+1-k):
    		window = nums[i:i+k]
    		res.append(max(window))
    	return res

if __name__ == '__main__':
	a = Solution()
	print a.maxSlidingWindow([1],1)


# 我自己做的很直白的思想， 最好看下别人的solution

"""
 jiuzhong solution， discussion codes
 O(n);双端队列
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []; deque = []
        for index, value in enumerate(nums):
            if deque and deque[0] + k <= index: # out of window so need to remove the first element in the deque
                deque.pop(0)
            while deque and nums[deque[-1]] < value:
                deque.pop()
            deque.append(index)
            if index+1 >= k: # when arrives the k element in the window, maxvalue needs to be stored in ans
                ans.append(nums[deque[0]]) # deque[0] stores the max value in the window
        return ans

"""
priority queue
"""
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 建立最大堆，因为默认为最小堆，加个负号就是最大堆
        q = [(-nums[i], i) for i in range(k)]  
        heapq.heapify(q)
        res = [-q[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            #最大值可能并不在滑动窗口中，将其永久删除，确保最大值在窗口中
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res

作者：jensen-huang
链接：https://leetcode-cn.com/problems/sliding-window-maximum/solution/you-xian-dui-lie-dan-diao-dui-lie-xun-zh-7vou/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
单调队列
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans