# Majority Element

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = None
        count = 1
        for n in nums:
            if n == majority:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority = n
                count = 1
        return majority