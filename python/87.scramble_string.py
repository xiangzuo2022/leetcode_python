# 解题思路：二叉树的问题一般使用递归来解决
# 1 递归：
# 简单的说，就是s1和s2是scramble的话，那么必然存在一个在s1上的长度l1，将s1分成s11和s12两段，同样有s21和s22。
# 那么要么s11和s21是scramble的并且s12和s22是scramble的 (交叉)；要么s11和s22是scramble的并且s12和s21是scramble的。
# 如果要能通过OJ，还必须把字符串排序后进行剪枝.

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
    	if len(s1) != len(s2): return False
    	if s1 == s2 : return True
    	l1 = list(s1);l2 = list(s2)  # convert string to list(array)
    	l1.sort();l2.sort
    	if l1 != l2: return False
    	n = len(s1)
    	for i in range(1,n):
    		if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
    			return True
    		if self.isScramble(s1[:i],s2[n-i:]) and self.isScramble(s1[i:],s2[:n-i]):
    			return True
    	return False
