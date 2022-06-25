"""
# 解题思路：列举出所有合法的括号匹配，使用dfs。如果左括号的数量大于右括号的数量的话，就不能产生合法的
# 括号匹配。
为什么不能right > left? 因为开始都是以左边开始， 结束的都是右括号
"""

class Solution:
    # @param {integer} n
    # @return {string[]}
    def helper(self,left,right,item,res):
    	if right < left:
    		return
    	if left == 0 and right == 0:
    		res.append(item)
    	if left > 0:
    		self.helper(left-1,right,item+'(',res)
    	if right > 0:
    		self.helper(left,right-1,item+')',res)


    def generateParenthesis(self, n):
    	if n == 0:
    		return []
    	res = []
    	self.helper(n,n,'',res)
    	return res
if __name__ == '__main__':
	a = Solution()
	print a.generateParenthesis(5)


# ************ The Second Time **************
"""
水中的鱼的解题思路：典型的递归。一步步构造字符串。当左括号出现次数<n时，就可以放置新的左括号。
当右括号出现次数小于左括号出现次数时，就可以放置新的右括号。
"""

class Solution:
    # @param {integer} n
    # @return {string[]}
    def judge(self,left,right,item,res):
        if right < left:return 
        if left == 0 and right == 0:
            res.append(item)
        if left > 0:
            self.judge(left-1,right,item+'(',res)
        if right > 0:
            self.judge(left,right-1,item+')',res)


    def generateParenthesis(self, n):
        res = []
        if n == 0: return []
        self.judge(n,n,'',res)
        return res


# ****** The fourth Time ******
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        value = []
        self.dfs(n,n,'',value)
        return value
        
    def dfs(self,left,right,item,value):
        if left > right:return
        if left == 0 and right == 0:
            value.append(item)
        if left > 0:
            self.dfs(left-1,right,item+'(',value)
        if right > 0:
            self.dfs(left,right-1,item+')',value)
        

"""
official solution
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。










