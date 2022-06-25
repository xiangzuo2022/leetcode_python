# 主字符串S，模式字符串list：L（L中的元素等长，有可能重复），寻找L以任意顺序拼接后得到的字符串在S中的索引。
# 解题思路：使用一个字典统计一下L中每个单词的数量。由于每个单词的长度一样，以题中给的例子而言，
# 可以3个字母3个字母的检查，如果不在字典中，则break出循环。有一个技巧是建立一个临时字典curr，
# 用来统计S中那些在L中的单词的数量，必须和L中单词的数量相等，否则同样break。
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, L):
    	words = {}; wordNum = len(L)
    	for i in L:
    		if i not in words:
    			words[i] = 1
    		else:
    			words[i] += 1
    	wordLen = len(L[0])   # 每个单词长度一样
    	res = []
    	for i in range(len(s)+1-wordLen*wordNum): # wordLen*wordNum is L中letter的数目
    		curr = {}; j = 0
    		while j < wordNum:
    			word = s[i+j*wordLen:i+j*wordLen+wordLen] #因为长度固定，可以几个字母一起检查
    			if word not in words: break
    			if word not in curr: 
    				curr[word] = 1
    			else:
    				curr[word] += 1
    			if curr[word] > words[word]:
    				break
    			j += 1
    		if j == wordNum:
    			res.append(i)
    	return res

# in line 18, range(len(s)+1-wordLen*wordNum) relates to the line 21. 
# 有很多细节的处理还需要注意

    	


