"""
Count set bits in an integer
Write an efficient program to count number of 1s in binary representation 
of an integer.
"""

def count_bit(n):
	count = 0
	while n:
		count += (n & 1)
		n >>= 1
	return count


"""
At Bit level, how will you find if a number is a power of 2 or not.
http://geekexplains.blogspot.com/2009/05/finding-if-number-is-power-of-2-or-not.html
"""
def power_of_two(n):
    return ((n&-n)==n)


"""
Swap two numbers using XOR
推导：
x1 = x xor y
y1 = x1 xor y
x2 = x1 xor y1

x2 = x1 xor y1
x2 = x1 xor (x1 xor y)   // replace y1
x2 = (x1 xor x1) xor y   // regroup parenthesis - order does not matter for XOR
x2 = 0 xor y             // a xor a => 0
x2 = y                   // 0 xor a => a; x2 now has y's original value
"""
x = x XOR y
y = x XOR y
x = x XOR y



if __name__ == '__main__':
	print count_bit(15)
