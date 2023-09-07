"""
use miniheap and dictionary
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        freq_list=[]  
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
                
        for key in freq.keys():
           
            freq_list.append((-freq[key], key))
        heapq.heapify(freq_list)
        topk = []
        for i in range(0,k):
            topk.append(heapq.heappop(freq_list)[1])
        return topk
      
      
"""
小顶堆
"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #要统计元素出现频率
        map_ = {} #nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        
        #对频率排序
        #定义一个小顶堆，大小为k
        pri_que = [] #小顶堆
        
        #用固定大小为k的小顶堆，扫面所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k: #如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)
        
        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒叙来输出到数组
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result


# https://www.youtube.com/watch?v=YPTqKIgVk-k
# Bucket sort O(n)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range (len(nums)+ 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
# maxHeap C(k*log(n))
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        maxHeap = []
        for n, c in count.items():
            maxHeap.append((-c, n))
        heapq.heapify(maxHeap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res
         