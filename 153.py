# Find Minimum in Rotated Sorted Array

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return None
        if l == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        return min(self.findMin(nums[0 : l/2]), self.findMin(nums[l/2 : l]))