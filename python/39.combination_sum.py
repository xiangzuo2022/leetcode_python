class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
    	candidates.sort()
    	solution.net = []
    	self.DFS(candidates,target,0,[])
    	return solution.net

    def DFS(self,candidates,target,start,valuelist):
    	length = len(candidates)
    	if target == 0:
    		return solution.net.append(valuelist)
    	for i in range(start,length):
    		if target < candidates[i]:  # cannot find then return to terminate
    			return 
    		self.DFS(candidates,target-candidates[i],i,valuelist+[candidates[i]])


"""
穷举的时候一般考虑DFS，DFS就是递归
"""

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        candidates.sort()
        Solution.ans = []
        self.dfs(candidates,target,0,[])
        return Solution.ans

    def dfs(self,candidates,target,start,value):
        n = len(candidates)
        if target == 0:
            Solution.ans.append(value)
        for i in range(start,n):
            if target < candidates[i]:
                return
            self.dfs(candidates,target-candidates[i],i,value+[candidates[i]])



# ********* The Third Time *********

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates,target,start,value):
            if target == 0:
                ans.append(value)
            for i in range(start,len(candidates)):
                if target < candidates[i]: # 这个条件很关键
                    return
                dfs(candidates,target-candidates[i],i,value+[candidates[i]]) # 用i不用i+1是为了重复选取， 要配合上面的条件一起
                
        candidates.sort()  #关键在sort
        ans = []
        dfs(candidates,target,0,[])
        return ans



# my own solution
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates,sums,target,start,value):
            if sums == target:
                res.append(value)
            for i in range(start,len(candidates)):
                if candidates[i] > target - sums:return  # 关键在这，递归要有终止条件
                dfs(candidates,sums+candidates[i],target,i,value+[candidates[i]])
        
        candidates.sort()
        res = []
        dfs(candidates,0,target,0,[])
        return res


"""
可以这样写
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(start,target,value):
            if target == 0:
                ans.append(value)
            for i in range(start,len(candidates)):
                if target < candidates[i]:
                    break
                dfs(i,target-candidates[i],value+[candidates[i]]) # 这里i不是i+1, 因为同一个数可以被无数次的选择
        ans = []
        candidates.sort() # 一个关键点
        dfs(0,target,[])
        return ans
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        def backtrack(candidates,target,sum,startIndex):
            if sum > target: return 
            if sum == target: return res.append(path[:])
            for i in range(startIndex,len(candidates)):
                if sum + candidates[i] >target: return  #如果 sum + candidates[i] > target 就终止遍历
                sum += candidates[i] 
                path.append(candidates[i])
                backtrack(candidates,target,sum,i)  #startIndex = i:表示可以重复读取当前的数
                sum -= candidates[i]  #回溯
                path.pop()  #回溯
               
        candidates = sorted(candidates)  #需要排序
        backtrack(candidates,target,0,0)
        return res








            

