# Minimum Size Subarray Sum

"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(nlogn).
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
       	l = len(nums)
        res = l + 1
        i, j, cur_sum = 0, 0, 0
        while j < l:
            while cur_sum < s and j < l:
                cur_sum += nums[j]
                j += 1
            while cur_sum >= s:
                res = min(res, j - i)
                cur_sum -= nums[i]
                i += 1
        return res if res <= l else 0
