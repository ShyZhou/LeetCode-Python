# Valid Perfect Square

"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True

Example 2:

Input: 14
Returns: False
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # the nth square number can be computed from the previous square by n^2 = (n − 1)^2 + (2n − 1)
        n = 1
        sq = 0
        while sq < num:
            sq = sq + 2 * n - 1
            if sq == num:
                return True
            n += 1
        return False
