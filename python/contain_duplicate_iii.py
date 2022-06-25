"""
# 一个简单的解法， 从discussion中找到的
# 此题有用bucket实现的， 可以想想
Index 被改变了， 为啥还可以？？？？
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
    	ind = sorted(range(len(nums)),key=lambda x: nums[x]) # 得到index
        # input [7,5,34,6] ind: [1,3,0,2]
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


# ****** My own accepted soluiton ********
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                if abs(i-d[nums[i]]) <= k:
                    return True
                else:  # 这句很重要， 否则[1,0,1,1] and k =1 这种case 过不去
                    d[nums[i]] = i
        return False


 
# ********** The third solution *********
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()
        for i in range(len(nums)):
            index = d.get(nums[i])
            if index >= 0 and abs(i - index) <= k:
                return True
            d[nums[i]] = i 
        return False



if __name__ == '__main__':
 	a = Solution()
 	a.containsNearbyAlmostDuplicate([4,2,1],2,1)

