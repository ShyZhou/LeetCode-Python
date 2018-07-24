# Largest Number

"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a, b):
            t1 = str(a)+str(b)
            t2 = str(b)+str(a)
            if t1 > t2:
                return -1
            elif t1 < t2:
                return 1
            return 0

        num = sorted(nums, cmp=compare)
        if num[0] == 0:
            return '0'
        return ''.join(str(n) for n in num)