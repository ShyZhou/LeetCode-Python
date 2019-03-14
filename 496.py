# Next Greater Element I

"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""

# Brute force, O(len(nums1) * len(nums2))
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for n1 in nums1:
            # pprint.pprint(n1)
            found = 0
            for n2 in nums2:
                if n2 == n1:
                    found = 1
                if found == 1 and n2 > n1:
                    res.append(n2)
                    found = 0
                    break
            if found == 1:
                res.append(-1)
        return res

# Use Stack, O(len(nums2) + len(nums1))
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dmap = {} # map from each n in nums2 to next greater element of n
        stack = [] # stack to keep a decreasing sequence
        for n2 in nums2:
            while stack and stack[-1] < n2:
                # if we see n2 greater than the top element in stack, pop all element less than n2
                # and their next greater element is n2
                dmap[stack.pop()] = n2
            stack.append(n2)
        return [dmap.get(n1, -1) for n1 in nums1]
