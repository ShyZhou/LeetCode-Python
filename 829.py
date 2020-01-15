# Consecutive Numbers Sum

# Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

# Example 1:
# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3

# Example 2:
# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

# Example 3:
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5


a + (a + 1) + (a + 2) + ... + (a + n - 1) = (a + a + n - 1) * n = 2 * N
(2a + n - 1) * n = 2 * N

# N = x + (x + 1) + (x + 2) + ... + (x + k), x >= 0, k >= 1
# k * (2 * x + k + 1) = 2 * N
# Try all k, 1 <= k <= 2 * N, see if x = (2 * N / k - k - 1) / 2 is an interger
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for k  in range(1, 2 * N + 1):
            if (2 * N) % k == 0:
                x = 2 * N / k - k - 1
                if x >= 0 and x % 2 == 0:
                    res += 1
        return res
