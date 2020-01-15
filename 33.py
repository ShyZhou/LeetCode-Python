# Search in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Follow up:
# nums may contain duplicates.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] < nums[r]:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

    def search2(self, nums, target):
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            # 如果中值和左边值相等，无法判断左边有序还是右边有序，只能说明左值不是结果，只能l++
            # 1,2,3,3,3,3,3 -> 3,3,3,3,3,1,2 or 3,1,2,3,3,3,3
            if nums[m] == nums[l]:
                l += 1
            elif nums[m] > nums[l]: # 左边有序
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else: # 右边有序
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False

sol = Solution()
print(sol.search(nums=[4,5,6,7,0,1,2], target=0))
print(sol.search2(nums=[2,5,6,0,0,1,2], target=3))
