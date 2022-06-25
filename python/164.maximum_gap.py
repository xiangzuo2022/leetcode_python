class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, num):
    	N = len(num)
    	if N < 2:
    		return 0
    	A = min(num)
    	B = max(num)
    	bucketRange = max(1,int((B-A-1)/(N-1))+1)  #??
    	bucketLen = (B-A)/bucketRange + 1  # ??
    	buckets = [None]*bucketLen  #??
    	for k in num:
    		loc = (k-A)/bucketRange
    		bucket = buckets[loc]
    		if bucket is None:
    			bucket = {'min':k,'max':k}
    			buckets[loc] = bucket
    		else:
    			bucket['min'] = min(bucket['min'],k)
    			bucket['max'] = max(bucket['max'],k)
    	maxGap = 0
    	for x in range(bucketLen):
    		if buckets[x] is None:
    			continue
    		y = x + 1 #??
    	while  y < bucketLen and buckets[y] is None:
    		y += 1
    	if y < bucketLen:
                maxGap = max(maxGap, buckets[y]['min'] - buckets[x]['max'])
            x = y
        return maxGap 



   # http://bookshadow.com/weblog/2014/12/14/leetcode-maximum-gap/

"""
假设有N个元素A到B。那么最大差值不会小于ceiling[(B - A) / (N - 1)]. 令bucket（桶）的大小len = ceiling[(B - A) / (N - 1)]，则最多会有(B - A) / len + 1个桶.
对于数组中的任意整数K，很容易通过算式loc = (K - A) / len找出其桶的位置，然后维护每一个桶的最大值和最小值. 由于同一个桶内的元素之间的差值至多为len - 1，因此最终答案不会从同一个桶中选择。
对于每一个非空的桶p，找出下一个非空的桶q，则q.min - p.max可能就是备选答案。返回所有这些可能值中的最大值。
"""
# passed solution, O(n)
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, num):
        N = len(num)
        if N < 2:
            return 0
        A = min(num)
        B = max(num)
        bucketRange = max(1, int((B - A - 1) / (N - 1)) + 1) #ceil( (B - A) / (N - 1) )
        bucketLen = (B - A) / bucketRange + 1
        buckets = [None] * bucketLen
        maxGap = 0; prev = 0
        for K in num:
            loc = (K - A) / bucketRange
            bucket = buckets[loc]
            if bucket is None:
                bucket = {'min' : K, 'max' : K}
                buckets[loc] = bucket
            else:
                bucket['min'] = min(bucket['min'], K)
                bucket['max'] = max(bucket['max'], K)
        # calcuate gap
        for i in range(1,length):
            if buckets[i] == None:
                continue            
            maxGap = max(maxGap,buckets[i]['min'] - buckets[prev]['max'])
            prev = i
        return maxGap

# O(nlogn) sorting
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        num = sorted(num)
        maxGap = 0
        for x in range(len(num) - 1):
            maxGap = max(maxGap, num[x + 1] - num[x])
        return maxGap











