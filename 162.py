# Find Peak Element

"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Note:
Your solution should be in logarithmic complexity.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       	l = len(nums)
        if l == 1:
            return 0
        if l % 2 == 0:
            left = self.findPeakElement(nums[0:l/2])
            if (left != l/2 - 1 and left != 0) or nums[left] > nums[left + 1]:
                return left

            right = self.findPeakElement(nums[l/2:l])
            if (right != l/2 - 1 and right != 0) or nums[right+l/2] > nums[right+l/2 - 1]:
                return right + l/2

        else:
            left = self.findPeakElement(nums[0:(l-1)/2])
            if (left != (l-1)/2-1 and left != 0) or nums[left] > nums[left + 1]:
                return left

            right = self.findPeakElement(nums[(l+1)/2:l])
            if (right != (l-1)/2-1 and right != 0) or nums[right+(l+1)/2] > nums[right+(l+1)/2 - 1]:
                return right + (l+1)/2

            return (l-1)/2

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        s = 0
        e = l-1
        while s <= e:
            mid = (s + e) / 2
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == l - 1 or nums[mid] > nums[mid + 1]):
                return mid
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                e = mid - 1
            else:
                s = mid + 1