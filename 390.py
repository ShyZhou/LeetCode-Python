# Elimination Game

"""
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""

# TLE
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = list(range(1, n + 1))
        backward = False
        while len(l) > 1:
            print(l)
            s = -1 if backward else 0
            limit = len(l) + (1 if backward else 0)
            while abs(s) < limit:
                del l[s]
                s += 1 if not backward else -1
                limit -= 1
            backward = not backward
        return l[0]

# let f(n) be the final result of forward elimination (from left to right); b(n) be the result of backward elimination
# when n = 1, f(n) = b(n) = 1
# for any n, f(n) + b(n) = n + 1
# for n > 2, f(n) = 2 * b(n / 2)
# So, f(n) = 2 * (n / 2 + 1 - f(n / 2))
# https://blog.csdn.net/afei__/article/details/83689502
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 if n == 1 else 2 * (n / 2 + 1 - self.lastRemaining(n / 2))
