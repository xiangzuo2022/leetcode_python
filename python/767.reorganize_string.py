"""
use max heap
"""

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2: return s
        counts = collections.Counter(s)
        maxLength = max(counts.items(), key=lambda x:x[1])[1]
        if maxLength > (1 + length) // 2:
            return ""
        
        queue = [(-x[1], x[0]) for x in counts.items()]
        heapq.heapify(queue)
        ans = []
        while len(queue) > 1:
            _, ch1 = heapq.heappop(queue)
            _, ch2 = heapq.heappop(queue)
            ans.append(ch1)
            ans.append(ch2)
            counts[ch1] -= 1
            counts[ch2] -= 1
            if counts[ch1] > 0:
                heapq.heappush(queue, (-counts[ch1], ch1))
            if counts[ch2] > 0:
                heapq.heappush(queue, (-counts[ch2], ch2))
        if queue:
            ans.append(queue[0][1])
        return "".join(ans)
    

# https://www.youtube.com/watch?v=2g_b1aYTHeg
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap) # O(n)

        prev = None
        res = ""

        while maxHeap or prev:
            if not maxHeap and prev: # cannot find valid strings and return ""
                return ""
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0: # need this condition
                prev = [cnt, char]
        return res