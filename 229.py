# Majority Element II

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

# Boyer-Moore Voting Algorithm https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # find 2 possible numbers
        a, b, cnt1, cnt2 = 0, 0, 0, 0
        for n in nums:
            if n == a:
                cnt1 += 1
            elif n == b:
                cnt2 += 1
            elif cnt1 == 0:
                a, cnt1 = n, 1
            elif cnt2 == 0:
                b, cnt2 = n, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # count occurrence
        cnt1, cnt2 = 0, 0
        for n in nums:
            if n == a:
                cnt1 += 1
            elif n == b:
                cnt2 += 1

        res = []
        if cnt1 * 3 > len(nums):
            res.append(a)
        if cnt2 * 3 > len(nums):
            res.append(b)
        return res
