class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):            
            x = num[i]
            if target-x in dict:
                return (dict[target-x]+1, i+1)
            dict[x] = i   # 有重复元素也没关系， 走不到重复的地方就已经返回了



# ********** The Second Time ***********
# 一下做法产生TLE: Time Limit Exceeded
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, num, target):
        n = len(num)
        d = {}
        for i in range(n):
            d[num[i]] = i
        for i in range(n):
            x = num[i]
            if target - x in num:
                if d[x] < d[target-x]:
                    return d[x],d[target-x]
                else:
                    return d[target-x],d[x]



"""
# Solution: 首先复制一份array，对其进行排序，找到符合条件的两个数 (use two pointers)，
# 再在原数组里找到index。利用字典的hash来查找，时间复杂度O(n），空间复杂度O(n)。
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, num, target):
        d = {}
        for index,x in enumerate(num,1):  # 从 1 算起， 默认是 0          
            if target - x in d:
                return d[target - x], index  #后面的会覆盖前面的，所以不用排序就能给出从小到大的顺序
            d[x] = index


"""
# Solution 2: 夹逼法 O(nlogn)， 注意不是binary search， 一开始我搞错了， 弄成binary search了
# 夹逼法比较直接， 所以代码冗长;对冲指针
"""

class Solution:
# @param {integer[]} nums
# @param {integer} target
# @return {integer[]}
def twoSum(self, nums, target):
    copynums = nums[:]  # deep copy the original array
    index = []
    copynums.sort()
    left = 0; right = len(nums)-1   
    
    while left < right:                  
        if copynums[left] + copynums[right] == target:                
            for k in range(0,len(nums)):
                if copynums[left] == nums[k]:                       
                    index.append(k)
                    break
            for k in range(len(nums)-1,-1,-1): # 这个地方要注意， array里可能有重复的元素，如果从头开始search，就会反复找到同一个index的元素，e.g.,[0,3,4,0]
                if copynums[right] == nums[k]:  # 如果找0的话， 总是找到index = 1
                    index.append(k)
                    break
            index.sort()                
            break
            
        elif copynums[left] + copynums[right] > target:                
            right = right - 1
        else:
            left = left + 1

    return (index[0]+1,index[1]+1)  # index从1 “1” 开始， 所以要加1 

"""
My own codes
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        copy = nums[:]
        copy.sort()
        left = 0; right = len(copy)-1;res=[0,0]
        while left < right:
            if copy[left] + copy[right] == target:
                for k in range(len(nums)):
                    if copy[left] == nums[k]:
                        res[0] = k
                        break
                for k in range(len(nums)-1,-1,-1):
                    if copy[right] == nums[k]:
                        res[1] = k
                        break
                res.sort()
                break
            elif copy[left] + copy[right] < target:
                left += 1
            else:
                right -= 1
        return [res[0]+1,res[1]+1]

"""
My own solution 2
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        d = dict();ans = []
        for i in range(0,n):
            if target-nums[i] in d:
                if i < d[target-nums[i]]:  #要求输出的index升序， 所以要判断一下
                    return i+1,d[target-nums[i]]+1                    
                else:
                    return d[target-nums[i]]+1, i+ 1
            else:
                d[nums[i]] = i
        return ans


"""
my code according to jiuzhang solution
此题无论哪种解法必须用到 O(n)的存储空间
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        copy = nums[:]
        nums.sort()
        ans = [0,0]
        left = 0; right = n-1 
        while left < right:
            if (nums[left] + nums[right]) > target:
                right -= 1
            elif (nums[left] + nums[right]) < target:
                left += 1
            else:
                for k in range(n):
                    if nums[left] == copy[k]:
                        ans[0] = k
                        break
                for m in range(n-1,-1,-1):
                    if nums[right] == copy[m]:
                        ans[1] = m
                        break
                ans.sort()
                break
        return ans


if __name__ == '__main__':
    a = Solution()
    print a.twoSum([0,4,3,0],0)












