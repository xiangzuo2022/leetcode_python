class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
  
    def combinationSum3(self, k, n):
        ans = []
        def search(start, cnt, sums, nums):
            if cnt > k or sums > n:
                return
            if cnt == k and sums == n:
                ans.append(nums)
                return
            for x in range(start + 1, 10):
                search(x, cnt + 1, sums + x, nums + [x])
        search(0, 0, 0, [])
        return ans



        
"""
my own solution
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(target, count, start, value):         
            if target == 0 and count == k:
                ans.append(value)
                return 
            for i in range(start+1, 10):
                if count > k or target < 0:
                    return
                dfs(target-i, count+1, i, value+[i])
                       
            
        ans = []
        self.count = 0
        dfs(n, 0, 0, [])
        return ans



"""
O(n2)不是最优解
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        ind = sorted(range(len(nums)),key=lambda x: nums[x]) # 得到index

        # 根据nums中值的大小排序后记录index  
        print 'ind: ',ind   
        for i in range(len(nums)-1):
            j = i + 1
            # print 'i,j,ind[i],ind[j]:',i,j,ind[i],ind[j]
            while j < len(nums) and nums[ind[j]] - nums[ind[i]] <= t:
                if abs(ind[i] - ind[j]) <= k:
                    return True
                j += 1
        return False



"""
bucket sort的解法 O(n)
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        buckets = {}
        for i, v in enumerate(nums):
        # t == 0 is a special case where we only have to check the bucket
        # that v is in.
            bucketNum, offset = (v / t, 1) if t else (v, 0)
            for idx in xrange(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True

            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
            # Remove the bucket which is too far away. Beware of zero t.
                del buckets[nums[i - k] / t if t else nums[i - k]]

        return False


"""
O(n)
http://algobox.org/2015/12/29/contains-duplicate-iii/ (详细解答)
bucket sort 的另一种写法，比较容易懂
To determine whether there is a nearby almost duplicate in one pass we need to keep a 
sliding window with length k and a dynamic set can do this. Problem is we need to check 
almost duplicate each time we add a item into the window/set. If we use BST as our dynamic set, 
the cost of find almost duplicate is O(log n) therefore the whole solution is O(n log n). 
Now can we check it in O(1) time on average? The answer is yes. Hash table can do insert,
find and remove in O(1) time on average and by carefully design the hash table we can 
check almost duplicate in O(1) too.
The idea is like the bucket sort algorithm. Suppose we have consecutive buckets covering the 
range of nums with each bucket a width of t+1. If there are two item with difference <= t, 
one of the two will happen:

(1) the two in the same bucket
(2) the two in neighbor buckets
Note that we do not need to actually allocate a lot of buckets. At any time there will 
only be at most min(k, n) buckets. All we need to do is calculate the label of the 
bucket m = value/(t+1), and check the buckets m - 1, m, m + 1. The whole algorithm is then O(n).
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        n = len(nums)
        d = {}
        t += 1 # 考虑t=0 or t>0
        for i in xrange(n):
            if i > k:
                del d[nums[i - k - 1] / t] #不用考虑多余的，减少search时间
            m = nums[i] / t
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < t:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < t:
                return True
            d[m] = nums[i]
        return False
      
"""
backtrack + trim solution
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        def backtrack(k, n, startIndex):
            if len(path) > k or sum(path) > n:
                return
            if len(path) == k and sum(path) == n:                
                ans.append(path[:])                
                return 
            for i in range(startIndex, 10):               
                path.append(i)
                backtrack(k, n, i+1)
                path.pop()
        backtrack(k, n, 1)
        return ans


if __name__ == '__main__':
    a = Solution()
    print a.combinationSum3(3,7)
            



















            