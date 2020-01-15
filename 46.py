# Permutations

# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(candidate, path):
            if len(candidate) == 0:
                res.append(path)
                return
            for i in range(len(candidate)):
                dfs(candidate[:i] + candidate[i+1:], path + [candidate[i]])

        dfs(nums, [])
        return res

sol = Solution()
print(sol.permute(nums=[1,2,3]))
