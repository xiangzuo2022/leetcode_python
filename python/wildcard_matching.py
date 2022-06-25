# 难点在于如何处理"*"
# 遇到'*'时, 用star变量记录'*'在p中出现的位置, 用ss变量记录此时s字符串指针sPointer的位置, 
# 但不移动sPointer, 因为'*'可以匹配0个字符, ss表示这个'*'所能匹配到的位置。遇到不匹配的情况时, 
# 即走到if star!= -1时, pPointer被拉回到star的下一个位置, sPointer被拉回到ss的下一个位置, 
# 继续匹配。把s字符串走完, p中还可以剩下一堆'*', 如果p中还有其他字符就返回False了。
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
    	len_s = len(s); len_p = len(p)
    	pp = ps = ss = 0
    	start = -1
    	while ps < len_s:
    		if pp < len_p and (s[ps] == p[pp] or p[pp]=='?'):
    			pp += 1; ps += 1
    			continue
    		if pp < len_p and p[pp]=='*':
    			start = pp; pp+=1; ss = ps
    			continue
    		if start != -1:
    			pp = start + 1; ss += 1; ps = ss
    			continue
    		return False
    	while pp < len_p and p[pp] == '*':
    		pp += 1
    	if pp == len_p: return True
    	return False


# 可以理解为'?'就是与比较的字符相匹配
# For each element in s
# If *s==*p or *p == ? which means this is a match, then goes to next element s++ p++.
# If p=='*', this is also a match, but one or many chars may be available, so let us save this *'s position and the matched s position.
# If not match, then we check if there is a * previously showed up,
#        if there is no *,  return false;
#        if there is an *,  we set current p to the next element of *, and set current s to the next saved s position.

# e.g.
# abed
# ?b*d**
# a=?, go on, b=b, go on,
# e=*, save * position star=3, save s position ss = 3, p++
# e!=d,  check if there was a *, yes, ss++, s=ss; p=star+1
# d=d, go on, meet the end.
# check the rest element in p, if all are *, true, else false;

# Note that in char array, the last is NOT NULL, to check the end, use  "*p"  or "*p=='\0'".


