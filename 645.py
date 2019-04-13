# Set Mismatch

"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0] * len(nums)
        for i in nums:
            count[i - 1] += 1
        res = [0] * 2
        for i in range(len(count)):
            if count[i] == 2:
                res[0] = i + 1
            if count[i] == 0:
                res[1] = i + 1
            if res[0] > 0 and res[1] > 0:
                break
        return res
