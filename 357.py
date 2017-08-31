# Count Numbers with Unique Digits

"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        mul = 1
        for i in range(1, min(n, 10) + 1):
            mul = mul * min(9, (9 - i + 2))
            res += mul
        return res