# Perfect Squares

"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

# DP
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [float('inf')] * (n + 1)
        res[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                res[i] = min(res[i], res[i - j ** 2] + 1)
        return res[n]

# Lagrange's four-square theorem https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
# 首先我们将数字化简一下，由于一个数如果含有因子4，那么我们可以把4都去掉，并不影响结果，比如2和8,3和12等等，返回的结果都相同
# 还有一个可以化简的地方就是，如果一个数除以8余7的话，那么肯定是由4个完全平方数组成
# 那么做完两步后，一个很大的数有可能就会变得很小了，大大减少了运算时间，下面我们就来尝试的将其拆为两个平方数之和，如果拆成功了那么就会返回1或2，因为其中一个平方数可能为0.
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n = n / 4
        if n % 8 == 7:
            return 4
        for i in range(int(math.sqrt(n)) + 1):
            j = int(math.sqrt(n - i ** 2))
            if i ** 2 + j ** 2 == n:
                return 1 if i == 0 or j == 0 else 2
        return 3
