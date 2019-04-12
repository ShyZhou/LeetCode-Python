# Sum of Square Numbers

"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a^2 + b^2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: 3
Output: False
"""

import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(math.sqrt(c)) + 1):
            b = c - math.pow(a, 2)
            if math.pow(int(math.sqrt(b)), 2) == b:
                return True
        return False


