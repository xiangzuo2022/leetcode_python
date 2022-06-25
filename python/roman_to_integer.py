class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
    	romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}

        prev_value = total =0

        for i in range(len(s)-1, -1, -1):
            int_val = romans[s[i]]
            if int_val < prev_value:
                total -= int_val
            else:
                total += int_val
            prev_value = int_val

        return total



# **************** The Second Time *************
"""
# Solution: need to memorize
# From the end to the beginning
# 计数规则：
# 相同的数字连写，所表示的数等于这些数字相加得到的数，例如：III = 3
# 小的数字在大的数字右边，所表示的数等于这些数字相加得到的数，例如：VIII = 8
# 小的数字，限于（I、X和C）在大的数字左边，所表示的数等于大数减去小数所得的数，例如：IV = 4
# 正常使用时，连续的数字重复不得超过三次
# 在一个数的上面画横线，表示这个数扩大1000倍（本题只考虑3999以内的数，所以用不到这条规则）
"""


class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        d = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        right = total = 0
        for i in range(len(s)-1,-1,-1):  # from back to the front
            left = d[s[i]]
            if left < right:
                total -= left
            else:
                total += left
            right = left
        return total




if __name__ == '__main__':
	a = Solution()
	print a.romanToInt('MCMXCVI')