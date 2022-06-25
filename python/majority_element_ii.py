"""
# 观察可知，数组中至多可能会有2个出现次数超过 ⌊ n/3 ⌋ 的众数 记变量n1, n2为候选众数； c1, c2为它们对应的出现次数
# 遍历数组，记当前数字为num, 若num与n1或n2相同，则将其对应的出现次数加1, 否则，若c1或c2为0，则将其置为1，对应的候选众数置为num
# 否则，将c1与c2分别减1, 最后，再统计一次候选众数在数组中出现的次数，若满足要求，则返回之。
# 首先，可以通过分析得到结论：满足条件的数字个数cnt最多为2。 
#　　证明： if cnt>2⇒cnt× (⌊n/3⌋+1 )>n 超出原数组的大小。 
#　然后，借鉴在数组中求出现次数超过一半的数这道题的思路：　 
#　　1). 第一遍扫描，设两个计数器和变量记录数组nums[]中出现频率最高的数。 
#　　2). 第二遍扫描，计算着两个数出现的次数。 
#　　3). 判断这两个数是否符合要求，符合则存入结果集。
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
    	first = second = 0
    	num1 = num2 = 0
    	ans = []
    	for i in range(len(nums)):  #核心在这个循环
    		if first == 0 or num1 == nums[i]:
    			num1 = nums[i]
    			first += 1
    		elif second == 0 or num2 == nums[i]:
    			num2 = nums[i]
    			second += 1
    		else:
    			first -= 1  # 用来抵消的
    			second -= 1

    	first = second = 0
    	for i in range(len(nums)):
    		if nums[i] == num1:
    			first += 1
    		if nums[i] == num2:
    			second += 1

    	if first > len(nums)/3 and num1 not in ans: # 避免重复
    		ans.append(num1)
    	if second > len(nums)/3 and num2 not in ans:
    		ans.append(num2)
    	return ans

"""
Solution 2: 用了额外的存储空间是题目不允许的
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        d = {};res = []
        n = len(nums)
        if n == 0:return []
        m = n/3
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        for key in d:
            if d[key] > m:
                res.append(key)
        return res


"""
Boyer-Moore Algorithm: two passes
http://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:return []
        count1,count2,e1,e2 = 0,0,0,1
        for i in nums:
            if i == e1: count1+=1
            elif i == e2: count2+=1
            elif count1 == 0:
                e1 = i
                count1+= 1
            elif count2 == 0:
                e2 = i
                count2+=1
            else:
                count1, count2 = count1-1,count2-1
        return [e for e in (e1,e2) if nums.count(e) > len(nums)/3]











