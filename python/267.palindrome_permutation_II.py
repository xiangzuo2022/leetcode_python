class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counter = collections.Counter(s)
        odds = filter(lambda x: x % 2, counter.values())
        if len(odds) > 1:
            return []
        baseStr, mid = self.preProcess(counter)
        return self.dfs(baseStr, 0, mid, [baseStr + mid + baseStr[::-1]])

    def preProcess(self, counter):
        baseStr = mid = ""
        for char in counter:    
            if counter[char] % 2:
                mid = char
            baseStr += char*(counter[char]/2)
        return baseStr, mid

    def dfs(self, s, start, mid, ans):
        if start == len(s) - 1:
            return ans
        for i in range(start, len(s)):
            if i >= 1 and s[i] == s[i-1] == s[start]:
                continue 
            if i != start:
                permu = s[:start] + s[i] + s[start+1:i] + s[start] + s[i+1:] 
                ans.append(permu + mid + permu[::-1])
            else:
                permu = s
            self.dfs(permu, start+1, mid, ans)
        return ans