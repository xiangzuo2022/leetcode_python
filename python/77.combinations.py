class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
    	def dfs(start,valuelist):
    		if self.count == k:
    			res.append(valuelist)
    			return
    		for i in range(start,n+1):
    			self.count += 1
    			dfs(i+1,valuelist + [i])
    			self.count -= 1  #如果不减1， count就会一直增加， 但是我们需要count每次从0开始
    	res = []
    	self.count = 0
    	dfs(1,[])
    	return res

# backtrack template solution
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        def backpack(n, k, startIndex):
            if len(path) == k:                
                ans.append(path[:])
                return 
            for i in range(startIndex, n+1):
                path.append(i)               
                backpack(n, k, i+1)
                path.pop() # remove the previous results otherwise the results will be accumualted
        backpack(n, k, 1)
        return ans

"""
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}

def dfs( parameter ):
	if stop condtion or base case:
		# base case:
		update result
	    return	
	else:
		# general cases:
		for all possible next moves:		
		    select one next move
			dfs( paramter with selected next move )
			undo the selection	
		return
"""

"""
after trim, the speed is 8 times faster
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        def backpack(n, k, startIndex):
            if len(path) == k:                
                ans.append(path[:])
                return 
            for i in range(startIndex, n-(k-len(path))+2):
                path.append(i)               
                backpack(n, k, i+1)
                path.pop()
        backpack(n, k, 1)
        return ans
        
























