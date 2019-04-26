# Rotated Digits

"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:
N will be in range [1, 10000].
"""

# Using set, s & t: elements common to s and t; s | t: elements from both s and t; s - t: elements in s but not t
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        must_set = set('2569')
        optional_set = set('018')
        res = 0
        for n in range(1, N+1):
            number_set = set(str(n))
            if (number_set & must_set) == set(''):
                continue
            if (number_set | must_set) == must_set:
                res += 1
            elif ((number_set - must_set) | optional_set) == optional_set:
                res += 1
        return res

# Using regex
import re
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        pattern = re.compile(r'^[0182569]*[2569]+[0182569]*$')
        return sum(True if pattern.match(str(n)) else False for n in range(1, N+1))
