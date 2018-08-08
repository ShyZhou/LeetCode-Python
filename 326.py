# Power of Three

"""
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while (n > 1 and n % 3 == 0):
            n = n / 3
        return n == 1


# No loop / recursion
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # integer is 0-2^31, so max value within the range is 3^19 = 1162261467
        return True if (n > 0 and 1162261467 % n == 0) else False
