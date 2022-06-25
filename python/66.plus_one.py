"""
先变回整数，然后+1，最后再变回来
"""

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
    	i = int("".join([str(i) for i in digits]))
    	print 'i: ',i
        if i < 0:
            return None

    
        return [int(c) for c in str(i+1)]
# 弄清含义，e.g., 9+1 = 10 , 最后return[1,0]


"""
Solution 2: 直接处理进位
"""
def plusOne(self, digits):
        carry = 1
        i = len(digits) - 1
        while carry and i >= 0:
            d = digits[i] + carry
            carry = d / 10
            digits[i] = d % 10 # only for the first digit
            i -= 1
        if carry:
            return [1] + digits
        else:
            return digits

# *********** The Fourth Time *************
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''; ans = []
        for i in range(len(digits)):
            s += str(digits[i])

        t = int(''.join(str(s)))
        t += 1
        for e in str(t):
            ans.append(int(e))
        return ans


if __name__ == '__main__':
	a = Solution()
	print a.plusOne([9])