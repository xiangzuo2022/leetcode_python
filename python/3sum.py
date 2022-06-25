"""
此题用递归会超时
# 解题思路：
# 1. 先将数组排序。
# 2. 排序后，可以按照TwoSum的思路来解题。怎么解呢？可以将num[i]的相反数即-num[i]作为target，
# 然后从i+1到len(num)-1的数组元素中寻找两个数使它们的和为-num[i]就可以了。下标i的范围是从0到
# len(num)-3。
# 3. 这个过程要注意去重。4，时间复杂度为O(N^2)。
此题的难点在于去重
"""



class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, num):
        num.sort()
        res = []
        for i in range(len(num)-2):
            if i == 0 or num[i] > num[i-1]:
                left = i + 1; right = len(num) - 1
                while left < right:
                    if num[left] + num[right] == -num[i]:
                        res.append([num[i], num[left], num[right]])
                        left += 1; right -= 1
                        while left < right and num[left] == num[left-1]: left +=1  #去重
                        while left < right and num[right] == num[right+1]: right -= 1
                    elif num[left] + num[right] < -num[i]:
                        while left < right:
                            left += 1
                            if num[left] > num[left-1]: break
                    else:
                        while left < right:
                            right -= 1
                            if num[right] < num[right+1]: break
        return res


"""
O(N^2)的解法, 对sum排序。先定下来a,在从a~末尾的这一段区间里找b,c, 两头往中间走。需要注意去重,
对于num=[-4,-1,-1,0,1,2]不要出来两组(-1,0,1). 以下解法很好地解释了如何去重。
"""
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        res = []
        sortnum = sorted(num)
        length = len(sortnum)
        # make sure a < b < c
        for i in xrange(length-2):
            a = sortnum[i]
            # remove duplicate a
            if i >= 1 and a == sortnum[i-1]:
                continue
            j = i + 1
            k = length - 1
            while j < k:
                b = sortnum[j]
                c = sortnum[k]
                if b + c == -a:
                    res.append([a,b,c])
                    # remove duplicate b,c
                    while j < k:
                        j += 1
                        k -= 1
                        if sortnum[j] != b or sortnum[k] != c:
                            break
                elif b + c > -a:
                    # remove duplicate c
                    while j < k:
                        k -= 1
                        if sortnum[k] != c:
                            break
                else:
                    # remove duplicate b
                    while j < k:
                        j += 1
                        if sortnum[j] != b:
                            break
        return res



"""
My own way to implement the idea:
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        res = []; n = len(nums)
        for i in range(n-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            else:
                left = i+1; right = n-1
                while left < right:
                    if nums[left] + nums[right] == -nums[i]:
                        res.append([nums[i],nums[left],nums[right]])
                        while left < right:
                            left += 1; right -= 1
                            if nums[left] != nums[left-1] or nums[right]!=nums[right+1]:
                                break
                    elif nums[left] + nums[right] > -nums[i]:
                        while left < right:
                            right -= 1
                            if nums[right]!= nums[right+1]:
                                break
                    else:
                        while left < right:
                            left += 1
                            if nums[left]!= nums[left-1]:
                                break
        return res

"""
借用4sum的idea， 代码很简洁; 用了dictionary开了额外存储
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = dict();n = len(nums);ans = set()
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] not in d:
                    d[nums[i]+nums[j]] = [(i,j)]
                else:
                    d[nums[i]+nums[j]].append((i,j))
        for i in range(n):
            t = 0 - nums[i]
            if t in d:
                for k in d[t]:
                    if k[0] > i:
                        ans.add((nums[i],nums[k[0]],nums[k[1]]))
        return [list(i) for i in ans]


"""
discussion的解法
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []; n = len(nums)    
        for i in range(n-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            left = i + 1; right = n-1
            while left < right:
                sums = nums[left] + nums[right] + nums[i]                
                if sums == 0:
                    ans.append(([nums[i],nums[left],nums[right]]))
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1;right -= 1
                elif sums < 0:  #注意一定要是elif
                    left += 1
                else:
                    right -= 1
               
        return ans





        