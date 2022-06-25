  # 解题思路：anagram的意思是：abc，bac，acb就是anagram。即同一段字符串的字母的不同排序。
  # 将这些都找出来。这里使用了哈希表，即Python中的dict。针对前面的例子来讲，映射为{abc：abc，bac，acb}。

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        
        dic={}
        res=[]
        for word in strs:
        	
           	S_word=''.join(sorted(word))
           	print 'Sword: ',S_word
           	dic[S_word]=[word] if S_word not in dic else dic[S_word]+[word]
        for key in dic:
            if len(dic[key]) > 1:
                res += dic[key]
        return res

if __name__ == '__main__':
	a = Solution()
	a.anagrams(['abc','bac','acb'])


#  ******** The Second Time *********
# 解法二：MLE, 注意此题是寻找anagrams不是产生， 以下解法是产生anagrams
class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
      def dfs(depth,start,value):
        if depth == len(strs):
          ans.append(value)
        for i in range(len(strs)):
          dfs(depth+1,i+1,value+[strs[i]])

      ans = []
      if strs == None : return ans
      dfs(0,0,[])
      return ans

# 我理解的anagrams的判别其实就是，把输入的单词按字母顺序排序，如果排序后是同一字典序，那么他们就是一类的。
# anagrams的意思是几个单词，如果每种字母出现的个数都相同，不考虑顺序，那么他们就是一类的。
# 输出所有是一类的单词，anagram【s】 所以如果一个单词和其他单词都不是一类的，那就不输出了。
class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
      d = {}
      ans = []
      for word in strs:
        s_word = ''.join(sorted(word))
        if s_word not in d:
          d[s_word] = [word]
        else:
          d[s_word] += [word]

      for key in d:
        if len(d[key]) > 1:
          ans += d[key]
      return ans



































