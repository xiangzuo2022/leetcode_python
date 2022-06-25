class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    
	def DFS(self, candidates, target, start, valuelist):
    length = len(candidates)
    if target == 0 and valuelist not in Solution.ret: return Solution.ret.append(valuelist)
    for i in range(start, length):
        if target < candidates[i]:
            return
        self.DFS(candidates, target - candidates[i], i + 1, valuelist + [candidates[i]])

    def combinationSum2(self, candidates, target):
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret


# ********* The third Time *********************
"""
Same idea as 39
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def dfs(candidates,target,depth,value):
            if target == 0 and value not in ans:
                return ans.append(value)
            for i in range(depth,len(candidates)):
                if target < candidates[i]:return 
                dfs(candidates,target-candidates[i],i+1,value+[candidates[i]])
        ans = []
        candidates.sort()
        dfs(candidates,target,0,[])
        return ans

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(start, target, value):
            n = len(candidates)
            if target == 0 and value not in ans:
                ans.append(value)
            for i in range(start,n):
                if target < candidates[i]:
                    break
                dfs(i+1, target-candidates[i], value+[candidates[i]])
        ans = []
        candidates.sort()
        dfs(0, target, [])
        return ans

"""
因为排过序所以可以这样去重
"""
class Solution:
   
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(candidates,target,sum,startIndex):
            if sum == target: res.append(path[:])
            for i in range(startIndex,len(candidates)):  #要对同一树层使用过的元素进行跳过
                if sum + candidates[i] > target: return 
                if i > startIndex and candidates[i] == candidates[i-1]: continue  #直接用startIndex来去重,要对同一树层使用过的元素进行跳过
                sum += candidates[i]
                path.append(candidates[i])
                backtrack(candidates,target,sum,i+1)  #i+1:每个数字在每个组合中只能使用一次
                sum -= candidates[i]  #回溯
                path.pop()  #回溯
        candidates = sorted(candidates)  #首先把给candidates排序，让其相同的元素都挨在一起。
        backtrack(candidates,target,0,0)
        return res



        
