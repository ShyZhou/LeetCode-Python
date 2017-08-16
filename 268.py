# Missing Number

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # rec = [0 for i in range(len(nums)+1)]
        rec = [0] * (len(nums)+1)
        for n in nums:
            rec[n] = 1
        for i in range(len(rec)):
            if rec[i] == 0:
                return i