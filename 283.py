# Move Zeroes

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ni = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                if ni == 0:
                    ni = i + 1
                for j in range(ni, len(nums)):
                    if nums[j] != 0:
                        n = nums[i]
                        nums[i] = nums[j]
                        nums[j] = n
                        break
                    ni = ni + 1
                if ni == len(nums) - 1:
                    break
        return