# Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -float('inf')
        cur_sum = nums[0]
        for n in nums[1:]:
            if n >= 0:
                cur_sum = n if cur_sum < 0 else cur_sum + n
            else:
                res = max(res, cur_sum)
                cur_sum = n
        return res
