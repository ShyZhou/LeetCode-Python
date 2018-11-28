# Find All Duplicates in an Array

"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

# Similar question / solution to # 448 - Find All Numbers Disappeared in an Array
class Solution(object):
    def findDuplicates(self, nums):
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
                res.append(nums[i])

        return res
