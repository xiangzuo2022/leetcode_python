

# class Solution:
#     # @param n, an integer
#     # @return an integer
#     def hammingWeight(self, n):
    	
#     	return bin(n).count('1')  # this will not be accecped by interview





# ************* The Second Time ********
"""
# convert an integer to bits, << 2^b
# You can think of left-shifting by b 
# as multiplication by 2b and right-shifting as integer division by 2b. 
# http://www.cnblogs.com/drizzlecrj/archive/2007/03/13/672576.html

"""
class Solution:

    # @param n, an integer
    # @return an integer
     def hammingWeight(self, n):  # n 是32位的
        ans = 0
        while n:        
           	ans += n & 1          	
           	n >>= 1  # n divides by 2^1 (2)            
        return ans


"""
延伸一下：假设我们想要找到x的最低位(非0位)。如果我们从x中减1，那么这个位就清除了，但是x中其他所有的位都还存在。
因此, x & ~(x-1)包含了x的最低设置位。
"""



# Solution 2
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0        
        while n != 0: 
            count += 1
            n = n & (n - 1)  # Remove the last 1-bit.        
        return count

    	

if __name__ == '__main__':
	a = Solution()
	n = 11
	a.hammingWeight(n)
        