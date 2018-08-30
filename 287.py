# Find the Duplicate Number

"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

# http://bookshadow.com/weblog/2015/09/28/leetcode-find-duplicate-number/

# Time: O(nlogn), Space: O(1)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = 1
        max = len(nums) - 1
        while min < max:
            mid = int((min + max) / 2)
            cnt = 0
            for n in nums:
                if n <= mid:
                    cnt += 1
            if cnt <= mid:
                # nums have less than or equal to mid numbers whose values are less than mid
                # so, no duplicates in range [min, mid]
                min = mid + 1
            else:
                max = mid
        return min

# Time: O(n), Space: O(1)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
                slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]

            if slow == finder:
                return slow
