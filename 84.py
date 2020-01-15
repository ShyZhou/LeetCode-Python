# Largest Rectangle in Histogram

# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

# Example:
# Input: [2,1,5,6,2,3]
# Output: 10

# 向前遍历所有的值，算出共同的矩形面积，每次对比保留最大值
# 只要对局部峰值处理!
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(heights)):
            if i < len(heights) - 1 and heights[i + 1] >= heights[i]:
                continue
            min_h = heights[i]
            for j in range(i, -1, -1):
                min_h = min(min_h, heights[j])
                res = max(res, min_h * (j - i + 1))
        return res

# https://www.cnblogs.com/boring09/p/4231906.html
# 单调栈
class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        res = 0
        heights.append(0)
        for i in range(len(heights)):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack[-1]]
                    stack.pop()
                    w = i if not stack else i - stack[-1] + 1
                    res = max(res, h * w)
                stack.append(i)
        return res


# Maximal Rectangle

# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example:

# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            res = max(res, self.largestRectangleArea(heights=heights))
        return res

# Maximal Square

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:
# Input:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        dp = [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = 1 if matrix[i][j] = 1 else 0
                elif matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                res = max(res, dp[i][j])
        return res * res
