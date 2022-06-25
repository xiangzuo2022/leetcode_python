"""
# idea, obtain the freq of s, then put in the max heap with [(3,a), (2,b), (2,c), (1,d)]. 
pop one by one from max heap, and reduce each count by 1 and append to cache queue. 
if queue size is less than k, continue. push back to heap if its front cnt > 0. 
add letter to res, when reaches lens, return res otherwise ''. Time O(nlog26), Space O(26).
# corner case, s='a' , k=0
此题用到了很多数据结构：max heap, deque, 但是核心思想还是利用frequency从大到小来做
"""
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """      
        
        if k == 0:
            return s
        count = collections.Counter(s)
        heap = []
        for key in count:
            heapq.heappush(heap, (-count[key], key)) 
        res = [] # notes, res='', res+=letter will create new string.
        queue = collections.deque()
        while heap: 
            cnt, letter = heapq.heappop(heap)
            res.append(letter)
            cnt += 1  # decrease cnt because cnt < 0
            queue.append((cnt, letter))
            if len(queue) < k:
                continue
            front = queue.popleft()
            if front[0] < 0: # cnt > 0
                heapq.heappush(heap, front)
        return ''.join(res) if len(res) == len(s) else ''