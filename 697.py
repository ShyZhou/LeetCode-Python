# Degree of an Array

"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6

Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""

import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums).most_common()
        res = len(nums)
        for t in counter:
            if t[1] == counter[0][1]:
                indexes = [index for index, value in enumerate(nums) if value == t[0]]
                res = min(indexes[-1] - indexes[0] + 1, res)
                if res == 1:
                    break
        return res

