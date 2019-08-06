# Diagonal Traverse

"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
"""

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])

        res = []
        use_reverse = True

        for j in range(n):
            i = 0
            k = j
            cur_arr = []
            while i < m and k >= 0:
                cur_arr.append(matrix[i][k])
                i += 1
                k -= 1
            if use_reverse:
                cur_arr.reverse()
            res += cur_arr
            use_reverse = not use_reverse

        for i in range(1, m):
            j = n - 1
            k = i
            cur_arr = []
            while k < m and j >= 0:
                cur_arr.append(matrix[k][j])
                j -= 1
                k += 1
            if use_reverse:
                cur_arr.reverse()
            res += cur_arr
            use_reverse = not use_reverse

        return res
