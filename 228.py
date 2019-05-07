# Summary Ranges

"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        i, j = 0, 1
        res = []
        while j < len(nums):
            if nums[j] == nums[j - 1] + 1:
                j += 1
            else:
                res.append(str(nums[i])) if j - 1 == i else res.append(str(nums[i]) + '->' + str(nums[j - 1]))
                i = j
                j += 1
        res.append(str(nums[i])) if j - 1 == i else res.append(str(nums[i]) + '->' + str(nums[j - 1]))
        return res
