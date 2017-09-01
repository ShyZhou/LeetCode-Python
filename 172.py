# Factorial Trailing Zeroes

"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # number of 5's in n!
        res = 0
        while (n > 0):
            n = n / 5
            res += n
        return res