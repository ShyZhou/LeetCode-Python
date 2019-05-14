# Maximal Square

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    else:
                        dp[i][j] = 1
                res = max(res, dp[i][j])
        return res*res
