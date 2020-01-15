# Subsets

# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# II

# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, index, res, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(nums, i + 1, res, path + [nums[i]])

        res = []
        dfs(nums, 0, res, [])
        return res

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, index, res, path):
            res.append(path)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                dfs(nums, i + 1, res, path + [nums[i]])

        res = []
        nums.sort()
        dfs(nums, 0, res, [])
        return res

sol = Solution()
print(sol.subsets(nums=[1,2,3]))
print(sol.subsetsWithDup(nums=[1,2,2]))
