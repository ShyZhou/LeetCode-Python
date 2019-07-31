# Target Sum

"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

# Time Limit Exceeded
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 1:
            return (nums[0] == S) + (nums[0] == -S)
        return self.findTargetSumWays(nums[:-1], S - nums[-1]) + self.findTargetSumWays(nums[:-1], S + nums[-1])

# DP, 状态转移方程：dp[i + 1][k + nums[i] * sgn] += dp[i][k], sgn取值±1，k为dp[i]中保存的所有状态；初始令dp[0][0] = 1
import collections
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = collections.Counter()
        dp[0] = 1
        for n in nums:
            ndp = collections.Counter()
            for sign in (1, -1):
                for k in dp.keys():
                    ndp[k + n * sign] += dp[k]
            dp = ndp
        return dp[S]
