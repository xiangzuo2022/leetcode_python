"""
# 解题思路：这道题使用bfs来解决。使用BFS, 单词和length一块记录, dict中每个单词只能用一次, 所以用过即删。
# dict给的是set类型, 检查一个单词在不在其中(word in dict)为O(1)时间。设单词长度为L, dict里有N个单词, 
# 每次扫一遍dict判断每个单词是否与当前单词只差一个字母的时间复杂度是O(N*L), 而每次变换当前单词的一个字母, 
# 看变换出的词是否在dict中的时间复杂度是O(26*L), 所以要选择后者。
此题很有意思，用了小技巧
"""


class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
    	#wordDict.add(endWord)
        wordDict = set(wordDict)
    	q = []
    	q.append((beginWord,1)) # 记录单词的同时也记录长度
    	while q:
    		curr = q.pop(0)
    		currword = curr[0]; currlen = curr[1]
    		if currword == endWord: return currlen
    		for i in range(len(beginWord)):
    			part1 = currword[:i]; part2 = currword[i+1:] # part 1中currwrod[i]是取不到的
    			for j in 'abcdefghijklmnopqrstuvwxyz':
    				if currword[i] != j:
    					nextword = part1 + j + part2
    					if nextword in wordDict:
    						q.append((nextword,currlen+1))
    						wordDict.remove(nextword)  #不移去已经出现的词会再次出现不满足题意
    	return 0



"""
BFS in a better coding style
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
    
# https://www.youtube.com/watch?v=h9iTnkgv05E
# Graph

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(wordList)):
                pattern = word[:j] + "*" + word[j+1:] # this is the trick
                nei[pattern].append(word)

        visit = set([beginWord])
        # BFS to get shortest path
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0

