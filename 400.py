# Nth Digit

"""
Find the n-th digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 2^31).

Example 1:

Input:
3

Output:
3

Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        s = 0
        while True:
            if n <= 9 * i * 10 ** (i - 1):
                pos = (n - s) % i
                return int(str(10 ** (i - 1) + int((n - s - 1) / i))[(pos - 1) % i])
            else:
                s += 9 * i * 10 ** (i - 1)
                i += 1
