# Longest Increasing Subsequence

"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.

Follow up: Could you improve it to O(nlogn) time complexity?
"""

# DP
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       	res = 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + 1 if nums[j] < nums[i] else 1)
            res = max(res, dp[i])
        return res

# DP, sort the dp list
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in sorted(range(len(dp[:i])), key=dp[:i].__getitem__, reverse=True):
                if nums[j] < nums[i]:
                    dp[i] = dp[j] + 1
                    break
            res = max(res, dp[i])
        return res
