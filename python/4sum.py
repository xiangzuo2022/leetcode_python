class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):

        numLen, res, dict = len(num), set(), {} # set()解决重复问题
        if numLen < 4: return []
        num.sort()
        for p in range(numLen):
            for q in range(p+1, numLen): 
                if num[p]+num[q] not in dict:
                    dict[num[p]+num[q]] = [(p,q)]
                else:
                    dict[num[p]+num[q]].append((p,q))
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                T = target-num[i]-num[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j: # already sorted
                        	res.add((num[i],num[j],num[k[0]],num[k[1]]))
        return [list(i) for i in res]



# ************* The Second Time *************
"""
此题用递归会超时
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        def dfs(count,start,value):
            if target == 0 and count == 4:
                ans.append(value)
            for i in range(len(nums)):
                if target < nums[i] or count > 4:
                    return
                dfs(nums,target-nums[i],count+1,i+1,value+(nums[i]))
        ans = ()
        dfs(0,0,())
        return ans



class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        Solution.ans = []
        nums.sort()
        self.dfs(nums,target,0,0,[])
        return Solution.ans
        
    def dfs(self,nums,target,start,k,value):
        if target == 0 and k == 4:
            Solution.ans.append(value)
        for i in range(len(nums)):
            if target < nums[i] or k > 4:
                return
            self.dfs(nums,target-nums[i],k+1,i,value+[nums[i]])

# 以上两种方法都显示内存错误

"""
先对num排序, 然后建一个dictionary d, d[num[p]+num[q]] = [(p,q) pairs 满足num[p] + num[q]], 
而且这里的(p,q) pair总是满足p < q。然后用二层循环来搜, num[i]是四元组最小的数, num[j]是第二小的数, 
判断d中有没有target - num[i] - num[j]这个key的时间是O(1), 如果有这个key, 就把找到的四元组加入最后的
返回结果。res使用set()来去重, 否则对于输入[-3,-2,-1,0,0,1,2,3], 0会出现两个[-3, 0, 1, 2]
和两个[-2, -1, 0, 3]。这题去重的处理也是关键
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        d = {}; res = set(); n = len(nums) # 把res设为set类型是为了去重
        if n < 4 : return []
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] not in d:
                    d[nums[i]+nums[j]] = [(i,j)]
                else:
                    d[nums[i]+nums[j]].append((i,j))
        for i in range(n):
            for j in range(i+1,n-2):  
                T = target - nums[i] -nums[j]
                if T in d:
                    for k in d[T]:
                        if k[0] > j:  # 去重， 尤其是顺序不同的重复项
                            res.add((nums[i],nums[j],nums[k[0]],nums[k[1]]))
        return [list(i) for i in res] # 直接返回set类型不是题目想要的













