# Super Pow

"""
Your task is to calculate a^b mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024
"""

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = 1
        for i, n in enumerate(b):
            res = self.pow(res, 10) * self.pow(a, n) % 1337
        return res

    def pow(self, a, b):
        if a == 1 or b == 0:
            return 1
        if b == 1:
            return a % 1337

        h = self.pow(a % 1337, b / 2)
        if b % 2 == 0:
            return h * h % 1337
        else:
            return h * h * a % 1337
