# Longest Harmonious Subsequence

"""
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Note: The length of the input array will not exceed 20,000.
"""

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        s, e, res = 0, 0, 0
        while e < len(nums):
            if nums[e] > nums[s] + 1:
                res = max(res, e - s) if nums[e - 1] != nums[s] else res
                s += 1
            else:
                e += 1
        return max(res, e - s) if nums[e - 1] != nums[s] else res

from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        d = dict(Counter(nums))
        for k in sorted(d):
            if k + 1 in d:
                res = max(res, d[k] + d[k + 1])
        return res
