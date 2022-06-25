"""
解题思路：双指针思想，尾指针不断往后扫，当扫到有一个窗口包含了所有T的字符，然后再收缩头指针，
直到不能再收缩为止。最后记录所有可能的情况中窗口最小的。
"""
class Solution:
    # @return a string
    def minWindow(self, S, T):
        count1={}; count2={}
        for char in T:
            if char not in count1: count1[char]=1
            else: count1[char]+=1
        for char in T:
            if char not in count2: count2[char]=1
            else: count2[char]+=1
        count=len(T)
        start=0; minSize=100000; minStart=0
        for end in range(len(S)):
            if S[end] in count2 and count2[S[end]]>0:
                count1[S[end]]-=1
                if count1[S[end]]>=0:
                    count-=1
            if count==0:
                while True:
                    if S[start] in count2 and count2[S[start]]>0:
                        if count1[S[start]]<0:
                            count1[S[start]]+=1
                        else:
                            break
                    start+=1
                if minSize>end-start+1:
                    minSize=end-start+1; minStart=start
        if minSize==100000: return ''
        else:
            return S[minStart:minStart+minSize]




class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def isValid(a,b):
            for item in b:
                if item not in a or a[item] < b[item]:
                    return False
            return True
        source = collections.defaultdict(int)
        target = collections.defaultdict(int)
        for e in t:
            target[e] += 1
        ans = ''; j = 0; n = len(s); minLen = sys.maxint
        for i in range(n):
            while j < n and (isValid(source, target) == False):
                source[s[j]] += 1
                j += 1
            if isValid(source, target):
                if minLen > j-i+1:
                    minLen = j-i+1
                    ans = s[i:j]
            source[s[i]] -= 1
        return ans
            








