# Reverse Bits

"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	# 45 ms
    	return int('{0:032b}'.format(n)[::-1], 2)

    	# 43 ms
        s = ''
        while n:
            s += str(n % 2)
            n = n // 2
        return int(s.ljust(32, '0'), 2)

        # 39 ms
        r = 0
        b = 0
        while n:
            r = r * 2 + n % 2
            n = n // 2
            b += 1
        return 2 ** (32 - b) * r