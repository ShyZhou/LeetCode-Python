# Number of Boomerangs

"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""

from collections import defaultdict
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(points)
        for i in range(n):
            # dmap = {}
            # for j in range(n):
            #     distance = pow((points[i][0] - points[j][0]), 2) + pow((points[i][1] - points[j][1]), 2)
            #     dmap[distance] = dmap[distance] + 1 if distance in dmap else 1

            # a Python dictionary throws a KeyError if you try to get an item with a key that is not currently in the dictionary.
            # The defaultdict in contrast will simply create any items that you try to access.
            dmap = defaultdict(int)
            for j in range(n):
                dmap[pow((points[i][0] - points[j][0]), 2) + pow((points[i][1] - points[j][1]), 2)] += 1

            for d in dmap:
                res += dmap[d] * (dmap[d] - 1)
        return res
