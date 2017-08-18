# Product of Array Except Self

"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""

# O(n) space
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        before = [1] * len(nums)
        after = [1] * len(nums)
        res = []

        for i in range(1, len(nums)):
            before[i] = before[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            after[i] = after[i+1] * nums[i+1]

        for i in range(0, len(nums)):
            res.append(before[i] * after[i])

        return res

# O(1) space
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        before = [1] * len(nums)
        after = 1

        for i in range(1, len(nums)):
            before[i] = before[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            after = after * nums[i+1]
            before[i] = before[i] * after

        return before