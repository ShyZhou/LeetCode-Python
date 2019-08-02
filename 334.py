# Increasing Triplet Subsequence

"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:
Input: [1,2,3,4,5]
Output: true

Example 2:
Input: [5,4,3,2,1]
Output: false
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur = []
        for n in nums:
            if len(cur) == 0:
                cur.append(n)
            elif len(cur) == 1:
                if n > cur[0]:
                    cur.append(n)
                else:
                    cur[0] = n
            elif len(cur) == 2:
                if n > cur[1]:
                    return True
                else:
                    if n <= cur[0]:
                        cur[0] = n
                    else:
                        cur[1] = n
        return True if len(cur) == 3 else False

# x1 is smallest, x2 is second smallest
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x1 = x2 = float('inf')
        for n in nums:
            if n <= x1:
                x1 = n
            elif n <= x2:
                x2 = n
            else:
                return True
        return False
