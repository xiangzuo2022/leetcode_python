# 两个指针 start, end.  如果nums[end+1] = nums[end]+1, 就移动end指针, 否则, 
# 插入字符串nums[start]->nums[end]. 

n = len(nums); ans = []
        begin = 0; end = 0
        if n == 1: return [str(nums[0])]; tmp = ''
        while end <= n-1:
            while end < n-1 and nums[end]+1 == nums[end+1]:
                end += 1
            if begin == end:
                tmp = str(nums[begin])
            else:
                tmp = str(nums[begin]) + '->' + str(nums[end])
            ans.append(tmp)
            begin = end + 1
            end = begin
        return ans






# *********** My Own Solution ************
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        n = len(nums)
        
        if not nums: return ans
        if n == 1: return [str(nums[0])]
        start = end = 0;interval = ''
        while end <= n-1:
            if end+1 < n and (nums[end+1]) == nums[end] + 1:
                end += 1
                continue
                   
            else:
                if start != end:
                    interval = str(nums[start])+'->' +str(nums[end])
                else:
                    interval = str(nums[end])             
                
                ans.append(interval)
            end += 1
            start = end
            
        return ans























