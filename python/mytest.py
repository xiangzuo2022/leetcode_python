class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        i = len(digits) - 1
        while carry and i >= 0:            
            d = digits[i] + carry
            print("begin: ",d, digits[i])
            carry = d / 10
            digits[i] = d % 10
            print(carry, digits[i], d)
            i -= 1
        if carry:
            return [1] + digits
        else:
            return digits

a = Solution()
digits = [1,9,9]
print(a.plusOne(digits))


