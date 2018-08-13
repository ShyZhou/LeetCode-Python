# Intersection of Two Arrays II

"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
                num1_dict = {}
        for n in nums1:
            if n in num1_dict:
                num1_dict[n] += 1
            else:
                num1_dict[n] = 1

        res = []
        for n in nums2:
            if n in num1_dict:
                res.append(n)
                num1_dict[n] -= 1
                if num1_dict[n] == 0:
                    num1_dict.pop(n)

        return res
