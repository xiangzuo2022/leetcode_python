class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):

    	def dfs(num,string,res):
	    	if num == length:  # the last letter
	    		res.append(string)
	    		return
	    	for letter in dict[digits[num]]:
	    		dfs(num+1,string+letter,res)


    	if not digits:
    		return []
    	dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        res = []
        length = len(digits)
        dfs(0,'',res)
        return res



    

if __name__ == '__main__':
	a = Solution()
	print a.letterCombinations("")




# ******** The Second Time
# 解题思路：穷举所有可能的字符串使用dfs来解决。
class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        def dfs(num,value,res):
            if num == n:
                res.append(value)
                return
            for letter in d[digits[num]]:
                dfs(num+1,value+letter,res)

        d = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        if not digits:return []
        res = []
        n = len(digits)
        dfs(0,'',res)
        return res

"""
concise code
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(depth, value):
            if depth == len(digits):
                ans.append(value)
                return
            for letter in d[digits[depth]]:
                dfs(depth+1, value+letter)
            
            
        d = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        if not digits: return []
        ans = []
        dfs(0, '')
        return ans




class Solution(object):
    letterMap = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    ans = []
    s = ''
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        del self.ans[:]
        if digits == '':
            return self.ans
        self.backtracking(digits, 0)
        return self.ans
    
    def backtracking(self, digits, index):
        if index == len(digits):
            self.ans.append(self.s)
            return 
        else:
            letters = self.letterMap[digits[index]]
            for letter in letters:
                self.s += letter
                self.backtracking(digits, index+1)
                self.s = self.s[:-1]

