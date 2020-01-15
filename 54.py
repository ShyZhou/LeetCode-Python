# Spiral Matrix

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        res = matrix[0][:]
        if m > 2:
            res += [x[-1] for x in matrix[1:m-1]]
        if m > 1:
            res += matrix[m-1][:][::-1]
        if m > 2 and n > 1:
            res += [x[0] for x in matrix[1:m-1]][::-1]

        return res + self.spiralOrder([x[1:n-1] for x in matrix[1:m-1]])

sol = Solution()
print(sol.spiralOrder([[1], [5], [9]]))
