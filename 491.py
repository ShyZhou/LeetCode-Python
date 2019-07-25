# Increasing Subsequences

"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
"""

# 递归
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        candidate = self._find_candidates(nums)
        return [a for a in candidate if len(a) > 1]

    def _find_candidates(self, nums):
        if len(nums) == 0:
            return set()
        res = self._find_candidates(nums[:-1])
        last = nums[-1]
        for a in list(res):
            if last >= a[-1]:
                res.add(a + (last,))
        res.add((last,))
        return res

# DP
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dp = set()
        for n in nums:
            for a in list(dp):
                if n >= a[-1]:
                    dp.add(a + (n,))
            dp.add((n,))
        return list(a for a in dp if len(a) > 1)

