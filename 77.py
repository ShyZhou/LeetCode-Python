# Combinations

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# Example:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# recursion
class Solution(object):
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n + 1)
               for pre in self.combine(i - 1, k - 1)]

# backtracking
class Solution(object):
    def combine(self, n, k):
        res = []
        self.helper(range(1, n + 1), k, res, [])

    def helper(self, array, k, res, path):
        if k > len(array):
            return
        if k == 0:
            res.append(path)
        else:
            for i in range(len(array)):
                self.helper(array[i + 1:], k - 1, res, path + [array[i]])
