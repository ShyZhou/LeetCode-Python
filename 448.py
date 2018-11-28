# Find All Numbers Disappeared in an Array

"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

# Method 1: switch a number to its correct postion
# 4,3,2,7,8,2,3,1
# 7,3,2,4,8,2,3,1
# 3,3,2,4,8,2,7,1
# 2,3,3,4,8,2,7,1
# 3,2,3,4,8,2,7,1
# 3,2,3,4,1,2,7,8
# 1,2,3,4,3,2,7,8
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)

        return res

# Method 2: for each i, change the number on position i to be negative if it's positive; otherwise, keep it negative
# negative means the number for the position is in array
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            nums[j] = -nums[j] if nums[j] > 0 else nums[j]

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res
