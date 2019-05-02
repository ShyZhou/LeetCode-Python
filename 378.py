# Kth Smallest Element in a Sorted Matrix

"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.

Note:
You may assume k is always valid, 1 ≤ k ≤ n^2.
"""

# min-heap
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        h = [(matrix[0][0], 0, 0)]
        res = None
        for _ in range(k):
            res, i, j = heapq.heappop(h)
            if j == 0 and i < m - 1:
                heapq.heappush(h, (matrix[i + 1][j], i + 1, j))
            if j < n - 1:
                heapq.heappush(h, (matrix[i][j + 1], i, j + 1))
        return res

# binary search
import bisect
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l, h = matrix[0][0], matrix[-1][-1]
        while l <= h:
            mid = (l + h) >> 1
            loc = sum(bisect.bisect(m, mid) for m in matrix)
            if loc >= k:
                h = mid - 1
            else:
                l = mid + 1
        return l

# binary search optimization
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l, h = matrix[0][0], matrix[-1][-1]
        while l <= h:
            mid = (l + h) >> 1
            loc = self.SmallerNumberCount(matrix, mid)
            if loc >= k:
                h = mid - 1
            else:
                l = mid + 1
        return l

    def SmallerNumberCount(self, matrix, num):
        i, j = len(matrix) - 1, 0
        cnt = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > num:
                i -= 1
            else:
                cnt += i + 1
                j += 1
        return cnt
