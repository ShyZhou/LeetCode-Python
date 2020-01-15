# Rotate Array

"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:
Could you do it in-place with O(1) extra space?
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        l = len(nums)
        k = k % l
        for i in range(k):
            tmp = nums.pop()
            nums.insert(0, tmp)
        return

class Solution(object):
    def rotate(self, nums, k):
        for _ in range(k):
            nums.insert(0, nums.pop())

class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

class Solution(object):
    def rotate(self, nums, k):
        q = collections.deque(nums)
        q.rotate(k)
        nums[:] = q
